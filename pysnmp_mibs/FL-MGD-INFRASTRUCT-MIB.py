# SNMP MIB module (FL-MGD-INFRASTRUCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/phoenix/FL-MGD-INFRASTRUCT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:25 2025
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
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(RouterID,
 ospfAreaEntry,
 ospfIfEntry,
 ospfVirtIfEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "RouterID",
    "ospfAreaEntry",
    "ospfIfEntry",
    "ospfVirtIfEntry")

(PortList,
 dot1qStaticMulticastEntry,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "dot1qStaticMulticastEntry",
    "dot1qVlanIndex")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfEntry")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(vrrpOperVrId,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperVrId")


# MODULE-IDENTITY

flMgdInfrastructureMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 1, 8)
)
if mibBuilder.loadTexts:
    flMgdInfrastructureMibModule.setRevisions(
        ("2019-01-21 08:00",
         "2018-03-22 08:00",
         "2017-03-24 08:00",
         "2016-07-12 08:00",
         "2015-03-19 08:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledDisabledStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableStatus", 0),
          ("enableStatus", 1))
    )



class OpModeType(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("station", 0),
          ("master", 1),
          ("scb", 2),
          ("mcb", 3),
          ("ftb", 4),
          ("repeater", 5),
          ("machine-admin", 6))
    )



class EtypeValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_PhoenixContact_ObjectIdentity = ObjectIdentity
phoenixContact = _PhoenixContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346)
)
_PxcModules_ObjectIdentity = ObjectIdentity
pxcModules = _PxcModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 1)
)
_PxcGlobal_ObjectIdentity = ObjectIdentity
pxcGlobal = _PxcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 2)
)
_PxcBasic_ObjectIdentity = ObjectIdentity
pxcBasic = _PxcBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 2, 1)
)
_PxcBasicName_Type = DisplayString
_PxcBasicName_Object = MibScalar
pxcBasicName = _PxcBasicName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 2, 1, 1),
    _PxcBasicName_Type()
)
pxcBasicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxcBasicName.setStatus("current")
_PxcBasicDescr_Type = DisplayString
_PxcBasicDescr_Object = MibScalar
pxcBasicDescr = _PxcBasicDescr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 2, 1, 2),
    _PxcBasicDescr_Type()
)
pxcBasicDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxcBasicDescr.setStatus("current")
_PxcBasicURL_Type = DisplayString
_PxcBasicURL_Object = MibScalar
pxcBasicURL = _PxcBasicURL_Object(
    (1, 3, 6, 1, 4, 1, 4346, 2, 1, 3),
    _PxcBasicURL_Type()
)
pxcBasicURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxcBasicURL.setStatus("current")
_PxcFactoryLine_ObjectIdentity = ObjectIdentity
pxcFactoryLine = _PxcFactoryLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11)
)
_FlGlobal_ObjectIdentity = ObjectIdentity
flGlobal = _FlGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1)
)
_FlBasic_ObjectIdentity = ObjectIdentity
flBasic = _FlBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 1)
)
_FlBasicName_Type = DisplayString
_FlBasicName_Object = MibScalar
flBasicName = _FlBasicName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 1, 1),
    _FlBasicName_Type()
)
flBasicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flBasicName.setStatus("current")
_FlBasicDescr_Type = DisplayString
_FlBasicDescr_Object = MibScalar
flBasicDescr = _FlBasicDescr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 1, 2),
    _FlBasicDescr_Type()
)
flBasicDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flBasicDescr.setStatus("current")
_FlBasicURL_Type = DisplayString
_FlBasicURL_Object = MibScalar
flBasicURL = _FlBasicURL_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 1, 3),
    _FlBasicURL_Type()
)
flBasicURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flBasicURL.setStatus("current")


class _FlBasicCompCapacity_Type(Integer32):
    """Custom type flBasicCompCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlBasicCompCapacity_Type.__name__ = "Integer32"
_FlBasicCompCapacity_Object = MibScalar
flBasicCompCapacity = _FlBasicCompCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 1, 4),
    _FlBasicCompCapacity_Type()
)
flBasicCompCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flBasicCompCapacity.setStatus("current")
_FlComponents_ObjectIdentity = ObjectIdentity
flComponents = _FlComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 2)
)
_FlComponentsTable_Object = MibTable
flComponentsTable = _FlComponentsTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    flComponentsTable.setStatus("current")
_FlComponentsEntry_Object = MibTableRow
flComponentsEntry = _FlComponentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 2, 1, 1)
)
flComponentsEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flComponentsIndex"),
)
if mibBuilder.loadTexts:
    flComponentsEntry.setStatus("current")


class _FlComponentsIndex_Type(Integer32):
    """Custom type flComponentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlComponentsIndex_Type.__name__ = "Integer32"
_FlComponentsIndex_Object = MibTableColumn
flComponentsIndex = _FlComponentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 2, 1, 1, 1),
    _FlComponentsIndex_Type()
)
flComponentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flComponentsIndex.setStatus("current")
_FlComponentsName_Type = DisplayString
_FlComponentsName_Object = MibTableColumn
flComponentsName = _FlComponentsName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 2, 1, 1, 2),
    _FlComponentsName_Type()
)
flComponentsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flComponentsName.setStatus("current")
_FlComponentsDescr_Type = DisplayString
_FlComponentsDescr_Object = MibTableColumn
flComponentsDescr = _FlComponentsDescr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 2, 1, 1, 3),
    _FlComponentsDescr_Type()
)
flComponentsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flComponentsDescr.setStatus("current")
_FlComponentsURL_Type = DisplayString
_FlComponentsURL_Object = MibTableColumn
flComponentsURL = _FlComponentsURL_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 2, 1, 1, 4),
    _FlComponentsURL_Type()
)
flComponentsURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flComponentsURL.setStatus("current")
_FlComponentsOrderNumber_Type = DisplayString
_FlComponentsOrderNumber_Object = MibTableColumn
flComponentsOrderNumber = _FlComponentsOrderNumber_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 1, 2, 1, 1, 5),
    _FlComponentsOrderNumber_Type()
)
flComponentsOrderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flComponentsOrderNumber.setStatus("current")
_FlWorkDevice_ObjectIdentity = ObjectIdentity
flWorkDevice = _FlWorkDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11)
)
_FlWorkBasic_ObjectIdentity = ObjectIdentity
flWorkBasic = _FlWorkBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1)
)
_FlWorkBasicName_Type = DisplayString
_FlWorkBasicName_Object = MibScalar
flWorkBasicName = _FlWorkBasicName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 1),
    _FlWorkBasicName_Type()
)
flWorkBasicName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkBasicName.setStatus("current")
_FlWorkBasicDescr_Type = DisplayString
_FlWorkBasicDescr_Object = MibScalar
flWorkBasicDescr = _FlWorkBasicDescr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 2),
    _FlWorkBasicDescr_Type()
)
flWorkBasicDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkBasicDescr.setStatus("current")
_FlWorkBasicURL_Type = DisplayString
_FlWorkBasicURL_Object = MibScalar
flWorkBasicURL = _FlWorkBasicURL_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 3),
    _FlWorkBasicURL_Type()
)
flWorkBasicURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicURL.setStatus("current")


class _FlWorkBasicSerialNumber_Type(OctetString):
    """Custom type flWorkBasicSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_FlWorkBasicSerialNumber_Type.__name__ = "OctetString"
_FlWorkBasicSerialNumber_Object = MibScalar
flWorkBasicSerialNumber = _FlWorkBasicSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 4),
    _FlWorkBasicSerialNumber_Type()
)
flWorkBasicSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicSerialNumber.setStatus("current")
_FlWorkBasicHWRevision_Type = OctetString
_FlWorkBasicHWRevision_Object = MibScalar
flWorkBasicHWRevision = _FlWorkBasicHWRevision_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 5),
    _FlWorkBasicHWRevision_Type()
)
flWorkBasicHWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicHWRevision.setStatus("current")


class _FlWorkBasicPowerStat_Type(Integer32):
    """Custom type flWorkBasicPowerStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("sourceOne", 3),
          ("sourceTwo", 4),
          ("sourceBoth", 5))
    )


_FlWorkBasicPowerStat_Type.__name__ = "Integer32"
_FlWorkBasicPowerStat_Object = MibScalar
flWorkBasicPowerStat = _FlWorkBasicPowerStat_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 6),
    _FlWorkBasicPowerStat_Type()
)
flWorkBasicPowerStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicPowerStat.setStatus("current")
_FlWorkBasicSystemBusRevision_Type = OctetString
_FlWorkBasicSystemBusRevision_Object = MibScalar
flWorkBasicSystemBusRevision = _FlWorkBasicSystemBusRevision_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 7),
    _FlWorkBasicSystemBusRevision_Type()
)
flWorkBasicSystemBusRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicSystemBusRevision.setStatus("current")


class _FlWorkBasicCompMaxCapacity_Type(Integer32):
    """Custom type flWorkBasicCompMaxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkBasicCompMaxCapacity_Type.__name__ = "Integer32"
_FlWorkBasicCompMaxCapacity_Object = MibScalar
flWorkBasicCompMaxCapacity = _FlWorkBasicCompMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 11),
    _FlWorkBasicCompMaxCapacity_Type()
)
flWorkBasicCompMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicCompMaxCapacity.setStatus("current")


class _FlWorkBasicCompCapacity_Type(Integer32):
    """Custom type flWorkBasicCompCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkBasicCompCapacity_Type.__name__ = "Integer32"
_FlWorkBasicCompCapacity_Object = MibScalar
flWorkBasicCompCapacity = _FlWorkBasicCompCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 12),
    _FlWorkBasicCompCapacity_Type()
)
flWorkBasicCompCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicCompCapacity.setStatus("current")


class _FlWorkBasicLogicRevision_Type(OctetString):
    """Custom type flWorkBasicLogicRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_FlWorkBasicLogicRevision_Type.__name__ = "OctetString"
_FlWorkBasicLogicRevision_Object = MibScalar
flWorkBasicLogicRevision = _FlWorkBasicLogicRevision_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 13),
    _FlWorkBasicLogicRevision_Type()
)
flWorkBasicLogicRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicLogicRevision.setStatus("current")


class _FlWorkBasicPlatformID_Type(OctetString):
    """Custom type flWorkBasicPlatformID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_FlWorkBasicPlatformID_Type.__name__ = "OctetString"
_FlWorkBasicPlatformID_Object = MibScalar
flWorkBasicPlatformID = _FlWorkBasicPlatformID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 14),
    _FlWorkBasicPlatformID_Type()
)
flWorkBasicPlatformID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicPlatformID.setStatus("current")


class _FlWorkBasicFwGeneration_Type(OctetString):
    """Custom type flWorkBasicFwGeneration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_FlWorkBasicFwGeneration_Type.__name__ = "OctetString"
_FlWorkBasicFwGeneration_Object = MibScalar
flWorkBasicFwGeneration = _FlWorkBasicFwGeneration_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 15),
    _FlWorkBasicFwGeneration_Type()
)
flWorkBasicFwGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicFwGeneration.setStatus("current")


class _FlWorkBasicCfGeneration_Type(OctetString):
    """Custom type flWorkBasicCfGeneration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_FlWorkBasicCfGeneration_Type.__name__ = "OctetString"
_FlWorkBasicCfGeneration_Object = MibScalar
flWorkBasicCfGeneration = _FlWorkBasicCfGeneration_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 16),
    _FlWorkBasicCfGeneration_Type()
)
flWorkBasicCfGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicCfGeneration.setStatus("current")
_FlWorkBasicPortTable_Object = MibTable
flWorkBasicPortTable = _FlWorkBasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 17)
)
if mibBuilder.loadTexts:
    flWorkBasicPortTable.setStatus("current")
_FlWorkBasicPortEntry_Object = MibTableRow
flWorkBasicPortEntry = _FlWorkBasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 17, 1)
)
flWorkBasicPortEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkBasicPortIdx"),
)
if mibBuilder.loadTexts:
    flWorkBasicPortEntry.setStatus("current")


class _FlWorkBasicPortIdx_Type(Integer32):
    """Custom type flWorkBasicPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkBasicPortIdx_Type.__name__ = "Integer32"
_FlWorkBasicPortIdx_Object = MibTableColumn
flWorkBasicPortIdx = _FlWorkBasicPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 17, 1, 1),
    _FlWorkBasicPortIdx_Type()
)
flWorkBasicPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicPortIdx.setStatus("current")
_FlWorkBasicPortService_Type = OctetString
_FlWorkBasicPortService_Object = MibTableColumn
flWorkBasicPortService = _FlWorkBasicPortService_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 17, 1, 2),
    _FlWorkBasicPortService_Type()
)
flWorkBasicPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicPortService.setStatus("current")
_FlWorkBasicPortProtocol_Type = OctetString
_FlWorkBasicPortProtocol_Object = MibTableColumn
flWorkBasicPortProtocol = _FlWorkBasicPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 17, 1, 3),
    _FlWorkBasicPortProtocol_Type()
)
flWorkBasicPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicPortProtocol.setStatus("current")
_FlWorkBasicPortTransport_Type = OctetString
_FlWorkBasicPortTransport_Object = MibTableColumn
flWorkBasicPortTransport = _FlWorkBasicPortTransport_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 17, 1, 4),
    _FlWorkBasicPortTransport_Type()
)
flWorkBasicPortTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicPortTransport.setStatus("current")
_FlWorkBasicPort_Type = Integer32
_FlWorkBasicPort_Object = MibTableColumn
flWorkBasicPort = _FlWorkBasicPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 1, 17, 1, 5),
    _FlWorkBasicPort_Type()
)
flWorkBasicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkBasicPort.setStatus("current")
_FlWorkComponents_ObjectIdentity = ObjectIdentity
flWorkComponents = _FlWorkComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 2)
)
_FlWorkComponentsTable_Object = MibTable
flWorkComponentsTable = _FlWorkComponentsTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 2, 1)
)
if mibBuilder.loadTexts:
    flWorkComponentsTable.setStatus("current")
_FlWorkComponentsEntry_Object = MibTableRow
flWorkComponentsEntry = _FlWorkComponentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 2, 1, 1)
)
flWorkComponentsEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkComponentsIndex"),
)
if mibBuilder.loadTexts:
    flWorkComponentsEntry.setStatus("current")


class _FlWorkComponentsIndex_Type(Integer32):
    """Custom type flWorkComponentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkComponentsIndex_Type.__name__ = "Integer32"
_FlWorkComponentsIndex_Object = MibTableColumn
flWorkComponentsIndex = _FlWorkComponentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 2, 1, 1, 1),
    _FlWorkComponentsIndex_Type()
)
flWorkComponentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkComponentsIndex.setStatus("current")
_FlWorkComponentsOID_Type = ObjectIdentifier
_FlWorkComponentsOID_Object = MibTableColumn
flWorkComponentsOID = _FlWorkComponentsOID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 2, 1, 1, 2),
    _FlWorkComponentsOID_Type()
)
flWorkComponentsOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkComponentsOID.setStatus("current")
_FlWorkComponentsURL_Type = DisplayString
_FlWorkComponentsURL_Object = MibTableColumn
flWorkComponentsURL = _FlWorkComponentsURL_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 2, 1, 1, 3),
    _FlWorkComponentsURL_Type()
)
flWorkComponentsURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkComponentsURL.setStatus("current")


class _FlWorkComponentsDevSign_Type(Integer32):
    """Custom type flWorkComponentsDevSign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkComponentsDevSign_Type.__name__ = "Integer32"
_FlWorkComponentsDevSign_Object = MibTableColumn
flWorkComponentsDevSign = _FlWorkComponentsDevSign_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 2, 1, 1, 4),
    _FlWorkComponentsDevSign_Type()
)
flWorkComponentsDevSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkComponentsDevSign.setStatus("current")
_FlWorkTraps_ObjectIdentity = ObjectIdentity
flWorkTraps = _FlWorkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3)
)
_FlWorkTrapsDelemeter_ObjectIdentity = ObjectIdentity
flWorkTrapsDelemeter = _FlWorkTrapsDelemeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0)
)
_FlWorkNet_ObjectIdentity = ObjectIdentity
flWorkNet = _FlWorkNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4)
)
_FlWorkNetIfParameter_ObjectIdentity = ObjectIdentity
flWorkNetIfParameter = _FlWorkNetIfParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1)
)
_FlWorkNetIfParamPhyAddress_Type = MacAddress
_FlWorkNetIfParamPhyAddress_Object = MibScalar
flWorkNetIfParamPhyAddress = _FlWorkNetIfParamPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 1),
    _FlWorkNetIfParamPhyAddress_Type()
)
flWorkNetIfParamPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetIfParamPhyAddress.setStatus("current")
_FlWorkNetIfParamIpAddress_Type = IpAddress
_FlWorkNetIfParamIpAddress_Object = MibScalar
flWorkNetIfParamIpAddress = _FlWorkNetIfParamIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 2),
    _FlWorkNetIfParamIpAddress_Type()
)
flWorkNetIfParamIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfParamIpAddress.setStatus("current")
_FlWorkNetIfParamSubnetmask_Type = IpAddress
_FlWorkNetIfParamSubnetmask_Object = MibScalar
flWorkNetIfParamSubnetmask = _FlWorkNetIfParamSubnetmask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 3),
    _FlWorkNetIfParamSubnetmask_Type()
)
flWorkNetIfParamSubnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfParamSubnetmask.setStatus("current")
_FlWorkNetIfParamGwIpAddress_Type = IpAddress
_FlWorkNetIfParamGwIpAddress_Object = MibScalar
flWorkNetIfParamGwIpAddress = _FlWorkNetIfParamGwIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 4),
    _FlWorkNetIfParamGwIpAddress_Type()
)
flWorkNetIfParamGwIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfParamGwIpAddress.setStatus("current")


class _FlWorkNetIfParamStatus_Type(Integer32):
    """Custom type flWorkNetIfParamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notModified", 1),
          ("modified", 2))
    )


_FlWorkNetIfParamStatus_Type.__name__ = "Integer32"
_FlWorkNetIfParamStatus_Object = MibScalar
flWorkNetIfParamStatus = _FlWorkNetIfParamStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 5),
    _FlWorkNetIfParamStatus_Type()
)
flWorkNetIfParamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetIfParamStatus.setStatus("current")


class _FlWorkNetIfParamSave_Type(Integer32):
    """Custom type flWorkNetIfParamSave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restore", 1),
          ("apply", 2))
    )


_FlWorkNetIfParamSave_Type.__name__ = "Integer32"
_FlWorkNetIfParamSave_Object = MibScalar
flWorkNetIfParamSave = _FlWorkNetIfParamSave_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 6),
    _FlWorkNetIfParamSave_Type()
)
flWorkNetIfParamSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfParamSave.setStatus("current")


class _FlWorkNetIfParamAssignment_Type(Integer32):
    """Custom type flWorkNetIfParamAssignment based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("bootp", 2),
          ("dhcp", 3),
          ("dcp", 4),
          ("topology", 6))
    )


_FlWorkNetIfParamAssignment_Type.__name__ = "Integer32"
_FlWorkNetIfParamAssignment_Object = MibScalar
flWorkNetIfParamAssignment = _FlWorkNetIfParamAssignment_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 7),
    _FlWorkNetIfParamAssignment_Type()
)
flWorkNetIfParamAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfParamAssignment.setStatus("current")


class _FlWorkNetIfParamManagementVlanId_Type(Integer32):
    """Custom type flWorkNetIfParamManagementVlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FlWorkNetIfParamManagementVlanId_Type.__name__ = "Integer32"
_FlWorkNetIfParamManagementVlanId_Object = MibScalar
flWorkNetIfParamManagementVlanId = _FlWorkNetIfParamManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 8),
    _FlWorkNetIfParamManagementVlanId_Type()
)
flWorkNetIfParamManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfParamManagementVlanId.setStatus("current")


class _FlWorkNetIfParamConflictDetection_Type(Integer32):
    """Custom type flWorkNetIfParamConflictDetection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("acd", 2))
    )


_FlWorkNetIfParamConflictDetection_Type.__name__ = "Integer32"
_FlWorkNetIfParamConflictDetection_Object = MibScalar
flWorkNetIfParamConflictDetection = _FlWorkNetIfParamConflictDetection_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 9),
    _FlWorkNetIfParamConflictDetection_Type()
)
flWorkNetIfParamConflictDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfParamConflictDetection.setStatus("current")
_FlWorkNetIfParamDnsServerTable_Object = MibTable
flWorkNetIfParamDnsServerTable = _FlWorkNetIfParamDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 10)
)
if mibBuilder.loadTexts:
    flWorkNetIfParamDnsServerTable.setStatus("current")
_FlWorkNetIfParamDnsServerEntry_Object = MibTableRow
flWorkNetIfParamDnsServerEntry = _FlWorkNetIfParamDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 10, 1)
)
flWorkNetIfParamDnsServerEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkNetIfParamDnsServerIndex"),
)
if mibBuilder.loadTexts:
    flWorkNetIfParamDnsServerEntry.setStatus("current")


class _FlWorkNetIfParamDnsServerIndex_Type(Integer32):
    """Custom type flWorkNetIfParamDnsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkNetIfParamDnsServerIndex_Type.__name__ = "Integer32"
_FlWorkNetIfParamDnsServerIndex_Object = MibTableColumn
flWorkNetIfParamDnsServerIndex = _FlWorkNetIfParamDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 10, 1, 1),
    _FlWorkNetIfParamDnsServerIndex_Type()
)
flWorkNetIfParamDnsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetIfParamDnsServerIndex.setStatus("current")
_FlWorkNetIfParamDnsServerIPAddr_Type = IpAddress
_FlWorkNetIfParamDnsServerIPAddr_Object = MibTableColumn
flWorkNetIfParamDnsServerIPAddr = _FlWorkNetIfParamDnsServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 1, 10, 1, 2),
    _FlWorkNetIfParamDnsServerIPAddr_Type()
)
flWorkNetIfParamDnsServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfParamDnsServerIPAddr.setStatus("current")
_FlWorkNetPort_ObjectIdentity = ObjectIdentity
flWorkNetPort = _FlWorkNetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2)
)


class _FlWorkNetPortCapacity_Type(Integer32):
    """Custom type flWorkNetPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkNetPortCapacity_Type.__name__ = "Integer32"
_FlWorkNetPortCapacity_Object = MibScalar
flWorkNetPortCapacity = _FlWorkNetPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 1),
    _FlWorkNetPortCapacity_Type()
)
flWorkNetPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortCapacity.setStatus("current")
_FlWorkNetPortTable_Object = MibTable
flWorkNetPortTable = _FlWorkNetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2)
)
if mibBuilder.loadTexts:
    flWorkNetPortTable.setStatus("current")
_FlWorkNetPortEntry_Object = MibTableRow
flWorkNetPortEntry = _FlWorkNetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1)
)
flWorkNetPortEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkNetPortIndex"),
)
if mibBuilder.loadTexts:
    flWorkNetPortEntry.setStatus("current")


class _FlWorkNetPortIndex_Type(Integer32):
    """Custom type flWorkNetPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkNetPortIndex_Type.__name__ = "Integer32"
_FlWorkNetPortIndex_Object = MibTableColumn
flWorkNetPortIndex = _FlWorkNetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 1),
    _FlWorkNetPortIndex_Type()
)
flWorkNetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortIndex.setStatus("current")


class _FlWorkNetPortLinkState_Type(Integer32):
    """Custom type flWorkNetPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2),
          ("farEndFault", 3))
    )


_FlWorkNetPortLinkState_Type.__name__ = "Integer32"
_FlWorkNetPortLinkState_Object = MibTableColumn
flWorkNetPortLinkState = _FlWorkNetPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 2),
    _FlWorkNetPortLinkState_Type()
)
flWorkNetPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortLinkState.setStatus("current")
_FlWorkNetPortSpeed_Type = Gauge32
_FlWorkNetPortSpeed_Object = MibTableColumn
flWorkNetPortSpeed = _FlWorkNetPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 3),
    _FlWorkNetPortSpeed_Type()
)
flWorkNetPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortSpeed.setStatus("current")


class _FlWorkNetPortDuplexMode_Type(Integer32):
    """Custom type flWorkNetPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noLink", 0),
          ("full", 1),
          ("half", 2))
    )


_FlWorkNetPortDuplexMode_Type.__name__ = "Integer32"
_FlWorkNetPortDuplexMode_Object = MibTableColumn
flWorkNetPortDuplexMode = _FlWorkNetPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 4),
    _FlWorkNetPortDuplexMode_Type()
)
flWorkNetPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortDuplexMode.setStatus("current")


class _FlWorkNetPortNegotiation_Type(Integer32):
    """Custom type flWorkNetPortNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_FlWorkNetPortNegotiation_Type.__name__ = "Integer32"
_FlWorkNetPortNegotiation_Object = MibTableColumn
flWorkNetPortNegotiation = _FlWorkNetPortNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 5),
    _FlWorkNetPortNegotiation_Type()
)
flWorkNetPortNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortNegotiation.setStatus("current")


class _FlWorkNetPortName_Type(DisplayString):
    """Custom type flWorkNetPortName based on DisplayString"""
    defaultValue = OctetString("Port x")


_FlWorkNetPortName_Type.__name__ = "DisplayString"
_FlWorkNetPortName_Object = MibTableColumn
flWorkNetPortName = _FlWorkNetPortName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 6),
    _FlWorkNetPortName_Type()
)
flWorkNetPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortName.setStatus("current")


class _FlWorkNetPortEnable_Type(Integer32):
    """Custom type flWorkNetPortEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkNetPortEnable_Type.__name__ = "Integer32"
_FlWorkNetPortEnable_Object = MibTableColumn
flWorkNetPortEnable = _FlWorkNetPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 7),
    _FlWorkNetPortEnable_Type()
)
flWorkNetPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortEnable.setStatus("current")


class _FlWorkNetPortLinkMonitoring_Type(Integer32):
    """Custom type flWorkNetPortLinkMonitoring based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkNetPortLinkMonitoring_Type.__name__ = "Integer32"
_FlWorkNetPortLinkMonitoring_Object = MibTableColumn
flWorkNetPortLinkMonitoring = _FlWorkNetPortLinkMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 8),
    _FlWorkNetPortLinkMonitoring_Type()
)
flWorkNetPortLinkMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortLinkMonitoring.setStatus("current")


class _FlWorkNetPortModus_Type(Integer32):
    """Custom type flWorkNetPortModus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("autonegotiation", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("autoneg10-100", 20),
          ("fast-startup", 21))
    )


_FlWorkNetPortModus_Type.__name__ = "Integer32"
_FlWorkNetPortModus_Object = MibTableColumn
flWorkNetPortModus = _FlWorkNetPortModus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 9),
    _FlWorkNetPortModus_Type()
)
flWorkNetPortModus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortModus.setStatus("current")


class _FlWorkNetPortSTPEnable_Type(Integer32):
    """Custom type flWorkNetPortSTPEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkNetPortSTPEnable_Type.__name__ = "Integer32"
_FlWorkNetPortSTPEnable_Object = MibTableColumn
flWorkNetPortSTPEnable = _FlWorkNetPortSTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 10),
    _FlWorkNetPortSTPEnable_Type()
)
flWorkNetPortSTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortSTPEnable.setStatus("deprecated")
_FlWorkNetPortIfIndex_Type = Integer32
_FlWorkNetPortIfIndex_Object = MibTableColumn
flWorkNetPortIfIndex = _FlWorkNetPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 11),
    _FlWorkNetPortIfIndex_Type()
)
flWorkNetPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortIfIndex.setStatus("current")


class _FlWorkNetPortLLWHPort_Type(Integer32):
    """Custom type flWorkNetPortLLWHPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8193, 8296),
    )


_FlWorkNetPortLLWHPort_Type.__name__ = "Integer32"
_FlWorkNetPortLLWHPort_Object = MibTableColumn
flWorkNetPortLLWHPort = _FlWorkNetPortLLWHPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 12),
    _FlWorkNetPortLLWHPort_Type()
)
flWorkNetPortLLWHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortLLWHPort.setStatus("current")
_FlWorkNetPortType_Type = DisplayString
_FlWorkNetPortType_Object = MibTableColumn
flWorkNetPortType = _FlWorkNetPortType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 13),
    _FlWorkNetPortType_Type()
)
flWorkNetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortType.setStatus("current")
_FlWorkNetPortModuleName_Type = DisplayString
_FlWorkNetPortModuleName_Object = MibTableColumn
flWorkNetPortModuleName = _FlWorkNetPortModuleName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 14),
    _FlWorkNetPortModuleName_Type()
)
flWorkNetPortModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortModuleName.setStatus("current")
_FlWorkNetPortInterfaceName_Type = DisplayString
_FlWorkNetPortInterfaceName_Object = MibTableColumn
flWorkNetPortInterfaceName = _FlWorkNetPortInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 15),
    _FlWorkNetPortInterfaceName_Type()
)
flWorkNetPortInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortInterfaceName.setStatus("current")


class _FlWorkNetPortPriorityLevel_Type(Integer32):
    """Custom type flWorkNetPortPriorityLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FlWorkNetPortPriorityLevel_Type.__name__ = "Integer32"
_FlWorkNetPortPriorityLevel_Object = MibTableColumn
flWorkNetPortPriorityLevel = _FlWorkNetPortPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 16),
    _FlWorkNetPortPriorityLevel_Type()
)
flWorkNetPortPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortPriorityLevel.setStatus("current")


class _FlWorkNetPortPofTransmittingPower_Type(Integer32):
    """Custom type flWorkNetPortPofTransmittingPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("low", 2),
          ("normal", 3))
    )


_FlWorkNetPortPofTransmittingPower_Type.__name__ = "Integer32"
_FlWorkNetPortPofTransmittingPower_Object = MibTableColumn
flWorkNetPortPofTransmittingPower = _FlWorkNetPortPofTransmittingPower_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 17),
    _FlWorkNetPortPofTransmittingPower_Type()
)
flWorkNetPortPofTransmittingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofTransmittingPower.setStatus("current")


class _FlWorkNetPortStpMode_Type(Integer32):
    """Custom type flWorkNetPortStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("rstp", 2),
          ("none", 3))
    )


_FlWorkNetPortStpMode_Type.__name__ = "Integer32"
_FlWorkNetPortStpMode_Object = MibTableColumn
flWorkNetPortStpMode = _FlWorkNetPortStpMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 18),
    _FlWorkNetPortStpMode_Type()
)
flWorkNetPortStpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortStpMode.setStatus("current")


class _FlWorkNetPortFlowControl_Type(Integer32):
    """Custom type flWorkNetPortFlowControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkNetPortFlowControl_Type.__name__ = "Integer32"
_FlWorkNetPortFlowControl_Object = MibTableColumn
flWorkNetPortFlowControl = _FlWorkNetPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 20),
    _FlWorkNetPortFlowControl_Type()
)
flWorkNetPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortFlowControl.setStatus("current")
_FlWorkNetPortMaxFrameSize_Type = Integer32
_FlWorkNetPortMaxFrameSize_Object = MibTableColumn
flWorkNetPortMaxFrameSize = _FlWorkNetPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 21),
    _FlWorkNetPortMaxFrameSize_Type()
)
flWorkNetPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortMaxFrameSize.setStatus("current")


class _FlWorkNetPortJumboFrame_Type(Integer32):
    """Custom type flWorkNetPortJumboFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FlWorkNetPortJumboFrame_Type.__name__ = "Integer32"
_FlWorkNetPortJumboFrame_Object = MibTableColumn
flWorkNetPortJumboFrame = _FlWorkNetPortJumboFrame_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 22),
    _FlWorkNetPortJumboFrame_Type()
)
flWorkNetPortJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortJumboFrame.setStatus("current")
_FlWorkNetPortCableLength_Type = DisplayString
_FlWorkNetPortCableLength_Object = MibTableColumn
flWorkNetPortCableLength = _FlWorkNetPortCableLength_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 23),
    _FlWorkNetPortCableLength_Type()
)
flWorkNetPortCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortCableLength.setStatus("current")
_FlWorkNetPortPHYcompatibility_Type = Integer32
_FlWorkNetPortPHYcompatibility_Object = MibTableColumn
flWorkNetPortPHYcompatibility = _FlWorkNetPortPHYcompatibility_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 2, 1, 24),
    _FlWorkNetPortPHYcompatibility_Type()
)
flWorkNetPortPHYcompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortPHYcompatibility.setStatus("current")
_FlWorkNetPortPoETable_Object = MibTable
flWorkNetPortPoETable = _FlWorkNetPortPoETable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3)
)
if mibBuilder.loadTexts:
    flWorkNetPortPoETable.setStatus("current")
_FlWorkNetPortPoEEntry_Object = MibTableRow
flWorkNetPortPoEEntry = _FlWorkNetPortPoEEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3, 1)
)
flWorkNetPortPoEEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkNetPortPoEIndex"),
)
if mibBuilder.loadTexts:
    flWorkNetPortPoEEntry.setStatus("current")


class _FlWorkNetPortPoEIndex_Type(Integer32):
    """Custom type flWorkNetPortPoEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkNetPortPoEIndex_Type.__name__ = "Integer32"
_FlWorkNetPortPoEIndex_Object = MibTableColumn
flWorkNetPortPoEIndex = _FlWorkNetPortPoEIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3, 1, 1),
    _FlWorkNetPortPoEIndex_Type()
)
flWorkNetPortPoEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPoEIndex.setStatus("current")


class _FlWorkNetPortPoEPowerEnable_Type(Integer32):
    """Custom type flWorkNetPortPoEPowerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 3))
    )


_FlWorkNetPortPoEPowerEnable_Type.__name__ = "Integer32"
_FlWorkNetPortPoEPowerEnable_Object = MibTableColumn
flWorkNetPortPoEPowerEnable = _FlWorkNetPortPoEPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3, 1, 2),
    _FlWorkNetPortPoEPowerEnable_Type()
)
flWorkNetPortPoEPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortPoEPowerEnable.setStatus("current")


class _FlWorkNetPortPoECurrentLimitation_Type(Integer32):
    """Custom type flWorkNetPortPoECurrentLimitation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("unknown", 3))
    )


_FlWorkNetPortPoECurrentLimitation_Type.__name__ = "Integer32"
_FlWorkNetPortPoECurrentLimitation_Object = MibTableColumn
flWorkNetPortPoECurrentLimitation = _FlWorkNetPortPoECurrentLimitation_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3, 1, 3),
    _FlWorkNetPortPoECurrentLimitation_Type()
)
flWorkNetPortPoECurrentLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortPoECurrentLimitation.setStatus("current")


class _FlWorkNetPortPoEDeviceClass_Type(Integer32):
    """Custom type flWorkNetPortPoEDeviceClass based on Integer32"""
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
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("unknown", 5))
    )


_FlWorkNetPortPoEDeviceClass_Type.__name__ = "Integer32"
_FlWorkNetPortPoEDeviceClass_Object = MibTableColumn
flWorkNetPortPoEDeviceClass = _FlWorkNetPortPoEDeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3, 1, 4),
    _FlWorkNetPortPoEDeviceClass_Type()
)
flWorkNetPortPoEDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPoEDeviceClass.setStatus("current")


class _FlWorkNetPortPoEOutputCurrent_Type(Integer32):
    """Custom type flWorkNetPortPoEOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_FlWorkNetPortPoEOutputCurrent_Type.__name__ = "Integer32"
_FlWorkNetPortPoEOutputCurrent_Object = MibTableColumn
flWorkNetPortPoEOutputCurrent = _FlWorkNetPortPoEOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3, 1, 5),
    _FlWorkNetPortPoEOutputCurrent_Type()
)
flWorkNetPortPoEOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPoEOutputCurrent.setStatus("current")


class _FlWorkNetPortPoEOutputVoltage_Type(Integer32):
    """Custom type flWorkNetPortPoEOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45000, 56000),
    )


_FlWorkNetPortPoEOutputVoltage_Type.__name__ = "Integer32"
_FlWorkNetPortPoEOutputVoltage_Object = MibTableColumn
flWorkNetPortPoEOutputVoltage = _FlWorkNetPortPoEOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3, 1, 6),
    _FlWorkNetPortPoEOutputVoltage_Type()
)
flWorkNetPortPoEOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPoEOutputVoltage.setStatus("current")


class _FlWorkNetPortPoEFaultStatus_Type(Integer32):
    """Custom type flWorkNetPortPoEFaultStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noFault", 0),
          ("voltage", 1),
          ("thermal", 2),
          ("overload", 3),
          ("loadDisconnected", 4),
          ("powerSupplyMissing", 5),
          ("noPse", 6),
          ("noPoeSupport", 7),
          ("noPoeDeviceConnected", 8))
    )


_FlWorkNetPortPoEFaultStatus_Type.__name__ = "Integer32"
_FlWorkNetPortPoEFaultStatus_Object = MibTableColumn
flWorkNetPortPoEFaultStatus = _FlWorkNetPortPoEFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3, 1, 7),
    _FlWorkNetPortPoEFaultStatus_Type()
)
flWorkNetPortPoEFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPoEFaultStatus.setStatus("current")


class _FlWorkNetPortPoeFaultMonitoring_Type(Integer32):
    """Custom type flWorkNetPortPoeFaultMonitoring based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkNetPortPoeFaultMonitoring_Type.__name__ = "Integer32"
_FlWorkNetPortPoeFaultMonitoring_Object = MibTableColumn
flWorkNetPortPoeFaultMonitoring = _FlWorkNetPortPoeFaultMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 3, 1, 8),
    _FlWorkNetPortPoeFaultMonitoring_Type()
)
flWorkNetPortPoeFaultMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortPoeFaultMonitoring.setStatus("current")
_FlWorkNetPortPofScrjIfTable_Object = MibTable
flWorkNetPortPofScrjIfTable = _FlWorkNetPortPofScrjIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4)
)
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfTable.setStatus("current")
_FlWorkNetPortPofScrjIfEntry_Object = MibTableRow
flWorkNetPortPofScrjIfEntry = _FlWorkNetPortPofScrjIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1)
)
flWorkNetPortPofScrjIfEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkNetPortPofScrjIfIndex"),
)
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfEntry.setStatus("current")


class _FlWorkNetPortPofScrjIfIndex_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkNetPortPofScrjIfIndex_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfIndex_Object = MibTableColumn
flWorkNetPortPofScrjIfIndex = _FlWorkNetPortPofScrjIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 1),
    _FlWorkNetPortPofScrjIfIndex_Type()
)
flWorkNetPortPofScrjIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfIndex.setStatus("current")


class _FlWorkNetPortPofScrjIfStatus_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfStatus based on Integer32"""
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
        *(("notSupported", 1),
          ("noModule", 2),
          ("ok", 3),
          ("systemReserveLow", 4),
          ("systemReserveExhausted", 5))
    )


_FlWorkNetPortPofScrjIfStatus_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfStatus_Object = MibTableColumn
flWorkNetPortPofScrjIfStatus = _FlWorkNetPortPofScrjIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 2),
    _FlWorkNetPortPofScrjIfStatus_Type()
)
flWorkNetPortPofScrjIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfStatus.setStatus("current")


class _FlWorkNetPortPofScrjIfSupplyVoltage_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfSupplyVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65),
    )


_FlWorkNetPortPofScrjIfSupplyVoltage_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfSupplyVoltage_Object = MibTableColumn
flWorkNetPortPofScrjIfSupplyVoltage = _FlWorkNetPortPofScrjIfSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 4),
    _FlWorkNetPortPofScrjIfSupplyVoltage_Type()
)
flWorkNetPortPofScrjIfSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfSupplyVoltage.setStatus("current")


class _FlWorkNetPortPofScrjIfTxPower_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6553),
    )


_FlWorkNetPortPofScrjIfTxPower_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfTxPower_Object = MibTableColumn
flWorkNetPortPofScrjIfTxPower = _FlWorkNetPortPofScrjIfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 6),
    _FlWorkNetPortPofScrjIfTxPower_Type()
)
flWorkNetPortPofScrjIfTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfTxPower.setStatus("current")


class _FlWorkNetPortPofScrjIfRxPower_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6553),
    )


_FlWorkNetPortPofScrjIfRxPower_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfRxPower_Object = MibTableColumn
flWorkNetPortPofScrjIfRxPower = _FlWorkNetPortPofScrjIfRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 7),
    _FlWorkNetPortPofScrjIfRxPower_Type()
)
flWorkNetPortPofScrjIfRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfRxPower.setStatus("current")


class _FlWorkNetPortPofScrjIfSystemReserve_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfSystemReserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkNetPortPofScrjIfSystemReserve_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfSystemReserve_Object = MibTableColumn
flWorkNetPortPofScrjIfSystemReserve = _FlWorkNetPortPofScrjIfSystemReserve_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 8),
    _FlWorkNetPortPofScrjIfSystemReserve_Type()
)
flWorkNetPortPofScrjIfSystemReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfSystemReserve.setStatus("current")


class _FlWorkNetPortPofScrjIfRxPowerHighAlarm_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfRxPowerHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_FlWorkNetPortPofScrjIfRxPowerHighAlarm_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfRxPowerHighAlarm_Object = MibTableColumn
flWorkNetPortPofScrjIfRxPowerHighAlarm = _FlWorkNetPortPofScrjIfRxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 9),
    _FlWorkNetPortPofScrjIfRxPowerHighAlarm_Type()
)
flWorkNetPortPofScrjIfRxPowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfRxPowerHighAlarm.setStatus("current")


class _FlWorkNetPortPofScrjIfRxPowerLowAlarm_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfRxPowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_FlWorkNetPortPofScrjIfRxPowerLowAlarm_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfRxPowerLowAlarm_Object = MibTableColumn
flWorkNetPortPofScrjIfRxPowerLowAlarm = _FlWorkNetPortPofScrjIfRxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 10),
    _FlWorkNetPortPofScrjIfRxPowerLowAlarm_Type()
)
flWorkNetPortPofScrjIfRxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfRxPowerLowAlarm.setStatus("current")


class _FlWorkNetPortPofScrjIfRxPowerHighWarning_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfRxPowerHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_FlWorkNetPortPofScrjIfRxPowerHighWarning_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfRxPowerHighWarning_Object = MibTableColumn
flWorkNetPortPofScrjIfRxPowerHighWarning = _FlWorkNetPortPofScrjIfRxPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 11),
    _FlWorkNetPortPofScrjIfRxPowerHighWarning_Type()
)
flWorkNetPortPofScrjIfRxPowerHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfRxPowerHighWarning.setStatus("current")


class _FlWorkNetPortPofScrjIfRxPowerLowWarning_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfRxPowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_FlWorkNetPortPofScrjIfRxPowerLowWarning_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfRxPowerLowWarning_Object = MibTableColumn
flWorkNetPortPofScrjIfRxPowerLowWarning = _FlWorkNetPortPofScrjIfRxPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 12),
    _FlWorkNetPortPofScrjIfRxPowerLowWarning_Type()
)
flWorkNetPortPofScrjIfRxPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfRxPowerLowWarning.setStatus("current")
_FlWorkNetPortPofScrjIfManufacturer_Type = OctetString
_FlWorkNetPortPofScrjIfManufacturer_Object = MibTableColumn
flWorkNetPortPofScrjIfManufacturer = _FlWorkNetPortPofScrjIfManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 13),
    _FlWorkNetPortPofScrjIfManufacturer_Type()
)
flWorkNetPortPofScrjIfManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfManufacturer.setStatus("current")
_FlWorkNetPortPofScrjIfManufactOui_Type = OctetString
_FlWorkNetPortPofScrjIfManufactOui_Object = MibTableColumn
flWorkNetPortPofScrjIfManufactOui = _FlWorkNetPortPofScrjIfManufactOui_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 14),
    _FlWorkNetPortPofScrjIfManufactOui_Type()
)
flWorkNetPortPofScrjIfManufactOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfManufactOui.setStatus("current")
_FlWorkNetPortPofScrjIfRevision_Type = OctetString
_FlWorkNetPortPofScrjIfRevision_Object = MibTableColumn
flWorkNetPortPofScrjIfRevision = _FlWorkNetPortPofScrjIfRevision_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 16),
    _FlWorkNetPortPofScrjIfRevision_Type()
)
flWorkNetPortPofScrjIfRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfRevision.setStatus("current")
_FlWorkNetPortPofScrjIfWavelength_Type = Integer32
_FlWorkNetPortPofScrjIfWavelength_Object = MibTableColumn
flWorkNetPortPofScrjIfWavelength = _FlWorkNetPortPofScrjIfWavelength_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 17),
    _FlWorkNetPortPofScrjIfWavelength_Type()
)
flWorkNetPortPofScrjIfWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfWavelength.setStatus("current")
_FlWorkNetPortPofScrjIfTransceiverOptions_Type = Integer32
_FlWorkNetPortPofScrjIfTransceiverOptions_Object = MibTableColumn
flWorkNetPortPofScrjIfTransceiverOptions = _FlWorkNetPortPofScrjIfTransceiverOptions_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 18),
    _FlWorkNetPortPofScrjIfTransceiverOptions_Type()
)
flWorkNetPortPofScrjIfTransceiverOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfTransceiverOptions.setStatus("current")
_FlWorkNetPortPofScrjIfSerialNumber_Type = OctetString
_FlWorkNetPortPofScrjIfSerialNumber_Object = MibTableColumn
flWorkNetPortPofScrjIfSerialNumber = _FlWorkNetPortPofScrjIfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 19),
    _FlWorkNetPortPofScrjIfSerialNumber_Type()
)
flWorkNetPortPofScrjIfSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfSerialNumber.setStatus("current")
_FlWorkNetPortPofScrjIfDatecodeAndLot_Type = OctetString
_FlWorkNetPortPofScrjIfDatecodeAndLot_Object = MibTableColumn
flWorkNetPortPofScrjIfDatecodeAndLot = _FlWorkNetPortPofScrjIfDatecodeAndLot_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 20),
    _FlWorkNetPortPofScrjIfDatecodeAndLot_Type()
)
flWorkNetPortPofScrjIfDatecodeAndLot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfDatecodeAndLot.setStatus("current")


class _FlWorkNetPortPofScrjIfAlarmContactEnable_Type(Integer32):
    """Custom type flWorkNetPortPofScrjIfAlarmContactEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkNetPortPofScrjIfAlarmContactEnable_Type.__name__ = "Integer32"
_FlWorkNetPortPofScrjIfAlarmContactEnable_Object = MibTableColumn
flWorkNetPortPofScrjIfAlarmContactEnable = _FlWorkNetPortPofScrjIfAlarmContactEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 4, 1, 21),
    _FlWorkNetPortPofScrjIfAlarmContactEnable_Type()
)
flWorkNetPortPofScrjIfAlarmContactEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetPortPofScrjIfAlarmContactEnable.setStatus("current")
_FlWorkNetSFPModuleTable_Object = MibTable
flWorkNetSFPModuleTable = _FlWorkNetSFPModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5)
)
if mibBuilder.loadTexts:
    flWorkNetSFPModuleTable.setStatus("current")
_FlWorkNetSFPModuleEntry_Object = MibTableRow
flWorkNetSFPModuleEntry = _FlWorkNetSFPModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1)
)
flWorkNetSFPModuleEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkNetSFPModuleIndex"),
)
if mibBuilder.loadTexts:
    flWorkNetSFPModuleEntry.setStatus("current")


class _FlWorkNetSFPModuleIndex_Type(Integer32):
    """Custom type flWorkNetSFPModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkNetSFPModuleIndex_Type.__name__ = "Integer32"
_FlWorkNetSFPModuleIndex_Object = MibTableColumn
flWorkNetSFPModuleIndex = _FlWorkNetSFPModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 1),
    _FlWorkNetSFPModuleIndex_Type()
)
flWorkNetSFPModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleIndex.setStatus("current")


class _FlWorkNetSFPModuleType_Type(Integer32):
    """Custom type flWorkNetSFPModuleType based on Integer32"""
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
        *(("unknown", 1),
          ("eth-1000BASE-SX", 2),
          ("eth-1000BASE-LX", 3),
          ("eth-1000BASE-LH", 4),
          ("eth-1000BASE-CX", 5),
          ("eth-1000BASE-T", 6))
    )


_FlWorkNetSFPModuleType_Type.__name__ = "Integer32"
_FlWorkNetSFPModuleType_Object = MibTableColumn
flWorkNetSFPModuleType = _FlWorkNetSFPModuleType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 2),
    _FlWorkNetSFPModuleType_Type()
)
flWorkNetSFPModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleType.setStatus("current")


class _FlWorkNetSFPModuleMedia_Type(Integer32):
    """Custom type flWorkNetSFPModuleMedia based on Integer32"""
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
        *(("unknown", 1),
          ("single-Mode", 2),
          ("multi-Mode", 3),
          ("multi-Mode-50um", 4),
          ("multi-Mode-62um", 5),
          ("twisted-Pair", 6))
    )


_FlWorkNetSFPModuleMedia_Type.__name__ = "Integer32"
_FlWorkNetSFPModuleMedia_Object = MibTableColumn
flWorkNetSFPModuleMedia = _FlWorkNetSFPModuleMedia_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 3),
    _FlWorkNetSFPModuleMedia_Type()
)
flWorkNetSFPModuleMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleMedia.setStatus("current")
_FlWorkNetSFPModuleVendor_Type = DisplayString
_FlWorkNetSFPModuleVendor_Object = MibTableColumn
flWorkNetSFPModuleVendor = _FlWorkNetSFPModuleVendor_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 4),
    _FlWorkNetSFPModuleVendor_Type()
)
flWorkNetSFPModuleVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleVendor.setStatus("current")
_FlWorkNetSFPModulePartNo_Type = DisplayString
_FlWorkNetSFPModulePartNo_Object = MibTableColumn
flWorkNetSFPModulePartNo = _FlWorkNetSFPModulePartNo_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 5),
    _FlWorkNetSFPModulePartNo_Type()
)
flWorkNetSFPModulePartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModulePartNo.setStatus("current")
_FlWorkNetSFPModuleSerialNo_Type = DisplayString
_FlWorkNetSFPModuleSerialNo_Object = MibTableColumn
flWorkNetSFPModuleSerialNo = _FlWorkNetSFPModuleSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 6),
    _FlWorkNetSFPModuleSerialNo_Type()
)
flWorkNetSFPModuleSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleSerialNo.setStatus("current")
_FlWorkNetSFPModuleRev_Type = DisplayString
_FlWorkNetSFPModuleRev_Object = MibTableColumn
flWorkNetSFPModuleRev = _FlWorkNetSFPModuleRev_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 7),
    _FlWorkNetSFPModuleRev_Type()
)
flWorkNetSFPModuleRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleRev.setStatus("current")
_FlWorkNetSFPModuleLinkLength_Type = Integer32
_FlWorkNetSFPModuleLinkLength_Object = MibTableColumn
flWorkNetSFPModuleLinkLength = _FlWorkNetSFPModuleLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 8),
    _FlWorkNetSFPModuleLinkLength_Type()
)
flWorkNetSFPModuleLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleLinkLength.setStatus("current")
_FlWorkNetSFPModuleBitrate_Type = Integer32
_FlWorkNetSFPModuleBitrate_Object = MibTableColumn
flWorkNetSFPModuleBitrate = _FlWorkNetSFPModuleBitrate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 9),
    _FlWorkNetSFPModuleBitrate_Type()
)
flWorkNetSFPModuleBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleBitrate.setStatus("current")
_FlWorkNetSFPModuleTransceiverCode_Type = DisplayString
_FlWorkNetSFPModuleTransceiverCode_Object = MibTableColumn
flWorkNetSFPModuleTransceiverCode = _FlWorkNetSFPModuleTransceiverCode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 10),
    _FlWorkNetSFPModuleTransceiverCode_Type()
)
flWorkNetSFPModuleTransceiverCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleTransceiverCode.setStatus("current")


class _FlWorkNetSFPModuleEncoding_Type(Integer32):
    """Custom type flWorkNetSFPModuleEncoding based on Integer32"""
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
        *(("unknown", 1),
          ("cod-8B10B", 2),
          ("cod-4B5B", 3),
          ("cod-NRZ", 4),
          ("cod-Manchester", 5))
    )


_FlWorkNetSFPModuleEncoding_Type.__name__ = "Integer32"
_FlWorkNetSFPModuleEncoding_Object = MibTableColumn
flWorkNetSFPModuleEncoding = _FlWorkNetSFPModuleEncoding_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 11),
    _FlWorkNetSFPModuleEncoding_Type()
)
flWorkNetSFPModuleEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPModuleEncoding.setStatus("current")
_FlWorkNetSFPPortTxPower_Type = Integer32
_FlWorkNetSFPPortTxPower_Object = MibTableColumn
flWorkNetSFPPortTxPower = _FlWorkNetSFPPortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 12),
    _FlWorkNetSFPPortTxPower_Type()
)
flWorkNetSFPPortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPPortTxPower.setStatus("current")
_FlWorkNetSFPPortRxPower_Type = Integer32
_FlWorkNetSFPPortRxPower_Object = MibTableColumn
flWorkNetSFPPortRxPower = _FlWorkNetSFPPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 2, 5, 1, 13),
    _FlWorkNetSFPPortRxPower_Type()
)
flWorkNetSFPPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetSFPPortRxPower.setStatus("current")
_FlWorkNetIfList_ObjectIdentity = ObjectIdentity
flWorkNetIfList = _FlWorkNetIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3)
)
_FlWorkNetIfTable_Object = MibTable
flWorkNetIfTable = _FlWorkNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1)
)
if mibBuilder.loadTexts:
    flWorkNetIfTable.setStatus("current")
_FlWorkNetIfEntry_Object = MibTableRow
flWorkNetIfEntry = _FlWorkNetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1, 1)
)
flWorkNetIfEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flComponentsIndex"),
)
if mibBuilder.loadTexts:
    flWorkNetIfEntry.setStatus("current")
_FlWorkNetIfPhyAddress_Type = MacAddress
_FlWorkNetIfPhyAddress_Object = MibTableColumn
flWorkNetIfPhyAddress = _FlWorkNetIfPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1, 1, 1),
    _FlWorkNetIfPhyAddress_Type()
)
flWorkNetIfPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetIfPhyAddress.setStatus("current")
_FlWorkNetIfIpAddress_Type = IpAddress
_FlWorkNetIfIpAddress_Object = MibTableColumn
flWorkNetIfIpAddress = _FlWorkNetIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1, 1, 2),
    _FlWorkNetIfIpAddress_Type()
)
flWorkNetIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfIpAddress.setStatus("current")
_FlWorkNetIfSubnetmask_Type = IpAddress
_FlWorkNetIfSubnetmask_Object = MibTableColumn
flWorkNetIfSubnetmask = _FlWorkNetIfSubnetmask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1, 1, 3),
    _FlWorkNetIfSubnetmask_Type()
)
flWorkNetIfSubnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfSubnetmask.setStatus("current")
_FlWorkNetIfGwIpAddress_Type = IpAddress
_FlWorkNetIfGwIpAddress_Object = MibTableColumn
flWorkNetIfGwIpAddress = _FlWorkNetIfGwIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1, 1, 4),
    _FlWorkNetIfGwIpAddress_Type()
)
flWorkNetIfGwIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfGwIpAddress.setStatus("current")


class _FlWorkNetIfStatus_Type(Integer32):
    """Custom type flWorkNetIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notModified", 1),
          ("modified", 2))
    )


_FlWorkNetIfStatus_Type.__name__ = "Integer32"
_FlWorkNetIfStatus_Object = MibTableColumn
flWorkNetIfStatus = _FlWorkNetIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1, 1, 5),
    _FlWorkNetIfStatus_Type()
)
flWorkNetIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetIfStatus.setStatus("current")


class _FlWorkNetIfSave_Type(Integer32):
    """Custom type flWorkNetIfSave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restore", 1),
          ("apply", 2))
    )


_FlWorkNetIfSave_Type.__name__ = "Integer32"
_FlWorkNetIfSave_Object = MibTableColumn
flWorkNetIfSave = _FlWorkNetIfSave_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1, 1, 6),
    _FlWorkNetIfSave_Type()
)
flWorkNetIfSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfSave.setStatus("current")


class _FlWorkNetIfAssignment_Type(Integer32):
    """Custom type flWorkNetIfAssignment based on Integer32"""
    defaultValue = 2

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
        *(("static", 1),
          ("bootp", 2),
          ("dhcp", 3),
          ("dcp", 4))
    )


_FlWorkNetIfAssignment_Type.__name__ = "Integer32"
_FlWorkNetIfAssignment_Object = MibTableColumn
flWorkNetIfAssignment = _FlWorkNetIfAssignment_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1, 1, 7),
    _FlWorkNetIfAssignment_Type()
)
flWorkNetIfAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfAssignment.setStatus("current")


class _FlWorkNetIfManagementVlanId_Type(Integer32):
    """Custom type flWorkNetIfManagementVlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FlWorkNetIfManagementVlanId_Type.__name__ = "Integer32"
_FlWorkNetIfManagementVlanId_Object = MibTableColumn
flWorkNetIfManagementVlanId = _FlWorkNetIfManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 3, 1, 1, 8),
    _FlWorkNetIfManagementVlanId_Type()
)
flWorkNetIfManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkNetIfManagementVlanId.setStatus("current")
_FlWorkNetACD_ObjectIdentity = ObjectIdentity
flWorkNetACD = _FlWorkNetACD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 5)
)


class _FlWorkNetACDStatus_Type(Integer32):
    """Custom type flWorkNetACDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("noConflict", 2),
          ("conflictDetected", 3))
    )


_FlWorkNetACDStatus_Type.__name__ = "Integer32"
_FlWorkNetACDStatus_Object = MibScalar
flWorkNetACDStatus = _FlWorkNetACDStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 5, 1),
    _FlWorkNetACDStatus_Type()
)
flWorkNetACDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetACDStatus.setStatus("current")
_FlWorkNetACDIP_Type = IpAddress
_FlWorkNetACDIP_Object = MibScalar
flWorkNetACDIP = _FlWorkNetACDIP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 5, 2),
    _FlWorkNetACDIP_Type()
)
flWorkNetACDIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetACDIP.setStatus("current")
_FlWorkNetACDMAC_Type = MacAddress
_FlWorkNetACDMAC_Object = MibScalar
flWorkNetACDMAC = _FlWorkNetACDMAC_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 4, 5, 3),
    _FlWorkNetACDMAC_Type()
)
flWorkNetACDMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkNetACDMAC.setStatus("current")
_FlWorkFirmware_ObjectIdentity = ObjectIdentity
flWorkFirmware = _FlWorkFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11)
)
_FlWorkFWInfo_ObjectIdentity = ObjectIdentity
flWorkFWInfo = _FlWorkFWInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1)
)
_FlWorkFWInfoVersion_Type = OctetString
_FlWorkFWInfoVersion_Object = MibScalar
flWorkFWInfoVersion = _FlWorkFWInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 1),
    _FlWorkFWInfoVersion_Type()
)
flWorkFWInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoVersion.setStatus("current")
_FlWorkFWInfoState_Type = OctetString
_FlWorkFWInfoState_Object = MibScalar
flWorkFWInfoState = _FlWorkFWInfoState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 2),
    _FlWorkFWInfoState_Type()
)
flWorkFWInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoState.setStatus("current")
_FlWorkFWInfoDate_Type = OctetString
_FlWorkFWInfoDate_Object = MibScalar
flWorkFWInfoDate = _FlWorkFWInfoDate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 3),
    _FlWorkFWInfoDate_Type()
)
flWorkFWInfoDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoDate.setStatus("current")
_FlWorkFWInfoTime_Type = OctetString
_FlWorkFWInfoTime_Object = MibScalar
flWorkFWInfoTime = _FlWorkFWInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 4),
    _FlWorkFWInfoTime_Type()
)
flWorkFWInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoTime.setStatus("current")
_FlWorkFWInfoCopyright_Type = DisplayString
_FlWorkFWInfoCopyright_Object = MibScalar
flWorkFWInfoCopyright = _FlWorkFWInfoCopyright_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 5),
    _FlWorkFWInfoCopyright_Type()
)
flWorkFWInfoCopyright.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoCopyright.setStatus("current")
_FlWorkFWInfoBootVersion_Type = OctetString
_FlWorkFWInfoBootVersion_Object = MibScalar
flWorkFWInfoBootVersion = _FlWorkFWInfoBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 6),
    _FlWorkFWInfoBootVersion_Type()
)
flWorkFWInfoBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoBootVersion.setStatus("current")
_FlWorkFWInfoBootState_Type = OctetString
_FlWorkFWInfoBootState_Object = MibScalar
flWorkFWInfoBootState = _FlWorkFWInfoBootState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 7),
    _FlWorkFWInfoBootState_Type()
)
flWorkFWInfoBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoBootState.setStatus("current")
_FlWorkFWInfoBootDate_Type = OctetString
_FlWorkFWInfoBootDate_Object = MibScalar
flWorkFWInfoBootDate = _FlWorkFWInfoBootDate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 8),
    _FlWorkFWInfoBootDate_Type()
)
flWorkFWInfoBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoBootDate.setStatus("current")
_FlWorkFWInfoBootTime_Type = OctetString
_FlWorkFWInfoBootTime_Object = MibScalar
flWorkFWInfoBootTime = _FlWorkFWInfoBootTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 9),
    _FlWorkFWInfoBootTime_Type()
)
flWorkFWInfoBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoBootTime.setStatus("current")


class _FlWorkFWInfoOperStatus_Type(Integer32):
    """Custom type flWorkFWInfoOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ok", 2),
          ("notOk", 3))
    )


_FlWorkFWInfoOperStatus_Type.__name__ = "Integer32"
_FlWorkFWInfoOperStatus_Object = MibScalar
flWorkFWInfoOperStatus = _FlWorkFWInfoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 11),
    _FlWorkFWInfoOperStatus_Type()
)
flWorkFWInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoOperStatus.setStatus("current")
_FlWorkFWInfoHealthText_Type = DisplayString
_FlWorkFWInfoHealthText_Object = MibScalar
flWorkFWInfoHealthText = _FlWorkFWInfoHealthText_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 12),
    _FlWorkFWInfoHealthText_Type()
)
flWorkFWInfoHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoHealthText.setStatus("current")
_FlWorkFWInfoDisplay_Type = DisplayString
_FlWorkFWInfoDisplay_Object = MibScalar
flWorkFWInfoDisplay = _FlWorkFWInfoDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 13),
    _FlWorkFWInfoDisplay_Type()
)
flWorkFWInfoDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoDisplay.setStatus("current")
_FlWorkFWInfoEvent_ObjectIdentity = ObjectIdentity
flWorkFWInfoEvent = _FlWorkFWInfoEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14)
)
_FlWorkFWInfoEventTable_Object = MibTable
flWorkFWInfoEventTable = _FlWorkFWInfoEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1)
)
if mibBuilder.loadTexts:
    flWorkFWInfoEventTable.setStatus("current")
_FlWorkFWInfoEventEntry_Object = MibTableRow
flWorkFWInfoEventEntry = _FlWorkFWInfoEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1, 1)
)
flWorkFWInfoEventEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWInfoEventIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWInfoEventEntry.setStatus("current")


class _FlWorkFWInfoEventIndex_Type(Integer32):
    """Custom type flWorkFWInfoEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_FlWorkFWInfoEventIndex_Type.__name__ = "Integer32"
_FlWorkFWInfoEventIndex_Object = MibTableColumn
flWorkFWInfoEventIndex = _FlWorkFWInfoEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1, 1, 1),
    _FlWorkFWInfoEventIndex_Type()
)
flWorkFWInfoEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoEventIndex.setStatus("current")
_FlWorkFWInfoEventCode_Type = Integer32
_FlWorkFWInfoEventCode_Object = MibTableColumn
flWorkFWInfoEventCode = _FlWorkFWInfoEventCode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1, 1, 2),
    _FlWorkFWInfoEventCode_Type()
)
flWorkFWInfoEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoEventCode.setStatus("current")
_FlWorkFWInfoEventDescription_Type = OctetString
_FlWorkFWInfoEventDescription_Object = MibTableColumn
flWorkFWInfoEventDescription = _FlWorkFWInfoEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1, 1, 3),
    _FlWorkFWInfoEventDescription_Type()
)
flWorkFWInfoEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoEventDescription.setStatus("current")
_FlWorkFWInfoEventSystemUpTime_Type = TimeTicks
_FlWorkFWInfoEventSystemUpTime_Object = MibTableColumn
flWorkFWInfoEventSystemUpTime = _FlWorkFWInfoEventSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1, 1, 4),
    _FlWorkFWInfoEventSystemUpTime_Type()
)
flWorkFWInfoEventSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoEventSystemUpTime.setStatus("current")
_FlWorkFWInfoEventSntpTime_Type = OctetString
_FlWorkFWInfoEventSntpTime_Object = MibTableColumn
flWorkFWInfoEventSntpTime = _FlWorkFWInfoEventSntpTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1, 1, 5),
    _FlWorkFWInfoEventSntpTime_Type()
)
flWorkFWInfoEventSntpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoEventSntpTime.setStatus("current")
_FlWorkFWInfoEventSntpDate_Type = OctetString
_FlWorkFWInfoEventSntpDate_Object = MibTableColumn
flWorkFWInfoEventSntpDate = _FlWorkFWInfoEventSntpDate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1, 1, 6),
    _FlWorkFWInfoEventSntpDate_Type()
)
flWorkFWInfoEventSntpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoEventSntpDate.setStatus("current")
_FlWorkFWInfoEventSntpSeconds_Type = Unsigned32
_FlWorkFWInfoEventSntpSeconds_Object = MibTableColumn
flWorkFWInfoEventSntpSeconds = _FlWorkFWInfoEventSntpSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1, 1, 7),
    _FlWorkFWInfoEventSntpSeconds_Type()
)
flWorkFWInfoEventSntpSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoEventSntpSeconds.setStatus("current")
_FlWorkFWInfoEventSntpFractionalSeconds_Type = Unsigned32
_FlWorkFWInfoEventSntpFractionalSeconds_Object = MibTableColumn
flWorkFWInfoEventSntpFractionalSeconds = _FlWorkFWInfoEventSntpFractionalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 1, 1, 8),
    _FlWorkFWInfoEventSntpFractionalSeconds_Type()
)
flWorkFWInfoEventSntpFractionalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWInfoEventSntpFractionalSeconds.setStatus("current")


class _FlWorkFWInfoEventTableClear_Type(Integer32):
    """Custom type flWorkFWInfoEventTableClear based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 1),
          ("clear", 2))
    )


_FlWorkFWInfoEventTableClear_Type.__name__ = "Integer32"
_FlWorkFWInfoEventTableClear_Object = MibScalar
flWorkFWInfoEventTableClear = _FlWorkFWInfoEventTableClear_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 1, 14, 2),
    _FlWorkFWInfoEventTableClear_Type()
)
flWorkFWInfoEventTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWInfoEventTableClear.setStatus("current")
_FlWorkFWCtrl_ObjectIdentity = ObjectIdentity
flWorkFWCtrl = _FlWorkFWCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2)
)
_FlWorkFWCtrlBasic_ObjectIdentity = ObjectIdentity
flWorkFWCtrlBasic = _FlWorkFWCtrlBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1)
)


class _FlWorkFWCtrlReset_Type(Integer32):
    """Custom type flWorkFWCtrlReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_FlWorkFWCtrlReset_Type.__name__ = "Integer32"
_FlWorkFWCtrlReset_Object = MibScalar
flWorkFWCtrlReset = _FlWorkFWCtrlReset_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 1),
    _FlWorkFWCtrlReset_Type()
)
flWorkFWCtrlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlReset.setStatus("current")


class _FlWorkFWCtrlTrapDestCapacity_Type(Integer32):
    """Custom type flWorkFWCtrlTrapDestCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkFWCtrlTrapDestCapacity_Type.__name__ = "Integer32"
_FlWorkFWCtrlTrapDestCapacity_Object = MibScalar
flWorkFWCtrlTrapDestCapacity = _FlWorkFWCtrlTrapDestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 2),
    _FlWorkFWCtrlTrapDestCapacity_Type()
)
flWorkFWCtrlTrapDestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapDestCapacity.setStatus("obsolete")


class _FlWorkFWCtrlWatchdog_Type(Integer32):
    """Custom type flWorkFWCtrlWatchdog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlWatchdog_Type.__name__ = "Integer32"
_FlWorkFWCtrlWatchdog_Object = MibScalar
flWorkFWCtrlWatchdog = _FlWorkFWCtrlWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 3),
    _FlWorkFWCtrlWatchdog_Type()
)
flWorkFWCtrlWatchdog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlWatchdog.setStatus("current")


class _FlWorkFWCtrlHTTP_Type(Integer32):
    """Custom type flWorkFWCtrlHTTP based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlHTTP_Type.__name__ = "Integer32"
_FlWorkFWCtrlHTTP_Object = MibScalar
flWorkFWCtrlHTTP = _FlWorkFWCtrlHTTP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 6),
    _FlWorkFWCtrlHTTP_Type()
)
flWorkFWCtrlHTTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlHTTP.setStatus("deprecated")


class _FlWorkFWCtrlTelnet_Type(Integer32):
    """Custom type flWorkFWCtrlTelnet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlTelnet_Type.__name__ = "Integer32"
_FlWorkFWCtrlTelnet_Object = MibScalar
flWorkFWCtrlTelnet = _FlWorkFWCtrlTelnet_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 7),
    _FlWorkFWCtrlTelnet_Type()
)
flWorkFWCtrlTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTelnet.setStatus("deprecated")


class _FlWorkFWCtrlWebPageRefresh_Type(Integer32):
    """Custom type flWorkFWCtrlWebPageRefresh based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FlWorkFWCtrlWebPageRefresh_Type.__name__ = "Integer32"
_FlWorkFWCtrlWebPageRefresh_Object = MibScalar
flWorkFWCtrlWebPageRefresh = _FlWorkFWCtrlWebPageRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 8),
    _FlWorkFWCtrlWebPageRefresh_Type()
)
flWorkFWCtrlWebPageRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlWebPageRefresh.setStatus("current")


class _FlWorkFWCtrlSNMP_Type(Integer32):
    """Custom type flWorkFWCtrlSNMP based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlSNMP_Type.__name__ = "Integer32"
_FlWorkFWCtrlSNMP_Object = MibScalar
flWorkFWCtrlSNMP = _FlWorkFWCtrlSNMP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 9),
    _FlWorkFWCtrlSNMP_Type()
)
flWorkFWCtrlSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSNMP.setStatus("deprecated")


class _FlWorkFWCtrlOperatingMode_Type(Integer32):
    """Custom type flWorkFWCtrlOperatingMode based on Integer32"""
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
        *(("default", 1),
          ("profinet", 2),
          ("ethernetIP", 3))
    )


_FlWorkFWCtrlOperatingMode_Type.__name__ = "Integer32"
_FlWorkFWCtrlOperatingMode_Object = MibScalar
flWorkFWCtrlOperatingMode = _FlWorkFWCtrlOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 10),
    _FlWorkFWCtrlOperatingMode_Type()
)
flWorkFWCtrlOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlOperatingMode.setStatus("current")


class _FlWorkFWCtrlIfCounters_Type(Integer32):
    """Custom type flWorkFWCtrlIfCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 1),
          ("clear", 2))
    )


_FlWorkFWCtrlIfCounters_Type.__name__ = "Integer32"
_FlWorkFWCtrlIfCounters_Object = MibScalar
flWorkFWCtrlIfCounters = _FlWorkFWCtrlIfCounters_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 11),
    _FlWorkFWCtrlIfCounters_Type()
)
flWorkFWCtrlIfCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlIfCounters.setStatus("current")


class _FlWorkFWCtrlHTTPSecure_Type(Integer32):
    """Custom type flWorkFWCtrlHTTPSecure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlHTTPSecure_Type.__name__ = "Integer32"
_FlWorkFWCtrlHTTPSecure_Object = MibScalar
flWorkFWCtrlHTTPSecure = _FlWorkFWCtrlHTTPSecure_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 12),
    _FlWorkFWCtrlHTTPSecure_Type()
)
flWorkFWCtrlHTTPSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlHTTPSecure.setStatus("deprecated")


class _FlWorkFWCtrlSSH_Type(Integer32):
    """Custom type flWorkFWCtrlSSH based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlSSH_Type.__name__ = "Integer32"
_FlWorkFWCtrlSSH_Object = MibScalar
flWorkFWCtrlSSH = _FlWorkFWCtrlSSH_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 13),
    _FlWorkFWCtrlSSH_Type()
)
flWorkFWCtrlSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSSH.setStatus("deprecated")


class _FlWorkFWCtrlSNMPv3_Type(Integer32):
    """Custom type flWorkFWCtrlSNMPv3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlSNMPv3_Type.__name__ = "Integer32"
_FlWorkFWCtrlSNMPv3_Object = MibScalar
flWorkFWCtrlSNMPv3 = _FlWorkFWCtrlSNMPv3_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 14),
    _FlWorkFWCtrlSNMPv3_Type()
)
flWorkFWCtrlSNMPv3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSNMPv3.setStatus("deprecated")


class _FlWorkFwCtrlCpuOverloadStopForwarding_Type(Integer32):
    """Custom type flWorkFwCtrlCpuOverloadStopForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotStop", 1),
          ("stopForwarding", 2))
    )


_FlWorkFwCtrlCpuOverloadStopForwarding_Type.__name__ = "Integer32"
_FlWorkFwCtrlCpuOverloadStopForwarding_Object = MibScalar
flWorkFwCtrlCpuOverloadStopForwarding = _FlWorkFwCtrlCpuOverloadStopForwarding_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 15),
    _FlWorkFwCtrlCpuOverloadStopForwarding_Type()
)
flWorkFwCtrlCpuOverloadStopForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFwCtrlCpuOverloadStopForwarding.setStatus("current")


class _FlWorkFWCtrlDisplayRights_Type(Integer32):
    """Custom type flWorkFWCtrlDisplayRights based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlDisplayRights_Type.__name__ = "Integer32"
_FlWorkFWCtrlDisplayRights_Object = MibScalar
flWorkFWCtrlDisplayRights = _FlWorkFWCtrlDisplayRights_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 16),
    _FlWorkFWCtrlDisplayRights_Type()
)
flWorkFWCtrlDisplayRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDisplayRights.setStatus("current")


class _FlWorkFWCtrlDisplayContrast_Type(Integer32):
    """Custom type flWorkFWCtrlDisplayContrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlDisplayContrast_Type.__name__ = "Integer32"
_FlWorkFWCtrlDisplayContrast_Object = MibScalar
flWorkFWCtrlDisplayContrast = _FlWorkFWCtrlDisplayContrast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 17),
    _FlWorkFWCtrlDisplayContrast_Type()
)
flWorkFWCtrlDisplayContrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDisplayContrast.setStatus("current")


class _FlWorkFWCtrlCLIIPSock_Type(Integer32):
    """Custom type flWorkFWCtrlCLIIPSock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlCLIIPSock_Type.__name__ = "Integer32"
_FlWorkFWCtrlCLIIPSock_Object = MibScalar
flWorkFWCtrlCLIIPSock = _FlWorkFWCtrlCLIIPSock_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 18),
    _FlWorkFWCtrlCLIIPSock_Type()
)
flWorkFWCtrlCLIIPSock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlCLIIPSock.setStatus("current")


class _FlWorkFWCtrlLEDsOff_Type(Integer32):
    """Custom type flWorkFWCtrlLEDsOff based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlLEDsOff_Type.__name__ = "Integer32"
_FlWorkFWCtrlLEDsOff_Object = MibScalar
flWorkFWCtrlLEDsOff = _FlWorkFWCtrlLEDsOff_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 20),
    _FlWorkFWCtrlLEDsOff_Type()
)
flWorkFWCtrlLEDsOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlLEDsOff.setStatus("current")


class _FlWorkFWCtrlWebServerMode_Type(Integer32):
    """Custom type flWorkFWCtrlWebServerMode based on Integer32"""
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
        *(("disable", 1),
          ("http", 2),
          ("https", 3))
    )


_FlWorkFWCtrlWebServerMode_Type.__name__ = "Integer32"
_FlWorkFWCtrlWebServerMode_Object = MibScalar
flWorkFWCtrlWebServerMode = _FlWorkFWCtrlWebServerMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 21),
    _FlWorkFWCtrlWebServerMode_Type()
)
flWorkFWCtrlWebServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlWebServerMode.setStatus("current")


class _FlWorkFWCtrlSnmpAgentMode_Type(Integer32):
    """Custom type flWorkFWCtrlSnmpAgentMode based on Integer32"""
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
        *(("disable", 1),
          ("snmpV2c", 2),
          ("snmpV3", 3))
    )


_FlWorkFWCtrlSnmpAgentMode_Type.__name__ = "Integer32"
_FlWorkFWCtrlSnmpAgentMode_Object = MibScalar
flWorkFWCtrlSnmpAgentMode = _FlWorkFWCtrlSnmpAgentMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 22),
    _FlWorkFWCtrlSnmpAgentMode_Type()
)
flWorkFWCtrlSnmpAgentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSnmpAgentMode.setStatus("current")


class _FlWorkFWCtrlCliServiceMode_Type(Integer32):
    """Custom type flWorkFWCtrlCliServiceMode based on Integer32"""
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
        *(("disable", 1),
          ("telnet", 2),
          ("ssh", 3))
    )


_FlWorkFWCtrlCliServiceMode_Type.__name__ = "Integer32"
_FlWorkFWCtrlCliServiceMode_Object = MibScalar
flWorkFWCtrlCliServiceMode = _FlWorkFWCtrlCliServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 23),
    _FlWorkFWCtrlCliServiceMode_Type()
)
flWorkFWCtrlCliServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlCliServiceMode.setStatus("current")


class _FlWorkFWCtrlPersistentEventLoggingMode_Type(Integer32):
    """Custom type flWorkFWCtrlPersistentEventLoggingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlPersistentEventLoggingMode_Type.__name__ = "Integer32"
_FlWorkFWCtrlPersistentEventLoggingMode_Object = MibScalar
flWorkFWCtrlPersistentEventLoggingMode = _FlWorkFWCtrlPersistentEventLoggingMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 24),
    _FlWorkFWCtrlPersistentEventLoggingMode_Type()
)
flWorkFWCtrlPersistentEventLoggingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlPersistentEventLoggingMode.setStatus("current")


class _FlWorkFWCtrlSmartModeGblEnable_Type(Integer32):
    """Custom type flWorkFWCtrlSmartModeGblEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlSmartModeGblEnable_Type.__name__ = "Integer32"
_FlWorkFWCtrlSmartModeGblEnable_Object = MibScalar
flWorkFWCtrlSmartModeGblEnable = _FlWorkFWCtrlSmartModeGblEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 25),
    _FlWorkFWCtrlSmartModeGblEnable_Type()
)
flWorkFWCtrlSmartModeGblEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSmartModeGblEnable.setStatus("current")


class _FlWorkFWCtrlHostnameResolutionEnable_Type(Integer32):
    """Custom type flWorkFWCtrlHostnameResolutionEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlHostnameResolutionEnable_Type.__name__ = "Integer32"
_FlWorkFWCtrlHostnameResolutionEnable_Object = MibScalar
flWorkFWCtrlHostnameResolutionEnable = _FlWorkFWCtrlHostnameResolutionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 26),
    _FlWorkFWCtrlHostnameResolutionEnable_Type()
)
flWorkFWCtrlHostnameResolutionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlHostnameResolutionEnable.setStatus("current")
_FlWorkFWCtrlHostname_Type = DisplayString
_FlWorkFWCtrlHostname_Object = MibScalar
flWorkFWCtrlHostname = _FlWorkFWCtrlHostname_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 27),
    _FlWorkFWCtrlHostname_Type()
)
flWorkFWCtrlHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlHostname.setStatus("current")


class _FlWorkFWCtrlSdCardGblEnable_Type(Integer32):
    """Custom type flWorkFWCtrlSdCardGblEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlSdCardGblEnable_Type.__name__ = "Integer32"
_FlWorkFWCtrlSdCardGblEnable_Object = MibScalar
flWorkFWCtrlSdCardGblEnable = _FlWorkFWCtrlSdCardGblEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 28),
    _FlWorkFWCtrlSdCardGblEnable_Type()
)
flWorkFWCtrlSdCardGblEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSdCardGblEnable.setStatus("current")


class _FlWorkFWCtrlWebLoginRequired_Type(Integer32):
    """Custom type flWorkFWCtrlWebLoginRequired based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlWebLoginRequired_Type.__name__ = "Integer32"
_FlWorkFWCtrlWebLoginRequired_Object = MibScalar
flWorkFWCtrlWebLoginRequired = _FlWorkFWCtrlWebLoginRequired_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 29),
    _FlWorkFWCtrlWebLoginRequired_Type()
)
flWorkFWCtrlWebLoginRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlWebLoginRequired.setStatus("current")


class _FlWorkFWCtrlTopologyBasedIpPort_Type(Integer32):
    """Custom type flWorkFWCtrlTopologyBasedIpPort based on Integer32"""
    defaultValue = 0


_FlWorkFWCtrlTopologyBasedIpPort_Type.__name__ = "Integer32"
_FlWorkFWCtrlTopologyBasedIpPort_Object = MibScalar
flWorkFWCtrlTopologyBasedIpPort = _FlWorkFWCtrlTopologyBasedIpPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 30),
    _FlWorkFWCtrlTopologyBasedIpPort_Type()
)
flWorkFWCtrlTopologyBasedIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTopologyBasedIpPort.setStatus("current")


class _FlWorkFWCtrlTopologyBasedIpState_Type(Integer32):
    """Custom type flWorkFWCtrlTopologyBasedIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("client", 1),
          ("root", 2))
    )


_FlWorkFWCtrlTopologyBasedIpState_Type.__name__ = "Integer32"
_FlWorkFWCtrlTopologyBasedIpState_Object = MibScalar
flWorkFWCtrlTopologyBasedIpState = _FlWorkFWCtrlTopologyBasedIpState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 1, 31),
    _FlWorkFWCtrlTopologyBasedIpState_Type()
)
flWorkFWCtrlTopologyBasedIpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlTopologyBasedIpState.setStatus("current")
_FlWorkFWCtrlTrapDest_ObjectIdentity = ObjectIdentity
flWorkFWCtrlTrapDest = _FlWorkFWCtrlTrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2)
)
_FlWorkFWCtrlTrapDestTable_Object = MibTable
flWorkFWCtrlTrapDestTable = _FlWorkFWCtrlTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapDestTable.setStatus("current")
_FlWorkFWCtrlTrapDestEntry_Object = MibTableRow
flWorkFWCtrlTrapDestEntry = _FlWorkFWCtrlTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 1, 1)
)
flWorkFWCtrlTrapDestEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlTrapDestIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapDestEntry.setStatus("current")


class _FlWorkFWCtrlTrapDestIndex_Type(Integer32):
    """Custom type flWorkFWCtrlTrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlTrapDestIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlTrapDestIndex_Object = MibTableColumn
flWorkFWCtrlTrapDestIndex = _FlWorkFWCtrlTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 1, 1, 1),
    _FlWorkFWCtrlTrapDestIndex_Type()
)
flWorkFWCtrlTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapDestIndex.setStatus("current")
_FlWorkFWCtrlTrapDestIPAddr_Type = IpAddress
_FlWorkFWCtrlTrapDestIPAddr_Object = MibTableColumn
flWorkFWCtrlTrapDestIPAddr = _FlWorkFWCtrlTrapDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 1, 1, 2),
    _FlWorkFWCtrlTrapDestIPAddr_Type()
)
flWorkFWCtrlTrapDestIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapDestIPAddr.setStatus("current")


class _FlWorkFWCtrlTrapDestName_Type(DisplayString):
    """Custom type flWorkFWCtrlTrapDestName based on DisplayString"""
    defaultValue = OctetString("")


_FlWorkFWCtrlTrapDestName_Type.__name__ = "DisplayString"
_FlWorkFWCtrlTrapDestName_Object = MibTableColumn
flWorkFWCtrlTrapDestName = _FlWorkFWCtrlTrapDestName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 1, 1, 4),
    _FlWorkFWCtrlTrapDestName_Type()
)
flWorkFWCtrlTrapDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapDestName.setStatus("current")


class _FlWorkFWCtrlTrapDestCapacityMax_Type(Integer32):
    """Custom type flWorkFWCtrlTrapDestCapacityMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkFWCtrlTrapDestCapacityMax_Type.__name__ = "Integer32"
_FlWorkFWCtrlTrapDestCapacityMax_Object = MibScalar
flWorkFWCtrlTrapDestCapacityMax = _FlWorkFWCtrlTrapDestCapacityMax_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 2),
    _FlWorkFWCtrlTrapDestCapacityMax_Type()
)
flWorkFWCtrlTrapDestCapacityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapDestCapacityMax.setStatus("current")


class _FlWorkFWCtrlTrapDestEnable_Type(Integer32):
    """Custom type flWorkFWCtrlTrapDestEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlTrapDestEnable_Type.__name__ = "Integer32"
_FlWorkFWCtrlTrapDestEnable_Object = MibScalar
flWorkFWCtrlTrapDestEnable = _FlWorkFWCtrlTrapDestEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 3),
    _FlWorkFWCtrlTrapDestEnable_Type()
)
flWorkFWCtrlTrapDestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapDestEnable.setStatus("current")


class _FlWorkFWCtrlTrapLink_Type(Integer32):
    """Custom type flWorkFWCtrlTrapLink based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("phyPortNumber", 1),
          ("snmpIfIndex", 2))
    )


_FlWorkFWCtrlTrapLink_Type.__name__ = "Integer32"
_FlWorkFWCtrlTrapLink_Object = MibScalar
flWorkFWCtrlTrapLink = _FlWorkFWCtrlTrapLink_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 4),
    _FlWorkFWCtrlTrapLink_Type()
)
flWorkFWCtrlTrapLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapLink.setStatus("current")


class _FlWorkFWCtrlTrapConnectionTest_Type(Integer32):
    """Custom type flWorkFWCtrlTrapConnectionTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTrap", 1),
          ("sendTrap", 2))
    )


_FlWorkFWCtrlTrapConnectionTest_Type.__name__ = "Integer32"
_FlWorkFWCtrlTrapConnectionTest_Object = MibScalar
flWorkFWCtrlTrapConnectionTest = _FlWorkFWCtrlTrapConnectionTest_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 5),
    _FlWorkFWCtrlTrapConnectionTest_Type()
)
flWorkFWCtrlTrapConnectionTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapConnectionTest.setStatus("current")
_FlWorkFWCtrlTrapEnableTable_Object = MibTable
flWorkFWCtrlTrapEnableTable = _FlWorkFWCtrlTrapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 10)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapEnableTable.setStatus("current")
_FlWorkFWCtrlTrapEnableEntry_Object = MibTableRow
flWorkFWCtrlTrapEnableEntry = _FlWorkFWCtrlTrapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 10, 1)
)
flWorkFWCtrlTrapEnableEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlTrapEnableIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapEnableEntry.setStatus("current")


class _FlWorkFWCtrlTrapEnableIndex_Type(Integer32):
    """Custom type flWorkFWCtrlTrapEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlTrapEnableIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlTrapEnableIndex_Object = MibTableColumn
flWorkFWCtrlTrapEnableIndex = _FlWorkFWCtrlTrapEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 10, 1, 1),
    _FlWorkFWCtrlTrapEnableIndex_Type()
)
flWorkFWCtrlTrapEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapEnableIndex.setStatus("current")
_FlWorkFWCtrlTrapEnableOid_Type = ObjectIdentifier
_FlWorkFWCtrlTrapEnableOid_Object = MibTableColumn
flWorkFWCtrlTrapEnableOid = _FlWorkFWCtrlTrapEnableOid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 10, 1, 2),
    _FlWorkFWCtrlTrapEnableOid_Type()
)
flWorkFWCtrlTrapEnableOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapEnableOid.setStatus("current")
_FlWorkFWCtrlTrapEnableName_Type = DisplayString
_FlWorkFWCtrlTrapEnableName_Object = MibTableColumn
flWorkFWCtrlTrapEnableName = _FlWorkFWCtrlTrapEnableName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 10, 1, 3),
    _FlWorkFWCtrlTrapEnableName_Type()
)
flWorkFWCtrlTrapEnableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapEnableName.setStatus("current")


class _FlWorkFWCtrlTrapEnableStatus_Type(Integer32):
    """Custom type flWorkFWCtrlTrapEnableStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlTrapEnableStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlTrapEnableStatus_Object = MibTableColumn
flWorkFWCtrlTrapEnableStatus = _FlWorkFWCtrlTrapEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 2, 10, 1, 4),
    _FlWorkFWCtrlTrapEnableStatus_Type()
)
flWorkFWCtrlTrapEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapEnableStatus.setStatus("current")
_FlWorkFWCtrlPasswd_ObjectIdentity = ObjectIdentity
flWorkFWCtrlPasswd = _FlWorkFWCtrlPasswd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 3)
)


class _FlWorkFWCtrlPasswdSet_Type(OctetString):
    """Custom type flWorkFWCtrlPasswdSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 128),
    )


_FlWorkFWCtrlPasswdSet_Type.__name__ = "OctetString"
_FlWorkFWCtrlPasswdSet_Object = MibScalar
flWorkFWCtrlPasswdSet = _FlWorkFWCtrlPasswdSet_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 3, 1),
    _FlWorkFWCtrlPasswdSet_Type()
)
flWorkFWCtrlPasswdSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlPasswdSet.setStatus("current")


class _FlWorkFWCtrlPasswdSuccess_Type(Integer32):
    """Custom type flWorkFWCtrlPasswdSuccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notChanged", 1),
          ("notSuccessful", 2),
          ("successful", 3))
    )


_FlWorkFWCtrlPasswdSuccess_Type.__name__ = "Integer32"
_FlWorkFWCtrlPasswdSuccess_Object = MibScalar
flWorkFWCtrlPasswdSuccess = _FlWorkFWCtrlPasswdSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 3, 2),
    _FlWorkFWCtrlPasswdSuccess_Type()
)
flWorkFWCtrlPasswdSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlPasswdSuccess.setStatus("current")


class _FlWorkFWCtrlLoginExpire_Type(Integer32):
    """Custom type flWorkFWCtrlLoginExpire based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_FlWorkFWCtrlLoginExpire_Type.__name__ = "Integer32"
_FlWorkFWCtrlLoginExpire_Object = MibScalar
flWorkFWCtrlLoginExpire = _FlWorkFWCtrlLoginExpire_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 3, 3),
    _FlWorkFWCtrlLoginExpire_Type()
)
flWorkFWCtrlLoginExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlLoginExpire.setStatus("current")
_FlWorkFWCtrlUpdate_ObjectIdentity = ObjectIdentity
flWorkFWCtrlUpdate = _FlWorkFWCtrlUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 4)
)
_FlWorkFWCtrlTftpIPAddr_Type = IpAddress
_FlWorkFWCtrlTftpIPAddr_Object = MibScalar
flWorkFWCtrlTftpIPAddr = _FlWorkFWCtrlTftpIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 4, 2),
    _FlWorkFWCtrlTftpIPAddr_Type()
)
flWorkFWCtrlTftpIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTftpIPAddr.setStatus("current")


class _FlWorkFWCtrlTftpFile_Type(OctetString):
    """Custom type flWorkFWCtrlTftpFile based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FlWorkFWCtrlTftpFile_Type.__name__ = "OctetString"
_FlWorkFWCtrlTftpFile_Object = MibScalar
flWorkFWCtrlTftpFile = _FlWorkFWCtrlTftpFile_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 4, 3),
    _FlWorkFWCtrlTftpFile_Type()
)
flWorkFWCtrlTftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTftpFile.setStatus("current")


class _FlWorkFWCtrlUpdateStatus_Type(Integer32):
    """Custom type flWorkFWCtrlUpdateStatus based on Integer32"""
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
        *(("updateOk", 1),
          ("updateFault", 2),
          ("noUpdate", 3),
          ("unknown", 4))
    )


_FlWorkFWCtrlUpdateStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlUpdateStatus_Object = MibScalar
flWorkFWCtrlUpdateStatus = _FlWorkFWCtrlUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 4, 4),
    _FlWorkFWCtrlUpdateStatus_Type()
)
flWorkFWCtrlUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlUpdateStatus.setStatus("current")


class _FlWorkFWCtrlUpdateExecute_Type(Integer32):
    """Custom type flWorkFWCtrlUpdateExecute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noFwUpdate", 1),
          ("startFwUpdate", 2))
    )


_FlWorkFWCtrlUpdateExecute_Type.__name__ = "Integer32"
_FlWorkFWCtrlUpdateExecute_Object = MibScalar
flWorkFWCtrlUpdateExecute = _FlWorkFWCtrlUpdateExecute_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 4, 5),
    _FlWorkFWCtrlUpdateExecute_Type()
)
flWorkFWCtrlUpdateExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlUpdateExecute.setStatus("current")


class _FlWorkFWCtrlRunningUpdate_Type(Integer32):
    """Custom type flWorkFWCtrlRunningUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("errorConnection", 4),
          ("errorFilename", 5),
          ("errorFault", 6),
          ("errorParameter", 7))
    )


_FlWorkFWCtrlRunningUpdate_Type.__name__ = "Integer32"
_FlWorkFWCtrlRunningUpdate_Object = MibScalar
flWorkFWCtrlRunningUpdate = _FlWorkFWCtrlRunningUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 4, 6),
    _FlWorkFWCtrlRunningUpdate_Type()
)
flWorkFWCtrlRunningUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlRunningUpdate.setStatus("current")


class _FlWorkFWCtrlAutoUpdate_Type(Integer32):
    """Custom type flWorkFWCtrlAutoUpdate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAutoFwUpdate", 1),
          ("startAutoFwUpdate", 2))
    )


_FlWorkFWCtrlAutoUpdate_Type.__name__ = "Integer32"
_FlWorkFWCtrlAutoUpdate_Object = MibScalar
flWorkFWCtrlAutoUpdate = _FlWorkFWCtrlAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 4, 7),
    _FlWorkFWCtrlAutoUpdate_Type()
)
flWorkFWCtrlAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAutoUpdate.setStatus("current")


class _FlWorkFWCtrlTftpImage_Type(Integer32):
    """Custom type flWorkFWCtrlTftpImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_FlWorkFWCtrlTftpImage_Type.__name__ = "Integer32"
_FlWorkFWCtrlTftpImage_Object = MibScalar
flWorkFWCtrlTftpImage = _FlWorkFWCtrlTftpImage_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 4, 8),
    _FlWorkFWCtrlTftpImage_Type()
)
flWorkFWCtrlTftpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTftpImage.setStatus("current")
_FlWorkFWCtrlConf_ObjectIdentity = ObjectIdentity
flWorkFWCtrlConf = _FlWorkFWCtrlConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5)
)


class _FlWorkFWCtrlConfStatus_Type(Integer32):
    """Custom type flWorkFWCtrlConfStatus based on Integer32"""
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
        *(("configOK", 1),
          ("configFault", 2),
          ("configSaved", 3),
          ("configSaveInProgress", 4),
          ("replaced", 5))
    )


_FlWorkFWCtrlConfStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfStatus_Object = MibScalar
flWorkFWCtrlConfStatus = _FlWorkFWCtrlConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 1),
    _FlWorkFWCtrlConfStatus_Type()
)
flWorkFWCtrlConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfStatus.setStatus("current")


class _FlWorkFWCtrlConfSave_Type(Integer32):
    """Custom type flWorkFWCtrlConfSave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSave", 1),
          ("save", 2))
    )


_FlWorkFWCtrlConfSave_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfSave_Object = MibScalar
flWorkFWCtrlConfSave = _FlWorkFWCtrlConfSave_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 2),
    _FlWorkFWCtrlConfSave_Type()
)
flWorkFWCtrlConfSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfSave.setStatus("current")


class _FlWorkFWCtrlDefaultUponDelivery_Type(Integer32):
    """Custom type flWorkFWCtrlDefaultUponDelivery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDefaultUponDelivery", 1),
          ("defaultUponDelivery", 2))
    )


_FlWorkFWCtrlDefaultUponDelivery_Type.__name__ = "Integer32"
_FlWorkFWCtrlDefaultUponDelivery_Object = MibScalar
flWorkFWCtrlDefaultUponDelivery = _FlWorkFWCtrlDefaultUponDelivery_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 3),
    _FlWorkFWCtrlDefaultUponDelivery_Type()
)
flWorkFWCtrlDefaultUponDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDefaultUponDelivery.setStatus("current")


class _FlWorkFWCtrlConfName_Type(OctetString):
    """Custom type flWorkFWCtrlConfName based on OctetString"""
    defaultValue = OctetString("MMS configuration")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FlWorkFWCtrlConfName_Type.__name__ = "OctetString"
_FlWorkFWCtrlConfName_Object = MibScalar
flWorkFWCtrlConfName = _FlWorkFWCtrlConfName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 4),
    _FlWorkFWCtrlConfName_Type()
)
flWorkFWCtrlConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfName.setStatus("current")


class _FlWorkFWCtrlConfSource_Type(Integer32):
    """Custom type flWorkFWCtrlConfSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonVolatileMemoryDevice", 1),
          ("pluggableMemory", 2))
    )


_FlWorkFWCtrlConfSource_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfSource_Object = MibScalar
flWorkFWCtrlConfSource = _FlWorkFWCtrlConfSource_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 5),
    _FlWorkFWCtrlConfSource_Type()
)
flWorkFWCtrlConfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfSource.setStatus("current")


class _FlWorkFWCtrlLoginSessions_Type(Integer32):
    """Custom type flWorkFWCtrlLoginSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkFWCtrlLoginSessions_Type.__name__ = "Integer32"
_FlWorkFWCtrlLoginSessions_Object = MibScalar
flWorkFWCtrlLoginSessions = _FlWorkFWCtrlLoginSessions_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 6),
    _FlWorkFWCtrlLoginSessions_Type()
)
flWorkFWCtrlLoginSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlLoginSessions.setStatus("current")


class _FlWorkFWCtrlPasswords_Type(Integer32):
    """Custom type flWorkFWCtrlPasswords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkFWCtrlPasswords_Type.__name__ = "Integer32"
_FlWorkFWCtrlPasswords_Object = MibScalar
flWorkFWCtrlPasswords = _FlWorkFWCtrlPasswords_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 7),
    _FlWorkFWCtrlPasswords_Type()
)
flWorkFWCtrlPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlPasswords.setStatus("current")


class _FlWorkFWCtrlSwitchStats_Type(Integer32):
    """Custom type flWorkFWCtrlSwitchStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkFWCtrlSwitchStats_Type.__name__ = "Integer32"
_FlWorkFWCtrlSwitchStats_Object = MibScalar
flWorkFWCtrlSwitchStats = _FlWorkFWCtrlSwitchStats_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 8),
    _FlWorkFWCtrlSwitchStats_Type()
)
flWorkFWCtrlSwitchStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSwitchStats.setStatus("current")


class _FlWorkFWCtrlTrapLog_Type(Integer32):
    """Custom type flWorkFWCtrlTrapLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkFWCtrlTrapLog_Type.__name__ = "Integer32"
_FlWorkFWCtrlTrapLog_Object = MibScalar
flWorkFWCtrlTrapLog = _FlWorkFWCtrlTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 9),
    _FlWorkFWCtrlTrapLog_Type()
)
flWorkFWCtrlTrapLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTrapLog.setStatus("current")
_FlWorkFWConfig_ObjectIdentity = ObjectIdentity
flWorkFWConfig = _FlWorkFWConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 10)
)
_FlWorkFWConfigTftpIPAddr_Type = IpAddress
_FlWorkFWConfigTftpIPAddr_Object = MibScalar
flWorkFWConfigTftpIPAddr = _FlWorkFWConfigTftpIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 10, 2),
    _FlWorkFWConfigTftpIPAddr_Type()
)
flWorkFWConfigTftpIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWConfigTftpIPAddr.setStatus("current")


class _FlWorkFWConfigTftpFile_Type(OctetString):
    """Custom type flWorkFWConfigTftpFile based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FlWorkFWConfigTftpFile_Type.__name__ = "OctetString"
_FlWorkFWConfigTftpFile_Object = MibScalar
flWorkFWConfigTftpFile = _FlWorkFWConfigTftpFile_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 10, 3),
    _FlWorkFWConfigTftpFile_Type()
)
flWorkFWConfigTftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWConfigTftpFile.setStatus("current")


class _FlWorkFWConfigStatus_Type(Integer32):
    """Custom type flWorkFWConfigStatus based on Integer32"""
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
        *(("transferOk", 1),
          ("transferFault", 2),
          ("noTransfer", 3),
          ("unknown", 4))
    )


_FlWorkFWConfigStatus_Type.__name__ = "Integer32"
_FlWorkFWConfigStatus_Object = MibScalar
flWorkFWConfigStatus = _FlWorkFWConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 10, 4),
    _FlWorkFWConfigStatus_Type()
)
flWorkFWConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWConfigStatus.setStatus("current")


class _FlWorkFWConfigExecute_Type(Integer32):
    """Custom type flWorkFWConfigExecute based on Integer32"""
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
        *(("noTransfer", 1),
          ("hostToDevice", 2),
          ("deviceToHost", 3))
    )


_FlWorkFWConfigExecute_Type.__name__ = "Integer32"
_FlWorkFWConfigExecute_Object = MibScalar
flWorkFWConfigExecute = _FlWorkFWConfigExecute_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 10, 5),
    _FlWorkFWConfigExecute_Type()
)
flWorkFWConfigExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWConfigExecute.setStatus("current")


class _FlWorkFWRunningConfig_Type(Integer32):
    """Custom type flWorkFWRunningConfig based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("errorConnection", 4),
          ("errorFilename", 5),
          ("errorFault", 6))
    )


_FlWorkFWRunningConfig_Type.__name__ = "Integer32"
_FlWorkFWRunningConfig_Object = MibScalar
flWorkFWRunningConfig = _FlWorkFWRunningConfig_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 10, 6),
    _FlWorkFWRunningConfig_Type()
)
flWorkFWRunningConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWRunningConfig.setStatus("current")
_FlWorkFWCtrlConfigPluggable_ObjectIdentity = ObjectIdentity
flWorkFWCtrlConfigPluggable = _FlWorkFWCtrlConfigPluggable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11)
)


class _FlWorkFWCtrlConfPluggableStatus_Type(Integer32):
    """Custom type flWorkFWCtrlConfPluggableStatus based on Integer32"""
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
        *(("plugmemPresent", 1),
          ("plugmemBusy", 2),
          ("plugmemNotSupported", 3),
          ("plugmemNotPresent", 4),
          ("plugmemDefect", 5),
          ("plugmemWrongType", 6))
    )


_FlWorkFWCtrlConfPluggableStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfPluggableStatus_Object = MibScalar
flWorkFWCtrlConfPluggableStatus = _FlWorkFWCtrlConfPluggableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 1),
    _FlWorkFWCtrlConfPluggableStatus_Type()
)
flWorkFWCtrlConfPluggableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfPluggableStatus.setStatus("current")


class _FlWorkFWCtrlConfPluggableClear_Type(Integer32):
    """Custom type flWorkFWCtrlConfPluggableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 1),
          ("clear", 2))
    )


_FlWorkFWCtrlConfPluggableClear_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfPluggableClear_Object = MibScalar
flWorkFWCtrlConfPluggableClear = _FlWorkFWCtrlConfPluggableClear_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 2),
    _FlWorkFWCtrlConfPluggableClear_Type()
)
flWorkFWCtrlConfPluggableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfPluggableClear.setStatus("current")


class _FlWorkFWCtrlConfPluggableCompare_Type(Integer32):
    """Custom type flWorkFWCtrlConfPluggableCompare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCompare", 1),
          ("compare", 2))
    )


_FlWorkFWCtrlConfPluggableCompare_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfPluggableCompare_Object = MibScalar
flWorkFWCtrlConfPluggableCompare = _FlWorkFWCtrlConfPluggableCompare_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 3),
    _FlWorkFWCtrlConfPluggableCompare_Type()
)
flWorkFWCtrlConfPluggableCompare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfPluggableCompare.setStatus("current")


class _FlWorkFWCtrlConfPluggableCompareStatus_Type(Integer32):
    """Custom type flWorkFWCtrlConfPluggableCompareStatus based on Integer32"""
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
        *(("unknown", 1),
          ("compareInProgress", 2),
          ("configEqual", 3),
          ("configNotEqual", 4),
          ("memoryModuleEmpty", 5))
    )


_FlWorkFWCtrlConfPluggableCompareStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfPluggableCompareStatus_Object = MibScalar
flWorkFWCtrlConfPluggableCompareStatus = _FlWorkFWCtrlConfPluggableCompareStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 4),
    _FlWorkFWCtrlConfPluggableCompareStatus_Type()
)
flWorkFWCtrlConfPluggableCompareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfPluggableCompareStatus.setStatus("current")
_FlWorkFWCtrlConfigMemInfo_ObjectIdentity = ObjectIdentity
flWorkFWCtrlConfigMemInfo = _FlWorkFWCtrlConfigMemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 5)
)
_FlWorkFWCtrlConfigMemConfName_Type = OctetString
_FlWorkFWCtrlConfigMemConfName_Object = MibScalar
flWorkFWCtrlConfigMemConfName = _FlWorkFWCtrlConfigMemConfName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 5, 1),
    _FlWorkFWCtrlConfigMemConfName_Type()
)
flWorkFWCtrlConfigMemConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfigMemConfName.setStatus("current")
_FlWorkFWCtrlConfigMemFwVersion_Type = OctetString
_FlWorkFWCtrlConfigMemFwVersion_Object = MibScalar
flWorkFWCtrlConfigMemFwVersion = _FlWorkFWCtrlConfigMemFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 5, 2),
    _FlWorkFWCtrlConfigMemFwVersion_Type()
)
flWorkFWCtrlConfigMemFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfigMemFwVersion.setStatus("current")
_FlWorkFWCtrlConfigMemIpAddress_Type = OctetString
_FlWorkFWCtrlConfigMemIpAddress_Object = MibScalar
flWorkFWCtrlConfigMemIpAddress = _FlWorkFWCtrlConfigMemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 5, 3),
    _FlWorkFWCtrlConfigMemIpAddress_Type()
)
flWorkFWCtrlConfigMemIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfigMemIpAddress.setStatus("current")


class _FlWorkFWCtrlConfigMemMrmFunctionality_Type(Integer32):
    """Custom type flWorkFWCtrlConfigMemMrmFunctionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("available", 1))
    )


_FlWorkFWCtrlConfigMemMrmFunctionality_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfigMemMrmFunctionality_Object = MibScalar
flWorkFWCtrlConfigMemMrmFunctionality = _FlWorkFWCtrlConfigMemMrmFunctionality_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 5, 4),
    _FlWorkFWCtrlConfigMemMrmFunctionality_Type()
)
flWorkFWCtrlConfigMemMrmFunctionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfigMemMrmFunctionality.setStatus("current")
_FlWorkFWCtrlConfigMemSerialNumber_Type = Unsigned32
_FlWorkFWCtrlConfigMemSerialNumber_Object = MibScalar
flWorkFWCtrlConfigMemSerialNumber = _FlWorkFWCtrlConfigMemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 5, 5),
    _FlWorkFWCtrlConfigMemSerialNumber_Type()
)
flWorkFWCtrlConfigMemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfigMemSerialNumber.setStatus("current")
_FlWorkFWCtrlConfigMemManufacturingId_Type = Integer32
_FlWorkFWCtrlConfigMemManufacturingId_Object = MibScalar
flWorkFWCtrlConfigMemManufacturingId = _FlWorkFWCtrlConfigMemManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 5, 6),
    _FlWorkFWCtrlConfigMemManufacturingId_Type()
)
flWorkFWCtrlConfigMemManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfigMemManufacturingId.setStatus("current")


class _FlWorkFWCtrlConfigMemType_Type(Integer32):
    """Custom type flWorkFWCtrlConfigMemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("memPlug", 1),
          ("roConfigStick", 2))
    )


_FlWorkFWCtrlConfigMemType_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfigMemType_Object = MibScalar
flWorkFWCtrlConfigMemType = _FlWorkFWCtrlConfigMemType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 5, 7),
    _FlWorkFWCtrlConfigMemType_Type()
)
flWorkFWCtrlConfigMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfigMemType.setStatus("current")


class _FlWorkFWCtrlConfigMemL3License_Type(Integer32):
    """Custom type flWorkFWCtrlConfigMemL3License based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noLicense", 0),
          ("licenseAvailable", 1))
    )


_FlWorkFWCtrlConfigMemL3License_Type.__name__ = "Integer32"
_FlWorkFWCtrlConfigMemL3License_Object = MibScalar
flWorkFWCtrlConfigMemL3License = _FlWorkFWCtrlConfigMemL3License_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 5, 11, 5, 8),
    _FlWorkFWCtrlConfigMemL3License_Type()
)
flWorkFWCtrlConfigMemL3License.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlConfigMemL3License.setStatus("current")
_FlWorkFWCtrlSerial_ObjectIdentity = ObjectIdentity
flWorkFWCtrlSerial = _FlWorkFWCtrlSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 6)
)


class _FlWorkFWCtrlSerialBaud_Type(Integer32):
    """Custom type flWorkFWCtrlSerialBaud based on Integer32"""
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
        *(("baud2400", 1),
          ("baud9600", 2),
          ("baud19200", 3),
          ("baud38400", 4))
    )


_FlWorkFWCtrlSerialBaud_Type.__name__ = "Integer32"
_FlWorkFWCtrlSerialBaud_Object = MibScalar
flWorkFWCtrlSerialBaud = _FlWorkFWCtrlSerialBaud_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 6, 1),
    _FlWorkFWCtrlSerialBaud_Type()
)
flWorkFWCtrlSerialBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSerialBaud.setStatus("current")


class _FlWorkFWCtrlSerialDataBits_Type(Integer32):
    """Custom type flWorkFWCtrlSerialDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bits8", 1)
    )


_FlWorkFWCtrlSerialDataBits_Type.__name__ = "Integer32"
_FlWorkFWCtrlSerialDataBits_Object = MibScalar
flWorkFWCtrlSerialDataBits = _FlWorkFWCtrlSerialDataBits_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 6, 2),
    _FlWorkFWCtrlSerialDataBits_Type()
)
flWorkFWCtrlSerialDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSerialDataBits.setStatus("current")


class _FlWorkFWCtrlSerialStopBits_Type(Integer32):
    """Custom type flWorkFWCtrlSerialStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_FlWorkFWCtrlSerialStopBits_Type.__name__ = "Integer32"
_FlWorkFWCtrlSerialStopBits_Object = MibScalar
flWorkFWCtrlSerialStopBits = _FlWorkFWCtrlSerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 6, 3),
    _FlWorkFWCtrlSerialStopBits_Type()
)
flWorkFWCtrlSerialStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSerialStopBits.setStatus("current")


class _FlWorkFWCtrlSerialParity_Type(Integer32):
    """Custom type flWorkFWCtrlSerialParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("odd", 2),
          ("even", 3))
    )


_FlWorkFWCtrlSerialParity_Type.__name__ = "Integer32"
_FlWorkFWCtrlSerialParity_Object = MibScalar
flWorkFWCtrlSerialParity = _FlWorkFWCtrlSerialParity_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 6, 4),
    _FlWorkFWCtrlSerialParity_Type()
)
flWorkFWCtrlSerialParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSerialParity.setStatus("current")


class _FlWorkFWCtrlSerialFlowControl_Type(Integer32):
    """Custom type flWorkFWCtrlSerialFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("hardware", 2))
    )


_FlWorkFWCtrlSerialFlowControl_Type.__name__ = "Integer32"
_FlWorkFWCtrlSerialFlowControl_Object = MibScalar
flWorkFWCtrlSerialFlowControl = _FlWorkFWCtrlSerialFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 6, 5),
    _FlWorkFWCtrlSerialFlowControl_Type()
)
flWorkFWCtrlSerialFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSerialFlowControl.setStatus("current")


class _FlWorkFWCtrlSerialTimeout_Type(Integer32):
    """Custom type flWorkFWCtrlSerialTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_FlWorkFWCtrlSerialTimeout_Type.__name__ = "Integer32"
_FlWorkFWCtrlSerialTimeout_Object = MibScalar
flWorkFWCtrlSerialTimeout = _FlWorkFWCtrlSerialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 6, 6),
    _FlWorkFWCtrlSerialTimeout_Type()
)
flWorkFWCtrlSerialTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSerialTimeout.setStatus("current")
_FlWorkFWCtrlAlarmContact_ObjectIdentity = ObjectIdentity
flWorkFWCtrlAlarmContact = _FlWorkFWCtrlAlarmContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7)
)
_FlWorkFWCtrlAlarmContactEvents_ObjectIdentity = ObjectIdentity
flWorkFWCtrlAlarmContactEvents = _FlWorkFWCtrlAlarmContactEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 1)
)


class _FlWorkFWCtrlAlarmContactEventPowerSupply_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactEventPowerSupply based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContactEventPowerSupply_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactEventPowerSupply_Object = MibScalar
flWorkFWCtrlAlarmContactEventPowerSupply = _FlWorkFWCtrlAlarmContactEventPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 1, 1),
    _FlWorkFWCtrlAlarmContactEventPowerSupply_Type()
)
flWorkFWCtrlAlarmContactEventPowerSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactEventPowerSupply.setStatus("current")


class _FlWorkFWCtrlAlarmContactEventLinkState_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactEventLinkState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContactEventLinkState_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactEventLinkState_Object = MibScalar
flWorkFWCtrlAlarmContactEventLinkState = _FlWorkFWCtrlAlarmContactEventLinkState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 1, 2),
    _FlWorkFWCtrlAlarmContactEventLinkState_Type()
)
flWorkFWCtrlAlarmContactEventLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactEventLinkState.setStatus("current")


class _FlWorkFWCtrlAlarmContactEventSecurityPortBlocked_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactEventSecurityPortBlocked based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContactEventSecurityPortBlocked_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactEventSecurityPortBlocked_Object = MibScalar
flWorkFWCtrlAlarmContactEventSecurityPortBlocked = _FlWorkFWCtrlAlarmContactEventSecurityPortBlocked_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 1, 3),
    _FlWorkFWCtrlAlarmContactEventSecurityPortBlocked_Type()
)
flWorkFWCtrlAlarmContactEventSecurityPortBlocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactEventSecurityPortBlocked.setStatus("current")


class _FlWorkFWCtrlAlarmContactEventPoeFaultDetected_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactEventPoeFaultDetected based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContactEventPoeFaultDetected_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactEventPoeFaultDetected_Object = MibScalar
flWorkFWCtrlAlarmContactEventPoeFaultDetected = _FlWorkFWCtrlAlarmContactEventPoeFaultDetected_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 1, 4),
    _FlWorkFWCtrlAlarmContactEventPoeFaultDetected_Type()
)
flWorkFWCtrlAlarmContactEventPoeFaultDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactEventPoeFaultDetected.setStatus("current")


class _FlWorkFWCtrlAlarmContactEventMrpRingFailure_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactEventMrpRingFailure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContactEventMrpRingFailure_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactEventMrpRingFailure_Object = MibScalar
flWorkFWCtrlAlarmContactEventMrpRingFailure = _FlWorkFWCtrlAlarmContactEventMrpRingFailure_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 1, 5),
    _FlWorkFWCtrlAlarmContactEventMrpRingFailure_Type()
)
flWorkFWCtrlAlarmContactEventMrpRingFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactEventMrpRingFailure.setStatus("current")


class _FlWorkFWCtrlAlarmContactEventConfigMemFail_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactEventConfigMemFail based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContactEventConfigMemFail_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactEventConfigMemFail_Object = MibScalar
flWorkFWCtrlAlarmContactEventConfigMemFail = _FlWorkFWCtrlAlarmContactEventConfigMemFail_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 1, 6),
    _FlWorkFWCtrlAlarmContactEventConfigMemFail_Type()
)
flWorkFWCtrlAlarmContactEventConfigMemFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactEventConfigMemFail.setStatus("current")


class _FlWorkFWCtrlAlarmContactEventPoFScrjTransCritical_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactEventPoFScrjTransCritical based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContactEventPoFScrjTransCritical_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactEventPoFScrjTransCritical_Object = MibScalar
flWorkFWCtrlAlarmContactEventPoFScrjTransCritical = _FlWorkFWCtrlAlarmContactEventPoFScrjTransCritical_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 1, 7),
    _FlWorkFWCtrlAlarmContactEventPoFScrjTransCritical_Type()
)
flWorkFWCtrlAlarmContactEventPoFScrjTransCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactEventPoFScrjTransCritical.setStatus("current")


class _FlWorkFWCtrlAlarmContactEventDlrRingFailure_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactEventDlrRingFailure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContactEventDlrRingFailure_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactEventDlrRingFailure_Object = MibScalar
flWorkFWCtrlAlarmContactEventDlrRingFailure = _FlWorkFWCtrlAlarmContactEventDlrRingFailure_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 1, 8),
    _FlWorkFWCtrlAlarmContactEventDlrRingFailure_Type()
)
flWorkFWCtrlAlarmContactEventDlrRingFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactEventDlrRingFailure.setStatus("current")


class _FlWorkFWCtrlAlarmContactEnable_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContactEnable_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactEnable_Object = MibScalar
flWorkFWCtrlAlarmContactEnable = _FlWorkFWCtrlAlarmContactEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 2),
    _FlWorkFWCtrlAlarmContactEnable_Type()
)
flWorkFWCtrlAlarmContactEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactEnable.setStatus("current")


class _FlWorkFWCtrlAlarmContactStatus_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContactStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )


_FlWorkFWCtrlAlarmContactStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContactStatus_Object = MibScalar
flWorkFWCtrlAlarmContactStatus = _FlWorkFWCtrlAlarmContactStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 3),
    _FlWorkFWCtrlAlarmContactStatus_Type()
)
flWorkFWCtrlAlarmContactStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactStatus.setStatus("current")
_FlWorkFWCtrlAlarmContactReason_Type = DisplayString
_FlWorkFWCtrlAlarmContactReason_Object = MibScalar
flWorkFWCtrlAlarmContactReason = _FlWorkFWCtrlAlarmContactReason_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 4),
    _FlWorkFWCtrlAlarmContactReason_Type()
)
flWorkFWCtrlAlarmContactReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContactReason.setStatus("current")
_FlWorkFWCtrlAlarmContact2Events_ObjectIdentity = ObjectIdentity
flWorkFWCtrlAlarmContact2Events = _FlWorkFWCtrlAlarmContact2Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 11)
)


class _FlWorkFWCtrlAlarmContact2EventPowerSupply_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2EventPowerSupply based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContact2EventPowerSupply_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2EventPowerSupply_Object = MibScalar
flWorkFWCtrlAlarmContact2EventPowerSupply = _FlWorkFWCtrlAlarmContact2EventPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 11, 1),
    _FlWorkFWCtrlAlarmContact2EventPowerSupply_Type()
)
flWorkFWCtrlAlarmContact2EventPowerSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2EventPowerSupply.setStatus("current")


class _FlWorkFWCtrlAlarmContact2EventLinkState_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2EventLinkState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContact2EventLinkState_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2EventLinkState_Object = MibScalar
flWorkFWCtrlAlarmContact2EventLinkState = _FlWorkFWCtrlAlarmContact2EventLinkState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 11, 2),
    _FlWorkFWCtrlAlarmContact2EventLinkState_Type()
)
flWorkFWCtrlAlarmContact2EventLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2EventLinkState.setStatus("current")


class _FlWorkFWCtrlAlarmContact2EventSecurityPortBlocked_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2EventSecurityPortBlocked based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContact2EventSecurityPortBlocked_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2EventSecurityPortBlocked_Object = MibScalar
flWorkFWCtrlAlarmContact2EventSecurityPortBlocked = _FlWorkFWCtrlAlarmContact2EventSecurityPortBlocked_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 11, 3),
    _FlWorkFWCtrlAlarmContact2EventSecurityPortBlocked_Type()
)
flWorkFWCtrlAlarmContact2EventSecurityPortBlocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2EventSecurityPortBlocked.setStatus("current")


class _FlWorkFWCtrlAlarmContact2EventPoeFaultDetected_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2EventPoeFaultDetected based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContact2EventPoeFaultDetected_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2EventPoeFaultDetected_Object = MibScalar
flWorkFWCtrlAlarmContact2EventPoeFaultDetected = _FlWorkFWCtrlAlarmContact2EventPoeFaultDetected_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 11, 4),
    _FlWorkFWCtrlAlarmContact2EventPoeFaultDetected_Type()
)
flWorkFWCtrlAlarmContact2EventPoeFaultDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2EventPoeFaultDetected.setStatus("current")


class _FlWorkFWCtrlAlarmContact2EventMrpRingFailure_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2EventMrpRingFailure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContact2EventMrpRingFailure_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2EventMrpRingFailure_Object = MibScalar
flWorkFWCtrlAlarmContact2EventMrpRingFailure = _FlWorkFWCtrlAlarmContact2EventMrpRingFailure_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 11, 5),
    _FlWorkFWCtrlAlarmContact2EventMrpRingFailure_Type()
)
flWorkFWCtrlAlarmContact2EventMrpRingFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2EventMrpRingFailure.setStatus("current")


class _FlWorkFWCtrlAlarmContact2EventConfigMemFail_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2EventConfigMemFail based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContact2EventConfigMemFail_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2EventConfigMemFail_Object = MibScalar
flWorkFWCtrlAlarmContact2EventConfigMemFail = _FlWorkFWCtrlAlarmContact2EventConfigMemFail_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 11, 6),
    _FlWorkFWCtrlAlarmContact2EventConfigMemFail_Type()
)
flWorkFWCtrlAlarmContact2EventConfigMemFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2EventConfigMemFail.setStatus("current")


class _FlWorkFWCtrlAlarmContact2EventPoFScrjTransCritical_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2EventPoFScrjTransCritical based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContact2EventPoFScrjTransCritical_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2EventPoFScrjTransCritical_Object = MibScalar
flWorkFWCtrlAlarmContact2EventPoFScrjTransCritical = _FlWorkFWCtrlAlarmContact2EventPoFScrjTransCritical_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 11, 7),
    _FlWorkFWCtrlAlarmContact2EventPoFScrjTransCritical_Type()
)
flWorkFWCtrlAlarmContact2EventPoFScrjTransCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2EventPoFScrjTransCritical.setStatus("current")


class _FlWorkFWCtrlAlarmContact2EventDlrRingFailure_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2EventDlrRingFailure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContact2EventDlrRingFailure_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2EventDlrRingFailure_Object = MibScalar
flWorkFWCtrlAlarmContact2EventDlrRingFailure = _FlWorkFWCtrlAlarmContact2EventDlrRingFailure_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 11, 8),
    _FlWorkFWCtrlAlarmContact2EventDlrRingFailure_Type()
)
flWorkFWCtrlAlarmContact2EventDlrRingFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2EventDlrRingFailure.setStatus("current")


class _FlWorkFWCtrlAlarmContact2Enable_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2Enable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlAlarmContact2Enable_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2Enable_Object = MibScalar
flWorkFWCtrlAlarmContact2Enable = _FlWorkFWCtrlAlarmContact2Enable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 12),
    _FlWorkFWCtrlAlarmContact2Enable_Type()
)
flWorkFWCtrlAlarmContact2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2Enable.setStatus("current")


class _FlWorkFWCtrlAlarmContact2Status_Type(Integer32):
    """Custom type flWorkFWCtrlAlarmContact2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )


_FlWorkFWCtrlAlarmContact2Status_Type.__name__ = "Integer32"
_FlWorkFWCtrlAlarmContact2Status_Object = MibScalar
flWorkFWCtrlAlarmContact2Status = _FlWorkFWCtrlAlarmContact2Status_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 13),
    _FlWorkFWCtrlAlarmContact2Status_Type()
)
flWorkFWCtrlAlarmContact2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2Status.setStatus("current")
_FlWorkFWCtrlAlarmContact2Reason_Type = DisplayString
_FlWorkFWCtrlAlarmContact2Reason_Object = MibScalar
flWorkFWCtrlAlarmContact2Reason = _FlWorkFWCtrlAlarmContact2Reason_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 7, 14),
    _FlWorkFWCtrlAlarmContact2Reason_Type()
)
flWorkFWCtrlAlarmContact2Reason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlAlarmContact2Reason.setStatus("current")
_FlWorkFWCtrlSecurity_ObjectIdentity = ObjectIdentity
flWorkFWCtrlSecurity = _FlWorkFWCtrlSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8)
)
_FlWorkFWCtrlSecurityAccess_ObjectIdentity = ObjectIdentity
flWorkFWCtrlSecurityAccess = _FlWorkFWCtrlSecurityAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 1)
)
_FlWorkFWCtrlSecurityAccessTable_Object = MibTable
flWorkFWCtrlSecurityAccessTable = _FlWorkFWCtrlSecurityAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityAccessTable.setStatus("current")
_FlWorkFWCtrlSecurityAccessEntry_Object = MibTableRow
flWorkFWCtrlSecurityAccessEntry = _FlWorkFWCtrlSecurityAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 1, 1, 1)
)
flWorkFWCtrlSecurityAccessEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlSecurityAccessIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityAccessEntry.setStatus("current")


class _FlWorkFWCtrlSecurityAccessIndex_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkFWCtrlSecurityAccessIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityAccessIndex_Object = MibTableColumn
flWorkFWCtrlSecurityAccessIndex = _FlWorkFWCtrlSecurityAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 1, 1, 1, 1),
    _FlWorkFWCtrlSecurityAccessIndex_Type()
)
flWorkFWCtrlSecurityAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityAccessIndex.setStatus("current")
_FlWorkFWCtrlSecurityAccessAddr_Type = IpAddress
_FlWorkFWCtrlSecurityAccessAddr_Object = MibTableColumn
flWorkFWCtrlSecurityAccessAddr = _FlWorkFWCtrlSecurityAccessAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 1, 1, 1, 2),
    _FlWorkFWCtrlSecurityAccessAddr_Type()
)
flWorkFWCtrlSecurityAccessAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityAccessAddr.setStatus("current")


class _FlWorkFWCtrlSecurityAccessDescr_Type(OctetString):
    """Custom type flWorkFWCtrlSecurityAccessDescr based on OctetString"""
    defaultValue = OctetString("Allowed address x")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FlWorkFWCtrlSecurityAccessDescr_Type.__name__ = "OctetString"
_FlWorkFWCtrlSecurityAccessDescr_Object = MibTableColumn
flWorkFWCtrlSecurityAccessDescr = _FlWorkFWCtrlSecurityAccessDescr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 1, 1, 1, 3),
    _FlWorkFWCtrlSecurityAccessDescr_Type()
)
flWorkFWCtrlSecurityAccessDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityAccessDescr.setStatus("current")


class _FlWorkFWCtrlSecurityAccessRight_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityAccessRight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_FlWorkFWCtrlSecurityAccessRight_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityAccessRight_Object = MibTableColumn
flWorkFWCtrlSecurityAccessRight = _FlWorkFWCtrlSecurityAccessRight_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 1, 1, 1, 4),
    _FlWorkFWCtrlSecurityAccessRight_Type()
)
flWorkFWCtrlSecurityAccessRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityAccessRight.setStatus("current")
_FlWorkFWCtrlSecurityAccessTableCapacityMax_Type = Integer32
_FlWorkFWCtrlSecurityAccessTableCapacityMax_Object = MibScalar
flWorkFWCtrlSecurityAccessTableCapacityMax = _FlWorkFWCtrlSecurityAccessTableCapacityMax_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 1, 2),
    _FlWorkFWCtrlSecurityAccessTableCapacityMax_Type()
)
flWorkFWCtrlSecurityAccessTableCapacityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityAccessTableCapacityMax.setStatus("current")


class _FlWorkFWCtrlSecurityAccessEnable_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityAccessEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlSecurityAccessEnable_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityAccessEnable_Object = MibScalar
flWorkFWCtrlSecurityAccessEnable = _FlWorkFWCtrlSecurityAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 1, 3),
    _FlWorkFWCtrlSecurityAccessEnable_Type()
)
flWorkFWCtrlSecurityAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityAccessEnable.setStatus("current")
_FlWorkFWCtrlSecurityPort_ObjectIdentity = ObjectIdentity
flWorkFWCtrlSecurityPort = _FlWorkFWCtrlSecurityPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2)
)
_FlWorkFWCtrlSecurityPortTable_Object = MibTable
flWorkFWCtrlSecurityPortTable = _FlWorkFWCtrlSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortTable.setStatus("current")
_FlWorkFWCtrlSecurityPortEntry_Object = MibTableRow
flWorkFWCtrlSecurityPortEntry = _FlWorkFWCtrlSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 1, 1)
)
flWorkFWCtrlSecurityPortEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortEntry.setStatus("current")


class _FlWorkFWCtrlSecurityPortIndex_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlSecurityPortIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortIndex_Object = MibTableColumn
flWorkFWCtrlSecurityPortIndex = _FlWorkFWCtrlSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 1, 1, 1),
    _FlWorkFWCtrlSecurityPortIndex_Type()
)
flWorkFWCtrlSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIndex.setStatus("current")
_FlWorkFWCtrlSecurityPortLastMacAddr_Type = MacAddress
_FlWorkFWCtrlSecurityPortLastMacAddr_Object = MibTableColumn
flWorkFWCtrlSecurityPortLastMacAddr = _FlWorkFWCtrlSecurityPortLastMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 1, 1, 2),
    _FlWorkFWCtrlSecurityPortLastMacAddr_Type()
)
flWorkFWCtrlSecurityPortLastMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortLastMacAddr.setStatus("current")


class _FlWorkFWCtrlSecurityPortMode_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortMode based on Integer32"""
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
        *(("noSecurity", 1),
          ("trapOnly", 2),
          ("blockPackets", 3),
          ("blockPacketsWithAutoReenabling", 4),
          ("passPackets", 5))
    )


_FlWorkFWCtrlSecurityPortMode_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortMode_Object = MibTableColumn
flWorkFWCtrlSecurityPortMode = _FlWorkFWCtrlSecurityPortMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 1, 1, 3),
    _FlWorkFWCtrlSecurityPortMode_Type()
)
flWorkFWCtrlSecurityPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortMode.setStatus("current")


class _FlWorkFWCtrlSecurityPortState_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("blocking", 2),
          ("reenabling", 3))
    )


_FlWorkFWCtrlSecurityPortState_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortState_Object = MibTableColumn
flWorkFWCtrlSecurityPortState = _FlWorkFWCtrlSecurityPortState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 1, 1, 4),
    _FlWorkFWCtrlSecurityPortState_Type()
)
flWorkFWCtrlSecurityPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortState.setStatus("current")
_FlWorkFWCtrlSecurityPortIllegalAddrCounter_Type = Gauge32
_FlWorkFWCtrlSecurityPortIllegalAddrCounter_Object = MibTableColumn
flWorkFWCtrlSecurityPortIllegalAddrCounter = _FlWorkFWCtrlSecurityPortIllegalAddrCounter_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 1, 1, 5),
    _FlWorkFWCtrlSecurityPortIllegalAddrCounter_Type()
)
flWorkFWCtrlSecurityPortIllegalAddrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIllegalAddrCounter.setStatus("current")
_FlWorkFWCtrlSecurityPortMacTable_Object = MibTable
flWorkFWCtrlSecurityPortMacTable = _FlWorkFWCtrlSecurityPortMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 2)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortMacTable.setStatus("current")
_FlWorkFWCtrlSecurityPortMacEntry_Object = MibTableRow
flWorkFWCtrlSecurityPortMacEntry = _FlWorkFWCtrlSecurityPortMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 2, 1)
)
flWorkFWCtrlSecurityPortMacEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlSecurityPortIndex"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlSecurityPortMacIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortMacEntry.setStatus("current")


class _FlWorkFWCtrlSecurityPortMacIndex_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlSecurityPortMacIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortMacIndex_Object = MibTableColumn
flWorkFWCtrlSecurityPortMacIndex = _FlWorkFWCtrlSecurityPortMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 2, 1, 1),
    _FlWorkFWCtrlSecurityPortMacIndex_Type()
)
flWorkFWCtrlSecurityPortMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortMacIndex.setStatus("current")
_FlWorkFWCtrlSecurityPortMacAddr_Type = MacAddress
_FlWorkFWCtrlSecurityPortMacAddr_Object = MibTableColumn
flWorkFWCtrlSecurityPortMacAddr = _FlWorkFWCtrlSecurityPortMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 2, 1, 2),
    _FlWorkFWCtrlSecurityPortMacAddr_Type()
)
flWorkFWCtrlSecurityPortMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortMacAddr.setStatus("current")


class _FlWorkFWCtrlSecurityPortMacDescr_Type(OctetString):
    """Custom type flWorkFWCtrlSecurityPortMacDescr based on OctetString"""
    defaultValue = OctetString("Allowed port xx")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FlWorkFWCtrlSecurityPortMacDescr_Type.__name__ = "OctetString"
_FlWorkFWCtrlSecurityPortMacDescr_Object = MibTableColumn
flWorkFWCtrlSecurityPortMacDescr = _FlWorkFWCtrlSecurityPortMacDescr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 2, 1, 3),
    _FlWorkFWCtrlSecurityPortMacDescr_Type()
)
flWorkFWCtrlSecurityPortMacDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortMacDescr.setStatus("current")


class _FlWorkFWCtrlSecurityPortMacVlanID_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortMacVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FlWorkFWCtrlSecurityPortMacVlanID_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortMacVlanID_Object = MibTableColumn
flWorkFWCtrlSecurityPortMacVlanID = _FlWorkFWCtrlSecurityPortMacVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 2, 1, 4),
    _FlWorkFWCtrlSecurityPortMacVlanID_Type()
)
flWorkFWCtrlSecurityPortMacVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortMacVlanID.setStatus("current")


class _FlWorkFWCtrlSecurityPortMacDelete_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortMacDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keepMAC", 1),
          ("deleteMAC", 2))
    )


_FlWorkFWCtrlSecurityPortMacDelete_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortMacDelete_Object = MibTableColumn
flWorkFWCtrlSecurityPortMacDelete = _FlWorkFWCtrlSecurityPortMacDelete_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 2, 1, 5),
    _FlWorkFWCtrlSecurityPortMacDelete_Type()
)
flWorkFWCtrlSecurityPortMacDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortMacDelete.setStatus("current")
_FlWorkFWCtrlSecurityPortTableCapacityMax_Type = Integer32
_FlWorkFWCtrlSecurityPortTableCapacityMax_Object = MibScalar
flWorkFWCtrlSecurityPortTableCapacityMax = _FlWorkFWCtrlSecurityPortTableCapacityMax_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 3),
    _FlWorkFWCtrlSecurityPortTableCapacityMax_Type()
)
flWorkFWCtrlSecurityPortTableCapacityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortTableCapacityMax.setStatus("current")
_FlWorkFWCtrlSecurityPortMacTableCapacityMax_Type = Integer32
_FlWorkFWCtrlSecurityPortMacTableCapacityMax_Object = MibScalar
flWorkFWCtrlSecurityPortMacTableCapacityMax = _FlWorkFWCtrlSecurityPortMacTableCapacityMax_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 4),
    _FlWorkFWCtrlSecurityPortMacTableCapacityMax_Type()
)
flWorkFWCtrlSecurityPortMacTableCapacityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortMacTableCapacityMax.setStatus("current")


class _FlWorkFWCtrlSecurityPortEnable_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlSecurityPortEnable_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortEnable_Object = MibScalar
flWorkFWCtrlSecurityPortEnable = _FlWorkFWCtrlSecurityPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 5),
    _FlWorkFWCtrlSecurityPortEnable_Type()
)
flWorkFWCtrlSecurityPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortEnable.setStatus("current")


class _FlWorkFWCtrlSecurityPortIllegalAddrCounterClear_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortIllegalAddrCounterClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 1),
          ("clear", 2))
    )


_FlWorkFWCtrlSecurityPortIllegalAddrCounterClear_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortIllegalAddrCounterClear_Object = MibScalar
flWorkFWCtrlSecurityPortIllegalAddrCounterClear = _FlWorkFWCtrlSecurityPortIllegalAddrCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 6),
    _FlWorkFWCtrlSecurityPortIllegalAddrCounterClear_Type()
)
flWorkFWCtrlSecurityPortIllegalAddrCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIllegalAddrCounterClear.setStatus("current")
_FlWorkFWCtrlSecurityPortIpFilterTable_Object = MibTable
flWorkFWCtrlSecurityPortIpFilterTable = _FlWorkFWCtrlSecurityPortIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 7)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIpFilterTable.setStatus("current")
_FlWorkFWCtrlSecurityPortIpFilterEntry_Object = MibTableRow
flWorkFWCtrlSecurityPortIpFilterEntry = _FlWorkFWCtrlSecurityPortIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 7, 1)
)
flWorkFWCtrlSecurityPortIpFilterEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlSecurityPortIndex"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlSecurityPortIpFilterIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIpFilterEntry.setStatus("current")


class _FlWorkFWCtrlSecurityPortIpFilterIndex_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortIpFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlSecurityPortIpFilterIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortIpFilterIndex_Object = MibTableColumn
flWorkFWCtrlSecurityPortIpFilterIndex = _FlWorkFWCtrlSecurityPortIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 7, 1, 1),
    _FlWorkFWCtrlSecurityPortIpFilterIndex_Type()
)
flWorkFWCtrlSecurityPortIpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIpFilterIndex.setStatus("current")
_FlWorkFWCtrlSecurityPortIpFilterAddr_Type = IpAddress
_FlWorkFWCtrlSecurityPortIpFilterAddr_Object = MibTableColumn
flWorkFWCtrlSecurityPortIpFilterAddr = _FlWorkFWCtrlSecurityPortIpFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 7, 1, 2),
    _FlWorkFWCtrlSecurityPortIpFilterAddr_Type()
)
flWorkFWCtrlSecurityPortIpFilterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIpFilterAddr.setStatus("current")


class _FlWorkFWCtrlSecurityPortIpFilterDescr_Type(OctetString):
    """Custom type flWorkFWCtrlSecurityPortIpFilterDescr based on OctetString"""
    defaultValue = OctetString("Allowed port xx")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FlWorkFWCtrlSecurityPortIpFilterDescr_Type.__name__ = "OctetString"
_FlWorkFWCtrlSecurityPortIpFilterDescr_Object = MibTableColumn
flWorkFWCtrlSecurityPortIpFilterDescr = _FlWorkFWCtrlSecurityPortIpFilterDescr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 7, 1, 3),
    _FlWorkFWCtrlSecurityPortIpFilterDescr_Type()
)
flWorkFWCtrlSecurityPortIpFilterDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIpFilterDescr.setStatus("current")


class _FlWorkFWCtrlSecurityPortIpFilterPort_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityPortIpFilterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlWorkFWCtrlSecurityPortIpFilterPort_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityPortIpFilterPort_Object = MibTableColumn
flWorkFWCtrlSecurityPortIpFilterPort = _FlWorkFWCtrlSecurityPortIpFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 7, 1, 4),
    _FlWorkFWCtrlSecurityPortIpFilterPort_Type()
)
flWorkFWCtrlSecurityPortIpFilterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIpFilterPort.setStatus("current")
_FlWorkFWCtrlSecurityPortIpFilterTableCapacityMax_Type = Integer32
_FlWorkFWCtrlSecurityPortIpFilterTableCapacityMax_Object = MibScalar
flWorkFWCtrlSecurityPortIpFilterTableCapacityMax = _FlWorkFWCtrlSecurityPortIpFilterTableCapacityMax_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 8),
    _FlWorkFWCtrlSecurityPortIpFilterTableCapacityMax_Type()
)
flWorkFWCtrlSecurityPortIpFilterTableCapacityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityPortIpFilterTableCapacityMax.setStatus("current")


class _FlWorkFWCtrlSecurityMAConMultiplePorts_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityMAConMultiplePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlSecurityMAConMultiplePorts_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityMAConMultiplePorts_Object = MibScalar
flWorkFWCtrlSecurityMAConMultiplePorts = _FlWorkFWCtrlSecurityMAConMultiplePorts_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 2, 9),
    _FlWorkFWCtrlSecurityMAConMultiplePorts_Type()
)
flWorkFWCtrlSecurityMAConMultiplePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityMAConMultiplePorts.setStatus("current")
_FlWorkFWCtrlSecurityDot1x_ObjectIdentity = ObjectIdentity
flWorkFWCtrlSecurityDot1x = _FlWorkFWCtrlSecurityDot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3)
)
_FlWorkFWCtrlSecurityDot1xPortTable_Object = MibTable
flWorkFWCtrlSecurityDot1xPortTable = _FlWorkFWCtrlSecurityDot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityDot1xPortTable.setStatus("current")
_FlWorkFWCtrlSecurityDot1xPortEntry_Object = MibTableRow
flWorkFWCtrlSecurityDot1xPortEntry = _FlWorkFWCtrlSecurityDot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 1, 1)
)
flWorkFWCtrlSecurityDot1xPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityDot1xPortEntry.setStatus("current")


class _FlWorkFWCtrlSecurityDot1xGuestVlanId_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityDot1xGuestVlanId based on Integer32"""
    defaultValue = 0


_FlWorkFWCtrlSecurityDot1xGuestVlanId_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityDot1xGuestVlanId_Object = MibTableColumn
flWorkFWCtrlSecurityDot1xGuestVlanId = _FlWorkFWCtrlSecurityDot1xGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 1, 1, 1),
    _FlWorkFWCtrlSecurityDot1xGuestVlanId_Type()
)
flWorkFWCtrlSecurityDot1xGuestVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityDot1xGuestVlanId.setStatus("current")


class _FlWorkFWCtrlSecurityDot1xAssignTimeout_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityDot1xAssignTimeout based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlWorkFWCtrlSecurityDot1xAssignTimeout_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityDot1xAssignTimeout_Object = MibTableColumn
flWorkFWCtrlSecurityDot1xAssignTimeout = _FlWorkFWCtrlSecurityDot1xAssignTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 1, 1, 2),
    _FlWorkFWCtrlSecurityDot1xAssignTimeout_Type()
)
flWorkFWCtrlSecurityDot1xAssignTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityDot1xAssignTimeout.setStatus("current")


class _FlWorkFWCtrlSecurityDot1xVlanAssign_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityDot1xVlanAssign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkFWCtrlSecurityDot1xVlanAssign_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityDot1xVlanAssign_Object = MibScalar
flWorkFWCtrlSecurityDot1xVlanAssign = _FlWorkFWCtrlSecurityDot1xVlanAssign_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 2),
    _FlWorkFWCtrlSecurityDot1xVlanAssign_Type()
)
flWorkFWCtrlSecurityDot1xVlanAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityDot1xVlanAssign.setStatus("current")
_FlWorkFWCtrlSecurityRadiusAuthServTable_Object = MibTable
flWorkFWCtrlSecurityRadiusAuthServTable = _FlWorkFWCtrlSecurityRadiusAuthServTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 3)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityRadiusAuthServTable.setStatus("current")
_FlWorkFWCtrlSecurityRadiusAuthServEntry_Object = MibTableRow
flWorkFWCtrlSecurityRadiusAuthServEntry = _FlWorkFWCtrlSecurityRadiusAuthServEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 3, 1)
)
flWorkFWCtrlSecurityRadiusAuthServEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlSecurityRadiusServIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityRadiusAuthServEntry.setStatus("current")


class _FlWorkFWCtrlSecurityRadiusServIndex_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityRadiusServIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlSecurityRadiusServIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityRadiusServIndex_Object = MibTableColumn
flWorkFWCtrlSecurityRadiusServIndex = _FlWorkFWCtrlSecurityRadiusServIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 3, 1, 1),
    _FlWorkFWCtrlSecurityRadiusServIndex_Type()
)
flWorkFWCtrlSecurityRadiusServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityRadiusServIndex.setStatus("current")
_FlWorkFWCtrlSecurityRadiusServAddress_Type = IpAddress
_FlWorkFWCtrlSecurityRadiusServAddress_Object = MibTableColumn
flWorkFWCtrlSecurityRadiusServAddress = _FlWorkFWCtrlSecurityRadiusServAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 3, 1, 2),
    _FlWorkFWCtrlSecurityRadiusServAddress_Type()
)
flWorkFWCtrlSecurityRadiusServAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityRadiusServAddress.setStatus("current")


class _FlWorkFWCtrlSecurityRadiusServPort_Type(Integer32):
    """Custom type flWorkFWCtrlSecurityRadiusServPort based on Integer32"""
    defaultValue = 1812


_FlWorkFWCtrlSecurityRadiusServPort_Type.__name__ = "Integer32"
_FlWorkFWCtrlSecurityRadiusServPort_Object = MibTableColumn
flWorkFWCtrlSecurityRadiusServPort = _FlWorkFWCtrlSecurityRadiusServPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 3, 1, 3),
    _FlWorkFWCtrlSecurityRadiusServPort_Type()
)
flWorkFWCtrlSecurityRadiusServPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityRadiusServPort.setStatus("current")


class _FlWorkFWCtrlSecurityRadiusServSharedSecret_Type(OctetString):
    """Custom type flWorkFWCtrlSecurityRadiusServSharedSecret based on OctetString"""
    defaultValue = OctetString("2bchanged")


_FlWorkFWCtrlSecurityRadiusServSharedSecret_Type.__name__ = "OctetString"
_FlWorkFWCtrlSecurityRadiusServSharedSecret_Object = MibTableColumn
flWorkFWCtrlSecurityRadiusServSharedSecret = _FlWorkFWCtrlSecurityRadiusServSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 3, 1, 4),
    _FlWorkFWCtrlSecurityRadiusServSharedSecret_Type()
)
flWorkFWCtrlSecurityRadiusServSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityRadiusServSharedSecret.setStatus("current")


class _FlWorkFWCtrlSecurityRadiusServName_Type(DisplayString):
    """Custom type flWorkFWCtrlSecurityRadiusServName based on DisplayString"""
    defaultValue = OctetString("")


_FlWorkFWCtrlSecurityRadiusServName_Type.__name__ = "DisplayString"
_FlWorkFWCtrlSecurityRadiusServName_Object = MibTableColumn
flWorkFWCtrlSecurityRadiusServName = _FlWorkFWCtrlSecurityRadiusServName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 8, 3, 3, 1, 5),
    _FlWorkFWCtrlSecurityRadiusServName_Type()
)
flWorkFWCtrlSecurityRadiusServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlSecurityRadiusServName.setStatus("current")
_FlWorkFWCtrlProfinet_ObjectIdentity = ObjectIdentity
flWorkFWCtrlProfinet = _FlWorkFWCtrlProfinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9)
)
_FlWorkFWCtrlProfinetAlarm_ObjectIdentity = ObjectIdentity
flWorkFWCtrlProfinetAlarm = _FlWorkFWCtrlProfinetAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1)
)
_FlWorkFWCtrlProfinetAlarmPortTable_Object = MibTable
flWorkFWCtrlProfinetAlarmPortTable = _FlWorkFWCtrlProfinetAlarmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmPortTable.setStatus("current")
_FlWorkFWCtrlProfinetAlarmPortEntry_Object = MibTableRow
flWorkFWCtrlProfinetAlarmPortEntry = _FlWorkFWCtrlProfinetAlarmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 1, 1)
)
flWorkFWCtrlProfinetAlarmPortEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlProfinetAlarmPortIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmPortEntry.setStatus("current")


class _FlWorkFWCtrlProfinetAlarmPortIndex_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetAlarmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkFWCtrlProfinetAlarmPortIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetAlarmPortIndex_Object = MibTableColumn
flWorkFWCtrlProfinetAlarmPortIndex = _FlWorkFWCtrlProfinetAlarmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 1, 1, 1),
    _FlWorkFWCtrlProfinetAlarmPortIndex_Type()
)
flWorkFWCtrlProfinetAlarmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmPortIndex.setStatus("current")


class _FlWorkFWCtrlProfinetAlarmPortLinkMonitoring_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetAlarmPortLinkMonitoring based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlProfinetAlarmPortLinkMonitoring_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetAlarmPortLinkMonitoring_Object = MibTableColumn
flWorkFWCtrlProfinetAlarmPortLinkMonitoring = _FlWorkFWCtrlProfinetAlarmPortLinkMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 1, 1, 2),
    _FlWorkFWCtrlProfinetAlarmPortLinkMonitoring_Type()
)
flWorkFWCtrlProfinetAlarmPortLinkMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmPortLinkMonitoring.setStatus("current")


class _FlWorkFWCtrlProfinetAlarmPortPofScrjDiag_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetAlarmPortPofScrjDiag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlProfinetAlarmPortPofScrjDiag_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetAlarmPortPofScrjDiag_Object = MibTableColumn
flWorkFWCtrlProfinetAlarmPortPofScrjDiag = _FlWorkFWCtrlProfinetAlarmPortPofScrjDiag_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 1, 1, 3),
    _FlWorkFWCtrlProfinetAlarmPortPofScrjDiag_Type()
)
flWorkFWCtrlProfinetAlarmPortPofScrjDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmPortPofScrjDiag.setStatus("current")


class _FlWorkFWCtrlProfinetAlarmPortSFPMissing_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetAlarmPortSFPMissing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlProfinetAlarmPortSFPMissing_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetAlarmPortSFPMissing_Object = MibTableColumn
flWorkFWCtrlProfinetAlarmPortSFPMissing = _FlWorkFWCtrlProfinetAlarmPortSFPMissing_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 1, 1, 4),
    _FlWorkFWCtrlProfinetAlarmPortSFPMissing_Type()
)
flWorkFWCtrlProfinetAlarmPortSFPMissing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmPortSFPMissing.setStatus("current")


class _FlWorkFWCtrlProfinetAlarmPowerSupply_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetAlarmPowerSupply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlProfinetAlarmPowerSupply_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetAlarmPowerSupply_Object = MibScalar
flWorkFWCtrlProfinetAlarmPowerSupply = _FlWorkFWCtrlProfinetAlarmPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 10),
    _FlWorkFWCtrlProfinetAlarmPowerSupply_Type()
)
flWorkFWCtrlProfinetAlarmPowerSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmPowerSupply.setStatus("current")


class _FlWorkFWCtrlProfinetAlarmModuleRemove_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetAlarmModuleRemove based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlProfinetAlarmModuleRemove_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetAlarmModuleRemove_Object = MibScalar
flWorkFWCtrlProfinetAlarmModuleRemove = _FlWorkFWCtrlProfinetAlarmModuleRemove_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 11),
    _FlWorkFWCtrlProfinetAlarmModuleRemove_Type()
)
flWorkFWCtrlProfinetAlarmModuleRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmModuleRemove.setStatus("current")


class _FlWorkFWCtrlProfinetAlarmPlugableMemory_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetAlarmPlugableMemory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlProfinetAlarmPlugableMemory_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetAlarmPlugableMemory_Object = MibScalar
flWorkFWCtrlProfinetAlarmPlugableMemory = _FlWorkFWCtrlProfinetAlarmPlugableMemory_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 12),
    _FlWorkFWCtrlProfinetAlarmPlugableMemory_Type()
)
flWorkFWCtrlProfinetAlarmPlugableMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmPlugableMemory.setStatus("current")


class _FlWorkFWCtrlProfinetAlarmMRPRingFailure_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetAlarmMRPRingFailure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlProfinetAlarmMRPRingFailure_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetAlarmMRPRingFailure_Object = MibScalar
flWorkFWCtrlProfinetAlarmMRPRingFailure = _FlWorkFWCtrlProfinetAlarmMRPRingFailure_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 1, 20),
    _FlWorkFWCtrlProfinetAlarmMRPRingFailure_Type()
)
flWorkFWCtrlProfinetAlarmMRPRingFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetAlarmMRPRingFailure.setStatus("current")
_FlWorkFWCtrlProfinetStatus_ObjectIdentity = ObjectIdentity
flWorkFWCtrlProfinetStatus = _FlWorkFWCtrlProfinetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 2)
)
_FlWorkFWCtrlProfinetStatusActiveARs_Type = Integer32
_FlWorkFWCtrlProfinetStatusActiveARs_Object = MibScalar
flWorkFWCtrlProfinetStatusActiveARs = _FlWorkFWCtrlProfinetStatusActiveARs_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 2, 1),
    _FlWorkFWCtrlProfinetStatusActiveARs_Type()
)
flWorkFWCtrlProfinetStatusActiveARs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetStatusActiveARs.setStatus("current")
_FlWorkFWCtrlProfinetStatusConReqCount_Type = Integer32
_FlWorkFWCtrlProfinetStatusConReqCount_Object = MibScalar
flWorkFWCtrlProfinetStatusConReqCount = _FlWorkFWCtrlProfinetStatusConReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 2, 2),
    _FlWorkFWCtrlProfinetStatusConReqCount_Type()
)
flWorkFWCtrlProfinetStatusConReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetStatusConReqCount.setStatus("current")


class _FlWorkFWCtrlProfinetStatusDiagStatus_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetStatusDiagStatus based on Integer32"""
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
        *(("inactive", 0),
          ("good", 1),
          ("maintenanceRequired", 2),
          ("maintenanceDemanded", 3),
          ("diagnosis", 4))
    )


_FlWorkFWCtrlProfinetStatusDiagStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetStatusDiagStatus_Object = MibScalar
flWorkFWCtrlProfinetStatusDiagStatus = _FlWorkFWCtrlProfinetStatusDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 2, 3),
    _FlWorkFWCtrlProfinetStatusDiagStatus_Type()
)
flWorkFWCtrlProfinetStatusDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetStatusDiagStatus.setStatus("current")
_FlWorkFWCtrlProfinetBoundarySettings_ObjectIdentity = ObjectIdentity
flWorkFWCtrlProfinetBoundarySettings = _FlWorkFWCtrlProfinetBoundarySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 3)
)
_FlWorkFWCtrlProfinetBoundarySettingsTable_Object = MibTable
flWorkFWCtrlProfinetBoundarySettingsTable = _FlWorkFWCtrlProfinetBoundarySettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 3, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetBoundarySettingsTable.setStatus("current")
_FlWorkFWCtrlProfinetBoundarySettingsEntry_Object = MibTableRow
flWorkFWCtrlProfinetBoundarySettingsEntry = _FlWorkFWCtrlProfinetBoundarySettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 3, 1, 1)
)
flWorkFWCtrlProfinetBoundarySettingsEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlProfinetBoundarySettingsPortIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetBoundarySettingsEntry.setStatus("current")


class _FlWorkFWCtrlProfinetBoundarySettingsPortIndex_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetBoundarySettingsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkFWCtrlProfinetBoundarySettingsPortIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetBoundarySettingsPortIndex_Object = MibTableColumn
flWorkFWCtrlProfinetBoundarySettingsPortIndex = _FlWorkFWCtrlProfinetBoundarySettingsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 3, 1, 1, 1),
    _FlWorkFWCtrlProfinetBoundarySettingsPortIndex_Type()
)
flWorkFWCtrlProfinetBoundarySettingsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetBoundarySettingsPortIndex.setStatus("current")


class _FlWorkFWCtrlProfinetBoundarySettingsDcpIdentify_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetBoundarySettingsDcpIdentify based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_FlWorkFWCtrlProfinetBoundarySettingsDcpIdentify_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetBoundarySettingsDcpIdentify_Object = MibTableColumn
flWorkFWCtrlProfinetBoundarySettingsDcpIdentify = _FlWorkFWCtrlProfinetBoundarySettingsDcpIdentify_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 3, 1, 1, 2),
    _FlWorkFWCtrlProfinetBoundarySettingsDcpIdentify_Type()
)
flWorkFWCtrlProfinetBoundarySettingsDcpIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetBoundarySettingsDcpIdentify.setStatus("current")


class _FlWorkFWCtrlProfinetBoundarySettingsDcpHello_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetBoundarySettingsDcpHello based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_FlWorkFWCtrlProfinetBoundarySettingsDcpHello_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetBoundarySettingsDcpHello_Object = MibTableColumn
flWorkFWCtrlProfinetBoundarySettingsDcpHello = _FlWorkFWCtrlProfinetBoundarySettingsDcpHello_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 3, 1, 1, 3),
    _FlWorkFWCtrlProfinetBoundarySettingsDcpHello_Type()
)
flWorkFWCtrlProfinetBoundarySettingsDcpHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetBoundarySettingsDcpHello.setStatus("current")


class _FlWorkFWCtrlProfinetBoundarySettingsLLDP_Type(Integer32):
    """Custom type flWorkFWCtrlProfinetBoundarySettingsLLDP based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_FlWorkFWCtrlProfinetBoundarySettingsLLDP_Type.__name__ = "Integer32"
_FlWorkFWCtrlProfinetBoundarySettingsLLDP_Object = MibTableColumn
flWorkFWCtrlProfinetBoundarySettingsLLDP = _FlWorkFWCtrlProfinetBoundarySettingsLLDP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 9, 3, 1, 1, 4),
    _FlWorkFWCtrlProfinetBoundarySettingsLLDP_Type()
)
flWorkFWCtrlProfinetBoundarySettingsLLDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlProfinetBoundarySettingsLLDP.setStatus("current")
_FlWorkFWCtrlMRP_ObjectIdentity = ObjectIdentity
flWorkFWCtrlMRP = _FlWorkFWCtrlMRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10)
)
_FlWorkFWCtrlMRPConfig_ObjectIdentity = ObjectIdentity
flWorkFWCtrlMRPConfig = _FlWorkFWCtrlMRPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1)
)
_FlWorkFWCtrlMRPConfigDomainTable_Object = MibTable
flWorkFWCtrlMRPConfigDomainTable = _FlWorkFWCtrlMRPConfigDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainTable.setStatus("current")
_FlWorkFWCtrlMRPConfigDomainEntry_Object = MibTableRow
flWorkFWCtrlMRPConfigDomainEntry = _FlWorkFWCtrlMRPConfigDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1)
)
flWorkFWCtrlMRPConfigDomainEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlMRPConfigDomainIdx"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainEntry.setStatus("current")


class _FlWorkFWCtrlMRPConfigDomainIdx_Type(Integer32):
    """Custom type flWorkFWCtrlMRPConfigDomainIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlMRPConfigDomainIdx_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPConfigDomainIdx_Object = MibTableColumn
flWorkFWCtrlMRPConfigDomainIdx = _FlWorkFWCtrlMRPConfigDomainIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1, 1),
    _FlWorkFWCtrlMRPConfigDomainIdx_Type()
)
flWorkFWCtrlMRPConfigDomainIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainIdx.setStatus("current")


class _FlWorkFWCtrlMRPConfigDomainUdid_Type(OctetString):
    """Custom type flWorkFWCtrlMRPConfigDomainUdid based on OctetString"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_FlWorkFWCtrlMRPConfigDomainUdid_Type.__name__ = "OctetString"
_FlWorkFWCtrlMRPConfigDomainUdid_Object = MibTableColumn
flWorkFWCtrlMRPConfigDomainUdid = _FlWorkFWCtrlMRPConfigDomainUdid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1, 2),
    _FlWorkFWCtrlMRPConfigDomainUdid_Type()
)
flWorkFWCtrlMRPConfigDomainUdid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainUdid.setStatus("current")


class _FlWorkFWCtrlMRPConfigDomainName_Type(OctetString):
    """Custom type flWorkFWCtrlMRPConfigDomainName based on OctetString"""
    defaultValue = OctetString("MRP-DOMAIN")


_FlWorkFWCtrlMRPConfigDomainName_Type.__name__ = "OctetString"
_FlWorkFWCtrlMRPConfigDomainName_Object = MibTableColumn
flWorkFWCtrlMRPConfigDomainName = _FlWorkFWCtrlMRPConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1, 3),
    _FlWorkFWCtrlMRPConfigDomainName_Type()
)
flWorkFWCtrlMRPConfigDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainName.setStatus("current")


class _FlWorkFWCtrlMRPConfigDomainRole_Type(Integer32):
    """Custom type flWorkFWCtrlMRPConfigDomainRole based on Integer32"""
    defaultValue = 0

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
        *(("disable", 0),
          ("client", 1),
          ("manager", 2),
          ("delete", 3),
          ("create", 4))
    )


_FlWorkFWCtrlMRPConfigDomainRole_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPConfigDomainRole_Object = MibTableColumn
flWorkFWCtrlMRPConfigDomainRole = _FlWorkFWCtrlMRPConfigDomainRole_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1, 4),
    _FlWorkFWCtrlMRPConfigDomainRole_Type()
)
flWorkFWCtrlMRPConfigDomainRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainRole.setStatus("current")


class _FlWorkFWCtrlMRPConfigDomainManagerPriority_Type(Integer32):
    """Custom type flWorkFWCtrlMRPConfigDomainManagerPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlWorkFWCtrlMRPConfigDomainManagerPriority_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPConfigDomainManagerPriority_Object = MibTableColumn
flWorkFWCtrlMRPConfigDomainManagerPriority = _FlWorkFWCtrlMRPConfigDomainManagerPriority_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1, 5),
    _FlWorkFWCtrlMRPConfigDomainManagerPriority_Type()
)
flWorkFWCtrlMRPConfigDomainManagerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainManagerPriority.setStatus("current")


class _FlWorkFWCtrlMRPConfigDomainVlanID_Type(Integer32):
    """Custom type flWorkFWCtrlMRPConfigDomainVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_FlWorkFWCtrlMRPConfigDomainVlanID_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPConfigDomainVlanID_Object = MibTableColumn
flWorkFWCtrlMRPConfigDomainVlanID = _FlWorkFWCtrlMRPConfigDomainVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1, 6),
    _FlWorkFWCtrlMRPConfigDomainVlanID_Type()
)
flWorkFWCtrlMRPConfigDomainVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainVlanID.setStatus("current")


class _FlWorkFWCtrlMRPConfigDomainRingPort1_Type(Integer32):
    """Custom type flWorkFWCtrlMRPConfigDomainRingPort1 based on Integer32"""
    defaultValue = 1


_FlWorkFWCtrlMRPConfigDomainRingPort1_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPConfigDomainRingPort1_Object = MibTableColumn
flWorkFWCtrlMRPConfigDomainRingPort1 = _FlWorkFWCtrlMRPConfigDomainRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1, 7),
    _FlWorkFWCtrlMRPConfigDomainRingPort1_Type()
)
flWorkFWCtrlMRPConfigDomainRingPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainRingPort1.setStatus("current")


class _FlWorkFWCtrlMRPConfigDomainRingPort2_Type(Integer32):
    """Custom type flWorkFWCtrlMRPConfigDomainRingPort2 based on Integer32"""
    defaultValue = 2


_FlWorkFWCtrlMRPConfigDomainRingPort2_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPConfigDomainRingPort2_Object = MibTableColumn
flWorkFWCtrlMRPConfigDomainRingPort2 = _FlWorkFWCtrlMRPConfigDomainRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1, 8),
    _FlWorkFWCtrlMRPConfigDomainRingPort2_Type()
)
flWorkFWCtrlMRPConfigDomainRingPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainRingPort2.setStatus("current")


class _FlWorkFWCtrlMRPConfigDomainResetRoundTripDelays_Type(Integer32):
    """Custom type flWorkFWCtrlMRPConfigDomainResetRoundTripDelays based on Integer32"""
    defaultValue = 1


_FlWorkFWCtrlMRPConfigDomainResetRoundTripDelays_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPConfigDomainResetRoundTripDelays_Object = MibTableColumn
flWorkFWCtrlMRPConfigDomainResetRoundTripDelays = _FlWorkFWCtrlMRPConfigDomainResetRoundTripDelays_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 1, 1, 1, 9),
    _FlWorkFWCtrlMRPConfigDomainResetRoundTripDelays_Type()
)
flWorkFWCtrlMRPConfigDomainResetRoundTripDelays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPConfigDomainResetRoundTripDelays.setStatus("current")
_FlWorkFWCtrlMRPInfo_ObjectIdentity = ObjectIdentity
flWorkFWCtrlMRPInfo = _FlWorkFWCtrlMRPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2)
)
_FlWorkFWCtrlMRPInfoDomainTable_Object = MibTable
flWorkFWCtrlMRPInfoDomainTable = _FlWorkFWCtrlMRPInfoDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainTable.setStatus("current")
_FlWorkFWCtrlMRPInfoDomainEntry_Object = MibTableRow
flWorkFWCtrlMRPInfoDomainEntry = _FlWorkFWCtrlMRPInfoDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1)
)
flWorkFWCtrlMRPInfoDomainEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlMRPInfoDomainIdx"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainEntry.setStatus("current")


class _FlWorkFWCtrlMRPInfoDomainIdx_Type(Integer32):
    """Custom type flWorkFWCtrlMRPInfoDomainIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlMRPInfoDomainIdx_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPInfoDomainIdx_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainIdx = _FlWorkFWCtrlMRPInfoDomainIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 1),
    _FlWorkFWCtrlMRPInfoDomainIdx_Type()
)
flWorkFWCtrlMRPInfoDomainIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainIdx.setStatus("current")
_FlWorkFWCtrlMRPInfoDomainUuid_Type = OctetString
_FlWorkFWCtrlMRPInfoDomainUuid_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainUuid = _FlWorkFWCtrlMRPInfoDomainUuid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 2),
    _FlWorkFWCtrlMRPInfoDomainUuid_Type()
)
flWorkFWCtrlMRPInfoDomainUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainUuid.setStatus("current")
_FlWorkFWCtrlMRPInfoDomainName_Type = OctetString
_FlWorkFWCtrlMRPInfoDomainName_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainName = _FlWorkFWCtrlMRPInfoDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 3),
    _FlWorkFWCtrlMRPInfoDomainName_Type()
)
flWorkFWCtrlMRPInfoDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainName.setStatus("current")


class _FlWorkFWCtrlMRPInfoDomainAdminRole_Type(Integer32):
    """Custom type flWorkFWCtrlMRPInfoDomainAdminRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("client", 1),
          ("manager", 2))
    )


_FlWorkFWCtrlMRPInfoDomainAdminRole_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPInfoDomainAdminRole_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainAdminRole = _FlWorkFWCtrlMRPInfoDomainAdminRole_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 4),
    _FlWorkFWCtrlMRPInfoDomainAdminRole_Type()
)
flWorkFWCtrlMRPInfoDomainAdminRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainAdminRole.setStatus("current")


class _FlWorkFWCtrlMRPInfoDomainOperRole_Type(Integer32):
    """Custom type flWorkFWCtrlMRPInfoDomainOperRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("client", 1),
          ("manager", 2))
    )


_FlWorkFWCtrlMRPInfoDomainOperRole_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPInfoDomainOperRole_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainOperRole = _FlWorkFWCtrlMRPInfoDomainOperRole_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 5),
    _FlWorkFWCtrlMRPInfoDomainOperRole_Type()
)
flWorkFWCtrlMRPInfoDomainOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainOperRole.setStatus("current")


class _FlWorkFWCtrlMRPInfoDomainManagerPriority_Type(Integer32):
    """Custom type flWorkFWCtrlMRPInfoDomainManagerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlWorkFWCtrlMRPInfoDomainManagerPriority_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPInfoDomainManagerPriority_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainManagerPriority = _FlWorkFWCtrlMRPInfoDomainManagerPriority_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 6),
    _FlWorkFWCtrlMRPInfoDomainManagerPriority_Type()
)
flWorkFWCtrlMRPInfoDomainManagerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainManagerPriority.setStatus("current")
_FlWorkFWCtrlMRPInfoDomainRingPort1_Type = Integer32
_FlWorkFWCtrlMRPInfoDomainRingPort1_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainRingPort1 = _FlWorkFWCtrlMRPInfoDomainRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 7),
    _FlWorkFWCtrlMRPInfoDomainRingPort1_Type()
)
flWorkFWCtrlMRPInfoDomainRingPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainRingPort1.setStatus("current")


class _FlWorkFWCtrlMRPInfoDomainRingPort1State_Type(Integer32):
    """Custom type flWorkFWCtrlMRPInfoDomainRingPort1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("blocked", 2),
          ("forwarding", 3))
    )


_FlWorkFWCtrlMRPInfoDomainRingPort1State_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPInfoDomainRingPort1State_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainRingPort1State = _FlWorkFWCtrlMRPInfoDomainRingPort1State_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 8),
    _FlWorkFWCtrlMRPInfoDomainRingPort1State_Type()
)
flWorkFWCtrlMRPInfoDomainRingPort1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainRingPort1State.setStatus("current")
_FlWorkFWCtrlMRPInfoDomainRingPort2_Type = Integer32
_FlWorkFWCtrlMRPInfoDomainRingPort2_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainRingPort2 = _FlWorkFWCtrlMRPInfoDomainRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 9),
    _FlWorkFWCtrlMRPInfoDomainRingPort2_Type()
)
flWorkFWCtrlMRPInfoDomainRingPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainRingPort2.setStatus("current")


class _FlWorkFWCtrlMRPInfoDomainRingPort2State_Type(Integer32):
    """Custom type flWorkFWCtrlMRPInfoDomainRingPort2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("blocked", 2),
          ("forwarding", 3))
    )


_FlWorkFWCtrlMRPInfoDomainRingPort2State_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPInfoDomainRingPort2State_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainRingPort2State = _FlWorkFWCtrlMRPInfoDomainRingPort2State_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 10),
    _FlWorkFWCtrlMRPInfoDomainRingPort2State_Type()
)
flWorkFWCtrlMRPInfoDomainRingPort2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainRingPort2State.setStatus("current")


class _FlWorkFWCtrlMRPInfoDomainState_Type(Integer32):
    """Custom type flWorkFWCtrlMRPInfoDomainState based on Integer32"""
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
        *(("disabled", 0),
          ("invalid", 1),
          ("ringClosed", 2),
          ("ringOpen", 3),
          ("rtOK", 4),
          ("rtLost", 5))
    )


_FlWorkFWCtrlMRPInfoDomainState_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPInfoDomainState_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainState = _FlWorkFWCtrlMRPInfoDomainState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 11),
    _FlWorkFWCtrlMRPInfoDomainState_Type()
)
flWorkFWCtrlMRPInfoDomainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainState.setStatus("current")


class _FlWorkFWCtrlMRPInfoDomainError_Type(Integer32):
    """Custom type flWorkFWCtrlMRPInfoDomainError based on Integer32"""
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
        *(("noError", 0),
          ("invalid", 1),
          ("multipleMRM", 2),
          ("singleSideReceive", 3))
    )


_FlWorkFWCtrlMRPInfoDomainError_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPInfoDomainError_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainError = _FlWorkFWCtrlMRPInfoDomainError_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 12),
    _FlWorkFWCtrlMRPInfoDomainError_Type()
)
flWorkFWCtrlMRPInfoDomainError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainError.setStatus("current")
_FlWorkFWCtrlMRPInfoDomainRingOpenCount_Type = Integer32
_FlWorkFWCtrlMRPInfoDomainRingOpenCount_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainRingOpenCount = _FlWorkFWCtrlMRPInfoDomainRingOpenCount_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 13),
    _FlWorkFWCtrlMRPInfoDomainRingOpenCount_Type()
)
flWorkFWCtrlMRPInfoDomainRingOpenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainRingOpenCount.setStatus("current")
_FlWorkFWCtrlMRPInfoDomainLastRingOpenChange_Type = TimeTicks
_FlWorkFWCtrlMRPInfoDomainLastRingOpenChange_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainLastRingOpenChange = _FlWorkFWCtrlMRPInfoDomainLastRingOpenChange_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 14),
    _FlWorkFWCtrlMRPInfoDomainLastRingOpenChange_Type()
)
flWorkFWCtrlMRPInfoDomainLastRingOpenChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainLastRingOpenChange.setStatus("current")
_FlWorkFWCtrlMRPInfoDomainRoundTripDelayMax_Type = Integer32
_FlWorkFWCtrlMRPInfoDomainRoundTripDelayMax_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainRoundTripDelayMax = _FlWorkFWCtrlMRPInfoDomainRoundTripDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 15),
    _FlWorkFWCtrlMRPInfoDomainRoundTripDelayMax_Type()
)
flWorkFWCtrlMRPInfoDomainRoundTripDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainRoundTripDelayMax.setStatus("current")
_FlWorkFWCtrlMRPInfoDomainRoundTripDelayMin_Type = Integer32
_FlWorkFWCtrlMRPInfoDomainRoundTripDelayMin_Object = MibTableColumn
flWorkFWCtrlMRPInfoDomainRoundTripDelayMin = _FlWorkFWCtrlMRPInfoDomainRoundTripDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 1, 1, 16),
    _FlWorkFWCtrlMRPInfoDomainRoundTripDelayMin_Type()
)
flWorkFWCtrlMRPInfoDomainRoundTripDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDomainRoundTripDelayMin.setStatus("current")


class _FlWorkFWCtrlMRPInfoDeviceBlockingSupport_Type(Integer32):
    """Custom type flWorkFWCtrlMRPInfoDeviceBlockingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-blocking", 1),
          ("blocking", 2))
    )


_FlWorkFWCtrlMRPInfoDeviceBlockingSupport_Type.__name__ = "Integer32"
_FlWorkFWCtrlMRPInfoDeviceBlockingSupport_Object = MibScalar
flWorkFWCtrlMRPInfoDeviceBlockingSupport = _FlWorkFWCtrlMRPInfoDeviceBlockingSupport_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 10, 2, 2),
    _FlWorkFWCtrlMRPInfoDeviceBlockingSupport_Type()
)
flWorkFWCtrlMRPInfoDeviceBlockingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMRPInfoDeviceBlockingSupport.setStatus("current")
_FlWorkFWCtrlTemp_ObjectIdentity = ObjectIdentity
flWorkFWCtrlTemp = _FlWorkFWCtrlTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 11)
)
_FlWorkFWCtrlActualDeviceTemperature_Type = Integer32
_FlWorkFWCtrlActualDeviceTemperature_Object = MibScalar
flWorkFWCtrlActualDeviceTemperature = _FlWorkFWCtrlActualDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 11, 1),
    _FlWorkFWCtrlActualDeviceTemperature_Type()
)
flWorkFWCtrlActualDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlActualDeviceTemperature.setStatus("current")
_FlWorkFWCtrlMinOperTemperature_Type = Integer32
_FlWorkFWCtrlMinOperTemperature_Object = MibScalar
flWorkFWCtrlMinOperTemperature = _FlWorkFWCtrlMinOperTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 11, 2),
    _FlWorkFWCtrlMinOperTemperature_Type()
)
flWorkFWCtrlMinOperTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMinOperTemperature.setStatus("current")
_FlWorkFWCtrlMaxOperTemperature_Type = Integer32
_FlWorkFWCtrlMaxOperTemperature_Object = MibScalar
flWorkFWCtrlMaxOperTemperature = _FlWorkFWCtrlMaxOperTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 11, 3),
    _FlWorkFWCtrlMaxOperTemperature_Type()
)
flWorkFWCtrlMaxOperTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlMaxOperTemperature.setStatus("current")
_FlWorkFWCtrlUserTempWarningThreshold_Type = Integer32
_FlWorkFWCtrlUserTempWarningThreshold_Object = MibScalar
flWorkFWCtrlUserTempWarningThreshold = _FlWorkFWCtrlUserTempWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 11, 4),
    _FlWorkFWCtrlUserTempWarningThreshold_Type()
)
flWorkFWCtrlUserTempWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserTempWarningThreshold.setStatus("current")


class _FlWorkFWCtrlTempShutdownPrevention_Type(Integer32):
    """Custom type flWorkFWCtrlTempShutdownPrevention based on Integer32"""
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


_FlWorkFWCtrlTempShutdownPrevention_Type.__name__ = "Integer32"
_FlWorkFWCtrlTempShutdownPrevention_Object = MibScalar
flWorkFWCtrlTempShutdownPrevention = _FlWorkFWCtrlTempShutdownPrevention_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 11, 5),
    _FlWorkFWCtrlTempShutdownPrevention_Type()
)
flWorkFWCtrlTempShutdownPrevention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTempShutdownPrevention.setStatus("current")
_FlWorkFWCtrlTelnetGroup_ObjectIdentity = ObjectIdentity
flWorkFWCtrlTelnetGroup = _FlWorkFWCtrlTelnetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 12)
)


class _FlWorkFWCtrlTelnetLoginTimeout_Type(Integer32):
    """Custom type flWorkFWCtrlTelnetLoginTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_FlWorkFWCtrlTelnetLoginTimeout_Type.__name__ = "Integer32"
_FlWorkFWCtrlTelnetLoginTimeout_Object = MibScalar
flWorkFWCtrlTelnetLoginTimeout = _FlWorkFWCtrlTelnetLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 12, 1),
    _FlWorkFWCtrlTelnetLoginTimeout_Type()
)
flWorkFWCtrlTelnetLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTelnetLoginTimeout.setStatus("current")


class _FlWorkFWCtrlTelnetMaxSessions_Type(Integer32):
    """Custom type flWorkFWCtrlTelnetMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_FlWorkFWCtrlTelnetMaxSessions_Type.__name__ = "Integer32"
_FlWorkFWCtrlTelnetMaxSessions_Object = MibScalar
flWorkFWCtrlTelnetMaxSessions = _FlWorkFWCtrlTelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 12, 2),
    _FlWorkFWCtrlTelnetMaxSessions_Type()
)
flWorkFWCtrlTelnetMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTelnetMaxSessions.setStatus("current")


class _FlWorkFWCtrlTelnetAllowNewMode_Type(Integer32):
    """Custom type flWorkFWCtrlTelnetAllowNewMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkFWCtrlTelnetAllowNewMode_Type.__name__ = "Integer32"
_FlWorkFWCtrlTelnetAllowNewMode_Object = MibScalar
flWorkFWCtrlTelnetAllowNewMode = _FlWorkFWCtrlTelnetAllowNewMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 12, 3),
    _FlWorkFWCtrlTelnetAllowNewMode_Type()
)
flWorkFWCtrlTelnetAllowNewMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlTelnetAllowNewMode.setStatus("current")
_FlWorkFWCtrlImage_ObjectIdentity = ObjectIdentity
flWorkFWCtrlImage = _FlWorkFWCtrlImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 13)
)


class _FlWorkFWCtrlImage1_Type(DisplayString):
    """Custom type flWorkFWCtrlImage1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FlWorkFWCtrlImage1_Type.__name__ = "DisplayString"
_FlWorkFWCtrlImage1_Object = MibScalar
flWorkFWCtrlImage1 = _FlWorkFWCtrlImage1_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 13, 1),
    _FlWorkFWCtrlImage1_Type()
)
flWorkFWCtrlImage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlImage1.setStatus("current")


class _FlWorkFWCtrlImage2_Type(DisplayString):
    """Custom type flWorkFWCtrlImage2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FlWorkFWCtrlImage2_Type.__name__ = "DisplayString"
_FlWorkFWCtrlImage2_Object = MibScalar
flWorkFWCtrlImage2 = _FlWorkFWCtrlImage2_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 13, 2),
    _FlWorkFWCtrlImage2_Type()
)
flWorkFWCtrlImage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlImage2.setStatus("current")


class _FlWorkFWCtrlActiveImage_Type(DisplayString):
    """Custom type flWorkFWCtrlActiveImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FlWorkFWCtrlActiveImage_Type.__name__ = "DisplayString"
_FlWorkFWCtrlActiveImage_Object = MibScalar
flWorkFWCtrlActiveImage = _FlWorkFWCtrlActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 13, 3),
    _FlWorkFWCtrlActiveImage_Type()
)
flWorkFWCtrlActiveImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlActiveImage.setStatus("current")


class _FlWorkFWCtrlNextActiveImage_Type(DisplayString):
    """Custom type flWorkFWCtrlNextActiveImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FlWorkFWCtrlNextActiveImage_Type.__name__ = "DisplayString"
_FlWorkFWCtrlNextActiveImage_Object = MibScalar
flWorkFWCtrlNextActiveImage = _FlWorkFWCtrlNextActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 13, 4),
    _FlWorkFWCtrlNextActiveImage_Type()
)
flWorkFWCtrlNextActiveImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlNextActiveImage.setStatus("current")
_FlWorkFWCtrlUserConfigGroup_ObjectIdentity = ObjectIdentity
flWorkFWCtrlUserConfigGroup = _FlWorkFWCtrlUserConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14)
)


class _FlWorkFWCtrlUserConfigCreate_Type(DisplayString):
    """Custom type flWorkFWCtrlUserConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FlWorkFWCtrlUserConfigCreate_Type.__name__ = "DisplayString"
_FlWorkFWCtrlUserConfigCreate_Object = MibScalar
flWorkFWCtrlUserConfigCreate = _FlWorkFWCtrlUserConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 1),
    _FlWorkFWCtrlUserConfigCreate_Type()
)
flWorkFWCtrlUserConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserConfigCreate.setStatus("current")
_FlWorkFWCtrlUserConfigTable_Object = MibTable
flWorkFWCtrlUserConfigTable = _FlWorkFWCtrlUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlUserConfigTable.setStatus("current")
_FlWorkFWCtrlUserConfigEntry_Object = MibTableRow
flWorkFWCtrlUserConfigEntry = _FlWorkFWCtrlUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1)
)
flWorkFWCtrlUserConfigEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlUserIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlUserConfigEntry.setStatus("current")


class _FlWorkFWCtrlUserIndex_Type(Integer32):
    """Custom type flWorkFWCtrlUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlUserIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlUserIndex_Object = MibTableColumn
flWorkFWCtrlUserIndex = _FlWorkFWCtrlUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 1),
    _FlWorkFWCtrlUserIndex_Type()
)
flWorkFWCtrlUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserIndex.setStatus("current")


class _FlWorkFWCtrlUserName_Type(DisplayString):
    """Custom type flWorkFWCtrlUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FlWorkFWCtrlUserName_Type.__name__ = "DisplayString"
_FlWorkFWCtrlUserName_Object = MibTableColumn
flWorkFWCtrlUserName = _FlWorkFWCtrlUserName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 2),
    _FlWorkFWCtrlUserName_Type()
)
flWorkFWCtrlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserName.setStatus("current")


class _FlWorkFWCtrlUserPassword_Type(DisplayString):
    """Custom type flWorkFWCtrlUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_FlWorkFWCtrlUserPassword_Type.__name__ = "DisplayString"
_FlWorkFWCtrlUserPassword_Object = MibTableColumn
flWorkFWCtrlUserPassword = _FlWorkFWCtrlUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 3),
    _FlWorkFWCtrlUserPassword_Type()
)
flWorkFWCtrlUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserPassword.setStatus("current")


class _FlWorkFWCtrlUserAccessMode_Type(Integer32):
    """Custom type flWorkFWCtrlUserAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("write", 2))
    )


_FlWorkFWCtrlUserAccessMode_Type.__name__ = "Integer32"
_FlWorkFWCtrlUserAccessMode_Object = MibTableColumn
flWorkFWCtrlUserAccessMode = _FlWorkFWCtrlUserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 4),
    _FlWorkFWCtrlUserAccessMode_Type()
)
flWorkFWCtrlUserAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserAccessMode.setStatus("current")
_FlWorkFWCtrlUserStatus_Type = RowStatus
_FlWorkFWCtrlUserStatus_Object = MibTableColumn
flWorkFWCtrlUserStatus = _FlWorkFWCtrlUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 5),
    _FlWorkFWCtrlUserStatus_Type()
)
flWorkFWCtrlUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserStatus.setStatus("current")


class _FlWorkFWCtrlUserAuthenticationType_Type(Integer32):
    """Custom type flWorkFWCtrlUserAuthenticationType based on Integer32"""
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
          ("hmacmd5", 2),
          ("hmacsha", 3))
    )


_FlWorkFWCtrlUserAuthenticationType_Type.__name__ = "Integer32"
_FlWorkFWCtrlUserAuthenticationType_Object = MibTableColumn
flWorkFWCtrlUserAuthenticationType = _FlWorkFWCtrlUserAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 6),
    _FlWorkFWCtrlUserAuthenticationType_Type()
)
flWorkFWCtrlUserAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserAuthenticationType.setStatus("current")


class _FlWorkFWCtrlUserEncryptionType_Type(Integer32):
    """Custom type flWorkFWCtrlUserEncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("des", 2))
    )


_FlWorkFWCtrlUserEncryptionType_Type.__name__ = "Integer32"
_FlWorkFWCtrlUserEncryptionType_Object = MibTableColumn
flWorkFWCtrlUserEncryptionType = _FlWorkFWCtrlUserEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 7),
    _FlWorkFWCtrlUserEncryptionType_Type()
)
flWorkFWCtrlUserEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserEncryptionType.setStatus("current")


class _FlWorkFWCtrlUserEncryptionPassword_Type(DisplayString):
    """Custom type flWorkFWCtrlUserEncryptionPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_FlWorkFWCtrlUserEncryptionPassword_Type.__name__ = "DisplayString"
_FlWorkFWCtrlUserEncryptionPassword_Object = MibTableColumn
flWorkFWCtrlUserEncryptionPassword = _FlWorkFWCtrlUserEncryptionPassword_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 8),
    _FlWorkFWCtrlUserEncryptionPassword_Type()
)
flWorkFWCtrlUserEncryptionPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserEncryptionPassword.setStatus("current")


class _FlWorkFWCtrlUserLockoutStatus_Type(Integer32):
    """Custom type flWorkFWCtrlUserLockoutStatus based on Integer32"""
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


_FlWorkFWCtrlUserLockoutStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlUserLockoutStatus_Object = MibTableColumn
flWorkFWCtrlUserLockoutStatus = _FlWorkFWCtrlUserLockoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 9),
    _FlWorkFWCtrlUserLockoutStatus_Type()
)
flWorkFWCtrlUserLockoutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserLockoutStatus.setStatus("current")
_FlWorkFWCtrlUserPasswordExpireTime_Type = DateAndTime
_FlWorkFWCtrlUserPasswordExpireTime_Object = MibTableColumn
flWorkFWCtrlUserPasswordExpireTime = _FlWorkFWCtrlUserPasswordExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 14, 2, 1, 10),
    _FlWorkFWCtrlUserPasswordExpireTime_Type()
)
flWorkFWCtrlUserPasswordExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlUserPasswordExpireTime.setStatus("current")
_FlWorkFWCtrlDigitalInput_ObjectIdentity = ObjectIdentity
flWorkFWCtrlDigitalInput = _FlWorkFWCtrlDigitalInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 15)
)
_FlWorkFWCtrlDigitalInputTable_Object = MibTable
flWorkFWCtrlDigitalInputTable = _FlWorkFWCtrlDigitalInputTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 15, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalInputTable.setStatus("current")
_FlWorkFWCtrlDigitalInputEntry_Object = MibTableRow
flWorkFWCtrlDigitalInputEntry = _FlWorkFWCtrlDigitalInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 15, 1, 1)
)
flWorkFWCtrlDigitalInputEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDigitalInputIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalInputEntry.setStatus("current")


class _FlWorkFWCtrlDigitalInputIndex_Type(Integer32):
    """Custom type flWorkFWCtrlDigitalInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkFWCtrlDigitalInputIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlDigitalInputIndex_Object = MibTableColumn
flWorkFWCtrlDigitalInputIndex = _FlWorkFWCtrlDigitalInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 15, 1, 1, 1),
    _FlWorkFWCtrlDigitalInputIndex_Type()
)
flWorkFWCtrlDigitalInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalInputIndex.setStatus("current")


class _FlWorkFWCtrlDigitalInputStatus_Type(Integer32):
    """Custom type flWorkFWCtrlDigitalInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("unknown", 3))
    )


_FlWorkFWCtrlDigitalInputStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlDigitalInputStatus_Object = MibTableColumn
flWorkFWCtrlDigitalInputStatus = _FlWorkFWCtrlDigitalInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 15, 1, 1, 2),
    _FlWorkFWCtrlDigitalInputStatus_Type()
)
flWorkFWCtrlDigitalInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalInputStatus.setStatus("current")


class _FlWorkFWCtrlDigitalInputEvents_Type(Integer32):
    """Custom type flWorkFWCtrlDigitalInputEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wlan", 1),
          ("roam", 2))
    )


_FlWorkFWCtrlDigitalInputEvents_Type.__name__ = "Integer32"
_FlWorkFWCtrlDigitalInputEvents_Object = MibTableColumn
flWorkFWCtrlDigitalInputEvents = _FlWorkFWCtrlDigitalInputEvents_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 15, 1, 1, 3),
    _FlWorkFWCtrlDigitalInputEvents_Type()
)
flWorkFWCtrlDigitalInputEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalInputEvents.setStatus("current")
_FlWorkFWCtrlEnergy_ObjectIdentity = ObjectIdentity
flWorkFWCtrlEnergy = _FlWorkFWCtrlEnergy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 17)
)


class _FlWorkFWCtrlEnergyTest_Type(Integer32):
    """Custom type flWorkFWCtrlEnergyTest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlEnergyTest_Type.__name__ = "Integer32"
_FlWorkFWCtrlEnergyTest_Object = MibScalar
flWorkFWCtrlEnergyTest = _FlWorkFWCtrlEnergyTest_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 17, 1),
    _FlWorkFWCtrlEnergyTest_Type()
)
flWorkFWCtrlEnergyTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlEnergyTest.setStatus("current")
_FlWorkEnergyPortTable_Object = MibTable
flWorkEnergyPortTable = _FlWorkEnergyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 17, 2)
)
if mibBuilder.loadTexts:
    flWorkEnergyPortTable.setStatus("current")
_FlWorkEnergyPortEntry_Object = MibTableRow
flWorkEnergyPortEntry = _FlWorkEnergyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 17, 2, 1)
)
flWorkEnergyPortEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkEnergyPortIndex"),
)
if mibBuilder.loadTexts:
    flWorkEnergyPortEntry.setStatus("current")


class _FlWorkEnergyPortIndex_Type(Integer32):
    """Custom type flWorkEnergyPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkEnergyPortIndex_Type.__name__ = "Integer32"
_FlWorkEnergyPortIndex_Object = MibTableColumn
flWorkEnergyPortIndex = _FlWorkEnergyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 17, 2, 1, 1),
    _FlWorkEnergyPortIndex_Type()
)
flWorkEnergyPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkEnergyPortIndex.setStatus("current")


class _FlWorkEnergyPortModus_Type(Integer32):
    """Custom type flWorkEnergyPortModus based on Integer32"""
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
        *(("ignore", 1),
          ("switch-off", 2),
          ("slow-down", 3))
    )


_FlWorkEnergyPortModus_Type.__name__ = "Integer32"
_FlWorkEnergyPortModus_Object = MibTableColumn
flWorkEnergyPortModus = _FlWorkEnergyPortModus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 17, 2, 1, 2),
    _FlWorkEnergyPortModus_Type()
)
flWorkEnergyPortModus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkEnergyPortModus.setStatus("current")
_FlWorkFWCtrlDigitalOutput_ObjectIdentity = ObjectIdentity
flWorkFWCtrlDigitalOutput = _FlWorkFWCtrlDigitalOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 18)
)
_FlWorkFWCtrlDigitalOutputTable_Object = MibTable
flWorkFWCtrlDigitalOutputTable = _FlWorkFWCtrlDigitalOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 18, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalOutputTable.setStatus("current")
_FlWorkFWCtrlDigitalOutputEntry_Object = MibTableRow
flWorkFWCtrlDigitalOutputEntry = _FlWorkFWCtrlDigitalOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 18, 1, 1)
)
flWorkFWCtrlDigitalOutputEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDigitalOutputIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalOutputEntry.setStatus("current")


class _FlWorkFWCtrlDigitalOutputIndex_Type(Integer32):
    """Custom type flWorkFWCtrlDigitalOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkFWCtrlDigitalOutputIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlDigitalOutputIndex_Object = MibTableColumn
flWorkFWCtrlDigitalOutputIndex = _FlWorkFWCtrlDigitalOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 18, 1, 1, 1),
    _FlWorkFWCtrlDigitalOutputIndex_Type()
)
flWorkFWCtrlDigitalOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalOutputIndex.setStatus("current")


class _FlWorkFWCtrlDigitalOutputStatus_Type(Integer32):
    """Custom type flWorkFWCtrlDigitalOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("unknown", 3))
    )


_FlWorkFWCtrlDigitalOutputStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlDigitalOutputStatus_Object = MibTableColumn
flWorkFWCtrlDigitalOutputStatus = _FlWorkFWCtrlDigitalOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 18, 1, 1, 2),
    _FlWorkFWCtrlDigitalOutputStatus_Type()
)
flWorkFWCtrlDigitalOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalOutputStatus.setStatus("current")


class _FlWorkFWCtrlDigitalOutputEnable_Type(Integer32):
    """Custom type flWorkFWCtrlDigitalOutputEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlDigitalOutputEnable_Type.__name__ = "Integer32"
_FlWorkFWCtrlDigitalOutputEnable_Object = MibTableColumn
flWorkFWCtrlDigitalOutputEnable = _FlWorkFWCtrlDigitalOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 18, 1, 1, 3),
    _FlWorkFWCtrlDigitalOutputEnable_Type()
)
flWorkFWCtrlDigitalOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalOutputEnable.setStatus("current")


class _FlWorkFWCtrlDigitalOutputEventDigitalInState_Type(Integer32):
    """Custom type flWorkFWCtrlDigitalOutputEventDigitalInState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlDigitalOutputEventDigitalInState_Type.__name__ = "Integer32"
_FlWorkFWCtrlDigitalOutputEventDigitalInState_Object = MibTableColumn
flWorkFWCtrlDigitalOutputEventDigitalInState = _FlWorkFWCtrlDigitalOutputEventDigitalInState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 18, 1, 1, 4),
    _FlWorkFWCtrlDigitalOutputEventDigitalInState_Type()
)
flWorkFWCtrlDigitalOutputEventDigitalInState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalOutputEventDigitalInState.setStatus("current")


class _FlWorkFWCtrlDigitalOutputEventWlanState_Type(Integer32):
    """Custom type flWorkFWCtrlDigitalOutputEventWlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlDigitalOutputEventWlanState_Type.__name__ = "Integer32"
_FlWorkFWCtrlDigitalOutputEventWlanState_Object = MibTableColumn
flWorkFWCtrlDigitalOutputEventWlanState = _FlWorkFWCtrlDigitalOutputEventWlanState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 18, 1, 1, 5),
    _FlWorkFWCtrlDigitalOutputEventWlanState_Type()
)
flWorkFWCtrlDigitalOutputEventWlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalOutputEventWlanState.setStatus("current")


class _FlWorkFWCtrlDigitalOutputEventWlanConnection_Type(Integer32):
    """Custom type flWorkFWCtrlDigitalOutputEventWlanConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlDigitalOutputEventWlanConnection_Type.__name__ = "Integer32"
_FlWorkFWCtrlDigitalOutputEventWlanConnection_Object = MibTableColumn
flWorkFWCtrlDigitalOutputEventWlanConnection = _FlWorkFWCtrlDigitalOutputEventWlanConnection_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 18, 1, 1, 6),
    _FlWorkFWCtrlDigitalOutputEventWlanConnection_Type()
)
flWorkFWCtrlDigitalOutputEventWlanConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDigitalOutputEventWlanConnection.setStatus("current")
_FlWorkFWCtrlDLR_ObjectIdentity = ObjectIdentity
flWorkFWCtrlDLR = _FlWorkFWCtrlDLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19)
)
_FlWorkFWCtrlDLRDomainTable_Object = MibTable
flWorkFWCtrlDLRDomainTable = _FlWorkFWCtrlDLRDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRDomainTable.setStatus("current")
_FlWorkFWCtrlDLRDomainEntry_Object = MibTableRow
flWorkFWCtrlDLRDomainEntry = _FlWorkFWCtrlDLRDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1)
)
flWorkFWCtrlDLRDomainEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDLRDomainIdx"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRDomainEntry.setStatus("current")


class _FlWorkFWCtrlDLRDomainIdx_Type(Integer32):
    """Custom type flWorkFWCtrlDLRDomainIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlDLRDomainIdx_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRDomainIdx_Object = MibTableColumn
flWorkFWCtrlDLRDomainIdx = _FlWorkFWCtrlDLRDomainIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 1),
    _FlWorkFWCtrlDLRDomainIdx_Type()
)
flWorkFWCtrlDLRDomainIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRDomainIdx.setStatus("current")


class _FlWorkFWCtrlDLRMode_Type(Integer32):
    """Custom type flWorkFWCtrlDLRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("node", 2),
          ("supervisor", 3))
    )


_FlWorkFWCtrlDLRMode_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRMode_Object = MibTableColumn
flWorkFWCtrlDLRMode = _FlWorkFWCtrlDLRMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 2),
    _FlWorkFWCtrlDLRMode_Type()
)
flWorkFWCtrlDLRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRMode.setStatus("current")
_FlWorkFWCtrlDLRPort1_Type = Integer32
_FlWorkFWCtrlDLRPort1_Object = MibTableColumn
flWorkFWCtrlDLRPort1 = _FlWorkFWCtrlDLRPort1_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 3),
    _FlWorkFWCtrlDLRPort1_Type()
)
flWorkFWCtrlDLRPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRPort1.setStatus("current")
_FlWorkFWCtrlDLRPort2_Type = Integer32
_FlWorkFWCtrlDLRPort2_Object = MibTableColumn
flWorkFWCtrlDLRPort2 = _FlWorkFWCtrlDLRPort2_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 4),
    _FlWorkFWCtrlDLRPort2_Type()
)
flWorkFWCtrlDLRPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRPort2.setStatus("current")


class _FlWorkFWCtrlDLRBeaconInterval_Type(Integer32):
    """Custom type flWorkFWCtrlDLRBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 100000),
    )


_FlWorkFWCtrlDLRBeaconInterval_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRBeaconInterval_Object = MibTableColumn
flWorkFWCtrlDLRBeaconInterval = _FlWorkFWCtrlDLRBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 5),
    _FlWorkFWCtrlDLRBeaconInterval_Type()
)
flWorkFWCtrlDLRBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRBeaconInterval.setStatus("current")


class _FlWorkFWCtrlDLRBeaconTimeout_Type(Integer32):
    """Custom type flWorkFWCtrlDLRBeaconTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 500000),
    )


_FlWorkFWCtrlDLRBeaconTimeout_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRBeaconTimeout_Object = MibTableColumn
flWorkFWCtrlDLRBeaconTimeout = _FlWorkFWCtrlDLRBeaconTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 6),
    _FlWorkFWCtrlDLRBeaconTimeout_Type()
)
flWorkFWCtrlDLRBeaconTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRBeaconTimeout.setStatus("current")


class _FlWorkFWCtrlDLRSupervisorPrecedence_Type(Integer32):
    """Custom type flWorkFWCtrlDLRSupervisorPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkFWCtrlDLRSupervisorPrecedence_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRSupervisorPrecedence_Object = MibTableColumn
flWorkFWCtrlDLRSupervisorPrecedence = _FlWorkFWCtrlDLRSupervisorPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 7),
    _FlWorkFWCtrlDLRSupervisorPrecedence_Type()
)
flWorkFWCtrlDLRSupervisorPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRSupervisorPrecedence.setStatus("current")


class _FlWorkFWCtrlDLRVlanId_Type(Integer32):
    """Custom type flWorkFWCtrlDLRVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FlWorkFWCtrlDLRVlanId_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRVlanId_Object = MibTableColumn
flWorkFWCtrlDLRVlanId = _FlWorkFWCtrlDLRVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 8),
    _FlWorkFWCtrlDLRVlanId_Type()
)
flWorkFWCtrlDLRVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRVlanId.setStatus("current")


class _FlWorkFWCtrlDLRRingStatus_Type(Integer32):
    """Custom type flWorkFWCtrlDLRRingStatus based on Integer32"""
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
        *(("normal", 0),
          ("ringFault", 1),
          ("loopDetect", 2),
          ("partialFault", 3),
          ("rapidFault", 4))
    )


_FlWorkFWCtrlDLRRingStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRRingStatus_Object = MibTableColumn
flWorkFWCtrlDLRRingStatus = _FlWorkFWCtrlDLRRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 9),
    _FlWorkFWCtrlDLRRingStatus_Type()
)
flWorkFWCtrlDLRRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRRingStatus.setStatus("current")


class _FlWorkFWCtrlDLRDeviceStatus_Type(Integer32):
    """Custom type flWorkFWCtrlDLRDeviceStatus based on Integer32"""
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
        *(("backupSupervisor", 0),
          ("activeSupervisor", 1),
          ("node", 2),
          ("noRing", 3),
          ("fault", 4))
    )


_FlWorkFWCtrlDLRDeviceStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRDeviceStatus_Object = MibTableColumn
flWorkFWCtrlDLRDeviceStatus = _FlWorkFWCtrlDLRDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 10),
    _FlWorkFWCtrlDLRDeviceStatus_Type()
)
flWorkFWCtrlDLRDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRDeviceStatus.setStatus("current")
_FlWorkFWCtrlDLRRingFaultCounter_Type = Integer32
_FlWorkFWCtrlDLRRingFaultCounter_Object = MibTableColumn
flWorkFWCtrlDLRRingFaultCounter = _FlWorkFWCtrlDLRRingFaultCounter_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 11),
    _FlWorkFWCtrlDLRRingFaultCounter_Type()
)
flWorkFWCtrlDLRRingFaultCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRRingFaultCounter.setStatus("current")


class _FlWorkFWCtrlDLRRingFaultCntClear_Type(Integer32):
    """Custom type flWorkFWCtrlDLRRingFaultCntClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 1),
          ("clear", 2))
    )


_FlWorkFWCtrlDLRRingFaultCntClear_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRRingFaultCntClear_Object = MibTableColumn
flWorkFWCtrlDLRRingFaultCntClear = _FlWorkFWCtrlDLRRingFaultCntClear_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 12),
    _FlWorkFWCtrlDLRRingFaultCntClear_Type()
)
flWorkFWCtrlDLRRingFaultCntClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRRingFaultCntClear.setStatus("current")
_FlWorkFWCtrlDLRActiveSupervisorIP_Type = IpAddress
_FlWorkFWCtrlDLRActiveSupervisorIP_Object = MibTableColumn
flWorkFWCtrlDLRActiveSupervisorIP = _FlWorkFWCtrlDLRActiveSupervisorIP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 13),
    _FlWorkFWCtrlDLRActiveSupervisorIP_Type()
)
flWorkFWCtrlDLRActiveSupervisorIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRActiveSupervisorIP.setStatus("current")
_FlWorkFWCtrlDLRActiveSupervisorMAC_Type = MacAddress
_FlWorkFWCtrlDLRActiveSupervisorMAC_Object = MibTableColumn
flWorkFWCtrlDLRActiveSupervisorMAC = _FlWorkFWCtrlDLRActiveSupervisorMAC_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 14),
    _FlWorkFWCtrlDLRActiveSupervisorMAC_Type()
)
flWorkFWCtrlDLRActiveSupervisorMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRActiveSupervisorMAC.setStatus("current")
_FlWorkFWCtrlDLRLastNodePort1IP_Type = IpAddress
_FlWorkFWCtrlDLRLastNodePort1IP_Object = MibTableColumn
flWorkFWCtrlDLRLastNodePort1IP = _FlWorkFWCtrlDLRLastNodePort1IP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 15),
    _FlWorkFWCtrlDLRLastNodePort1IP_Type()
)
flWorkFWCtrlDLRLastNodePort1IP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRLastNodePort1IP.setStatus("current")
_FlWorkFWCtrlDLRLastNodePort1MAC_Type = MacAddress
_FlWorkFWCtrlDLRLastNodePort1MAC_Object = MibTableColumn
flWorkFWCtrlDLRLastNodePort1MAC = _FlWorkFWCtrlDLRLastNodePort1MAC_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 16),
    _FlWorkFWCtrlDLRLastNodePort1MAC_Type()
)
flWorkFWCtrlDLRLastNodePort1MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRLastNodePort1MAC.setStatus("current")
_FlWorkFWCtrlDLRLastNodePort2IP_Type = IpAddress
_FlWorkFWCtrlDLRLastNodePort2IP_Object = MibTableColumn
flWorkFWCtrlDLRLastNodePort2IP = _FlWorkFWCtrlDLRLastNodePort2IP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 17),
    _FlWorkFWCtrlDLRLastNodePort2IP_Type()
)
flWorkFWCtrlDLRLastNodePort2IP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRLastNodePort2IP.setStatus("current")
_FlWorkFWCtrlDLRLastNodePort2MAC_Type = MacAddress
_FlWorkFWCtrlDLRLastNodePort2MAC_Object = MibTableColumn
flWorkFWCtrlDLRLastNodePort2MAC = _FlWorkFWCtrlDLRLastNodePort2MAC_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 18),
    _FlWorkFWCtrlDLRLastNodePort2MAC_Type()
)
flWorkFWCtrlDLRLastNodePort2MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRLastNodePort2MAC.setStatus("current")


class _FlWorkFWCtrlDLRRapidFaultClear_Type(Integer32):
    """Custom type flWorkFWCtrlDLRRapidFaultClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 1),
          ("clear", 2))
    )


_FlWorkFWCtrlDLRRapidFaultClear_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRRapidFaultClear_Object = MibTableColumn
flWorkFWCtrlDLRRapidFaultClear = _FlWorkFWCtrlDLRRapidFaultClear_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 19),
    _FlWorkFWCtrlDLRRapidFaultClear_Type()
)
flWorkFWCtrlDLRRapidFaultClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRRapidFaultClear.setStatus("current")
_FlWorkFWCtrlDLRActivePrecedence_Type = Integer32
_FlWorkFWCtrlDLRActivePrecedence_Object = MibTableColumn
flWorkFWCtrlDLRActivePrecedence = _FlWorkFWCtrlDLRActivePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 20),
    _FlWorkFWCtrlDLRActivePrecedence_Type()
)
flWorkFWCtrlDLRActivePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRActivePrecedence.setStatus("current")


class _FlWorkFWCtrlDLRVerifyFaultLocation_Type(Integer32):
    """Custom type flWorkFWCtrlDLRVerifyFaultLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("start", 2))
    )


_FlWorkFWCtrlDLRVerifyFaultLocation_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRVerifyFaultLocation_Object = MibTableColumn
flWorkFWCtrlDLRVerifyFaultLocation = _FlWorkFWCtrlDLRVerifyFaultLocation_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 21),
    _FlWorkFWCtrlDLRVerifyFaultLocation_Type()
)
flWorkFWCtrlDLRVerifyFaultLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRVerifyFaultLocation.setStatus("current")


class _FlWorkFWCtrlDLRRestartSignOn_Type(Integer32):
    """Custom type flWorkFWCtrlDLRRestartSignOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("start", 2))
    )


_FlWorkFWCtrlDLRRestartSignOn_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRRestartSignOn_Object = MibTableColumn
flWorkFWCtrlDLRRestartSignOn = _FlWorkFWCtrlDLRRestartSignOn_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 1, 1, 22),
    _FlWorkFWCtrlDLRRestartSignOn_Type()
)
flWorkFWCtrlDLRRestartSignOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRRestartSignOn.setStatus("current")
_FlWorkFWCtrlDLRNodeTable_Object = MibTable
flWorkFWCtrlDLRNodeTable = _FlWorkFWCtrlDLRNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 2)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRNodeTable.setStatus("current")
_FlWorkFWCtrlDLRNodeEntry_Object = MibTableRow
flWorkFWCtrlDLRNodeEntry = _FlWorkFWCtrlDLRNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 2, 1)
)
flWorkFWCtrlDLRNodeEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDLRDomainIdx"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDLRNodeIdx"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRNodeEntry.setStatus("current")


class _FlWorkFWCtrlDLRNodeIdx_Type(Integer32):
    """Custom type flWorkFWCtrlDLRNodeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkFWCtrlDLRNodeIdx_Type.__name__ = "Integer32"
_FlWorkFWCtrlDLRNodeIdx_Object = MibTableColumn
flWorkFWCtrlDLRNodeIdx = _FlWorkFWCtrlDLRNodeIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 2, 1, 2),
    _FlWorkFWCtrlDLRNodeIdx_Type()
)
flWorkFWCtrlDLRNodeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRNodeIdx.setStatus("current")
_FlWorkFWCtrlDLRNodeIP_Type = IpAddress
_FlWorkFWCtrlDLRNodeIP_Object = MibTableColumn
flWorkFWCtrlDLRNodeIP = _FlWorkFWCtrlDLRNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 2, 1, 3),
    _FlWorkFWCtrlDLRNodeIP_Type()
)
flWorkFWCtrlDLRNodeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRNodeIP.setStatus("current")
_FlWorkFWCtrlDLRNodeMAC_Type = MacAddress
_FlWorkFWCtrlDLRNodeMAC_Object = MibTableColumn
flWorkFWCtrlDLRNodeMAC = _FlWorkFWCtrlDLRNodeMAC_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 19, 2, 1, 4),
    _FlWorkFWCtrlDLRNodeMAC_Type()
)
flWorkFWCtrlDLRNodeMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDLRNodeMAC.setStatus("current")
_FlWorkFWCtrlFileTransfer_ObjectIdentity = ObjectIdentity
flWorkFWCtrlFileTransfer = _FlWorkFWCtrlFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 22)
)
_FlWorkFWCtrlFileTransferTftpIPAddr_Type = IpAddress
_FlWorkFWCtrlFileTransferTftpIPAddr_Object = MibScalar
flWorkFWCtrlFileTransferTftpIPAddr = _FlWorkFWCtrlFileTransferTftpIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 22, 1),
    _FlWorkFWCtrlFileTransferTftpIPAddr_Type()
)
flWorkFWCtrlFileTransferTftpIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlFileTransferTftpIPAddr.setStatus("current")
_FlWorkFWCtrlFileTransferTftpVapID_Type = Integer32
_FlWorkFWCtrlFileTransferTftpVapID_Object = MibScalar
flWorkFWCtrlFileTransferTftpVapID = _FlWorkFWCtrlFileTransferTftpVapID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 22, 2),
    _FlWorkFWCtrlFileTransferTftpVapID_Type()
)
flWorkFWCtrlFileTransferTftpVapID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlFileTransferTftpVapID.setStatus("current")


class _FlWorkFWCtrlFileTransferTftpProfileID_Type(Integer32):
    """Custom type flWorkFWCtrlFileTransferTftpProfileID based on Integer32"""
    defaultValue = 1


_FlWorkFWCtrlFileTransferTftpProfileID_Type.__name__ = "Integer32"
_FlWorkFWCtrlFileTransferTftpProfileID_Object = MibScalar
flWorkFWCtrlFileTransferTftpProfileID = _FlWorkFWCtrlFileTransferTftpProfileID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 22, 3),
    _FlWorkFWCtrlFileTransferTftpProfileID_Type()
)
flWorkFWCtrlFileTransferTftpProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlFileTransferTftpProfileID.setStatus("current")


class _FlWorkFWCtrlFileTransferTftpFileType_Type(Integer32):
    """Custom type flWorkFWCtrlFileTransferTftpFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 2),
          ("sec-context", 3),
          ("radius-rootcert", 4),
          ("radius-clientcert", 5),
          ("snapshot", 6))
    )


_FlWorkFWCtrlFileTransferTftpFileType_Type.__name__ = "Integer32"
_FlWorkFWCtrlFileTransferTftpFileType_Object = MibScalar
flWorkFWCtrlFileTransferTftpFileType = _FlWorkFWCtrlFileTransferTftpFileType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 22, 4),
    _FlWorkFWCtrlFileTransferTftpFileType_Type()
)
flWorkFWCtrlFileTransferTftpFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlFileTransferTftpFileType.setStatus("current")


class _FlWorkFWCtrlFileTransferTftpFile_Type(OctetString):
    """Custom type flWorkFWCtrlFileTransferTftpFile based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FlWorkFWCtrlFileTransferTftpFile_Type.__name__ = "OctetString"
_FlWorkFWCtrlFileTransferTftpFile_Object = MibScalar
flWorkFWCtrlFileTransferTftpFile = _FlWorkFWCtrlFileTransferTftpFile_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 22, 5),
    _FlWorkFWCtrlFileTransferTftpFile_Type()
)
flWorkFWCtrlFileTransferTftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlFileTransferTftpFile.setStatus("current")


class _FlWorkFWCtrlFileTransferStatus_Type(Integer32):
    """Custom type flWorkFWCtrlFileTransferStatus based on Integer32"""
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
        *(("transferOk", 1),
          ("transferFault", 2),
          ("noTransfer", 3),
          ("unknown", 4),
          ("inProgress", 5))
    )


_FlWorkFWCtrlFileTransferStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlFileTransferStatus_Object = MibScalar
flWorkFWCtrlFileTransferStatus = _FlWorkFWCtrlFileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 22, 6),
    _FlWorkFWCtrlFileTransferStatus_Type()
)
flWorkFWCtrlFileTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlFileTransferStatus.setStatus("current")


class _FlWorkFWCtrlFileTransferExecute_Type(Integer32):
    """Custom type flWorkFWCtrlFileTransferExecute based on Integer32"""
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
        *(("noTransfer", 1),
          ("hostToDevice", 2),
          ("deviceToHost", 3))
    )


_FlWorkFWCtrlFileTransferExecute_Type.__name__ = "Integer32"
_FlWorkFWCtrlFileTransferExecute_Object = MibScalar
flWorkFWCtrlFileTransferExecute = _FlWorkFWCtrlFileTransferExecute_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 22, 7),
    _FlWorkFWCtrlFileTransferExecute_Type()
)
flWorkFWCtrlFileTransferExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlFileTransferExecute.setStatus("current")
_FlWorkFWCtrlDiag_ObjectIdentity = ObjectIdentity
flWorkFWCtrlDiag = _FlWorkFWCtrlDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23)
)
_FlWorkFWCtrlDiagSurveillance_ObjectIdentity = ObjectIdentity
flWorkFWCtrlDiagSurveillance = _FlWorkFWCtrlDiagSurveillance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 1)
)
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringTable_Object = MibTable
flWorkFWCtrlDiagSurveillanceCrcMonitoringTable = _FlWorkFWCtrlDiagSurveillanceCrcMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSurveillanceCrcMonitoringTable.setStatus("current")
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringEntry_Object = MibTableRow
flWorkFWCtrlDiagSurveillanceCrcMonitoringEntry = _FlWorkFWCtrlDiagSurveillanceCrcMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 1, 1, 1)
)
flWorkFWCtrlDiagSurveillanceCrcMonitoringEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSurveillanceCrcMonitoringEntry.setStatus("current")


class _FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex_Object = MibTableColumn
flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex = _FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 1, 1, 1, 1),
    _FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex_Type()
)
flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex.setStatus("current")
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak_Type = Integer32
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak_Object = MibTableColumn
flWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak = _FlWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 1, 1, 1, 2),
    _FlWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak_Type()
)
flWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak.setStatus("current")


class _FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("warning", 2),
          ("critical", 3))
    )


_FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus_Object = MibTableColumn
flWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus = _FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 1, 1, 1, 3),
    _FlWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus_Type()
)
flWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus.setStatus("current")
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringWarningThreshold_Type = Integer32
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringWarningThreshold_Object = MibTableColumn
flWorkFWCtrlDiagSurveillanceCrcMonitoringWarningThreshold = _FlWorkFWCtrlDiagSurveillanceCrcMonitoringWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 1, 1, 1, 4),
    _FlWorkFWCtrlDiagSurveillanceCrcMonitoringWarningThreshold_Type()
)
flWorkFWCtrlDiagSurveillanceCrcMonitoringWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSurveillanceCrcMonitoringWarningThreshold.setStatus("current")
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringCriticalThreshold_Type = Integer32
_FlWorkFWCtrlDiagSurveillanceCrcMonitoringCriticalThreshold_Object = MibTableColumn
flWorkFWCtrlDiagSurveillanceCrcMonitoringCriticalThreshold = _FlWorkFWCtrlDiagSurveillanceCrcMonitoringCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 1, 1, 1, 5),
    _FlWorkFWCtrlDiagSurveillanceCrcMonitoringCriticalThreshold_Type()
)
flWorkFWCtrlDiagSurveillanceCrcMonitoringCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSurveillanceCrcMonitoringCriticalThreshold.setStatus("current")


class _FlWorkFWCtrlDiagSurveillanceResetCrcValues_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSurveillanceResetCrcValues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 1),
          ("clear", 2))
    )


_FlWorkFWCtrlDiagSurveillanceResetCrcValues_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSurveillanceResetCrcValues_Object = MibScalar
flWorkFWCtrlDiagSurveillanceResetCrcValues = _FlWorkFWCtrlDiagSurveillanceResetCrcValues_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 1, 2),
    _FlWorkFWCtrlDiagSurveillanceResetCrcValues_Type()
)
flWorkFWCtrlDiagSurveillanceResetCrcValues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSurveillanceResetCrcValues.setStatus("current")
_FlWorkFWCtrlDiagSnapshot_ObjectIdentity = ObjectIdentity
flWorkFWCtrlDiagSnapshot = _FlWorkFWCtrlDiagSnapshot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 2)
)


class _FlWorkFWCtrlDiagSnapshotTrigger_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSnapshotTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSnap", 1),
          ("snap", 2))
    )


_FlWorkFWCtrlDiagSnapshotTrigger_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSnapshotTrigger_Object = MibScalar
flWorkFWCtrlDiagSnapshotTrigger = _FlWorkFWCtrlDiagSnapshotTrigger_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 2, 1),
    _FlWorkFWCtrlDiagSnapshotTrigger_Type()
)
flWorkFWCtrlDiagSnapshotTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSnapshotTrigger.setStatus("current")


class _FlWorkFWCtrlDiagSnapshotStatus_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSnapshotStatus based on Integer32"""
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
        *(("notPresent", 0),
          ("busy", 1),
          ("present", 2),
          ("error", 3))
    )


_FlWorkFWCtrlDiagSnapshotStatus_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSnapshotStatus_Object = MibScalar
flWorkFWCtrlDiagSnapshotStatus = _FlWorkFWCtrlDiagSnapshotStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 2, 2),
    _FlWorkFWCtrlDiagSnapshotStatus_Type()
)
flWorkFWCtrlDiagSnapshotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSnapshotStatus.setStatus("current")
_FlWorkFWCtrlDiagSnapshotTimeStamp_Type = OctetString
_FlWorkFWCtrlDiagSnapshotTimeStamp_Object = MibScalar
flWorkFWCtrlDiagSnapshotTimeStamp = _FlWorkFWCtrlDiagSnapshotTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 2, 3),
    _FlWorkFWCtrlDiagSnapshotTimeStamp_Type()
)
flWorkFWCtrlDiagSnapshotTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSnapshotTimeStamp.setStatus("current")
_FlWorkFWCtrlDiagSyslog_ObjectIdentity = ObjectIdentity
flWorkFWCtrlDiagSyslog = _FlWorkFWCtrlDiagSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3)
)


class _FlWorkFWCtrlDiagSyslogEnable_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSyslogEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlDiagSyslogEnable_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSyslogEnable_Object = MibScalar
flWorkFWCtrlDiagSyslogEnable = _FlWorkFWCtrlDiagSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 1),
    _FlWorkFWCtrlDiagSyslogEnable_Type()
)
flWorkFWCtrlDiagSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogEnable.setStatus("current")
_FlWorkFWCtrlDiagSyslogServTable_Object = MibTable
flWorkFWCtrlDiagSyslogServTable = _FlWorkFWCtrlDiagSyslogServTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 2)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogServTable.setStatus("current")
_FlWorkFWCtrlDiagSyslogServEntry_Object = MibTableRow
flWorkFWCtrlDiagSyslogServEntry = _FlWorkFWCtrlDiagSyslogServEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 2, 1)
)
flWorkFWCtrlDiagSyslogServEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDiagSyslogServIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogServEntry.setStatus("current")


class _FlWorkFWCtrlDiagSyslogServIndex_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSyslogServIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlDiagSyslogServIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSyslogServIndex_Object = MibTableColumn
flWorkFWCtrlDiagSyslogServIndex = _FlWorkFWCtrlDiagSyslogServIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 2, 1, 1),
    _FlWorkFWCtrlDiagSyslogServIndex_Type()
)
flWorkFWCtrlDiagSyslogServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogServIndex.setStatus("current")
_FlWorkFWCtrlDiagSyslogServIP_Type = IpAddress
_FlWorkFWCtrlDiagSyslogServIP_Object = MibTableColumn
flWorkFWCtrlDiagSyslogServIP = _FlWorkFWCtrlDiagSyslogServIP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 2, 1, 2),
    _FlWorkFWCtrlDiagSyslogServIP_Type()
)
flWorkFWCtrlDiagSyslogServIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogServIP.setStatus("current")
_FlWorkFWCtrlDiagSyslogServPort_Type = Integer32
_FlWorkFWCtrlDiagSyslogServPort_Object = MibTableColumn
flWorkFWCtrlDiagSyslogServPort = _FlWorkFWCtrlDiagSyslogServPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 2, 1, 3),
    _FlWorkFWCtrlDiagSyslogServPort_Type()
)
flWorkFWCtrlDiagSyslogServPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogServPort.setStatus("current")


class _FlWorkFWCtrlDiagSyslogServName_Type(DisplayString):
    """Custom type flWorkFWCtrlDiagSyslogServName based on DisplayString"""
    defaultValue = OctetString("")


_FlWorkFWCtrlDiagSyslogServName_Type.__name__ = "DisplayString"
_FlWorkFWCtrlDiagSyslogServName_Object = MibTableColumn
flWorkFWCtrlDiagSyslogServName = _FlWorkFWCtrlDiagSyslogServName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 2, 1, 4),
    _FlWorkFWCtrlDiagSyslogServName_Type()
)
flWorkFWCtrlDiagSyslogServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogServName.setStatus("current")


class _FlWorkFWCtrlDiagSyslogTestMsg_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSyslogTestMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTestMsg", 1),
          ("sendTestMsg", 2))
    )


_FlWorkFWCtrlDiagSyslogTestMsg_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSyslogTestMsg_Object = MibScalar
flWorkFWCtrlDiagSyslogTestMsg = _FlWorkFWCtrlDiagSyslogTestMsg_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 3),
    _FlWorkFWCtrlDiagSyslogTestMsg_Type()
)
flWorkFWCtrlDiagSyslogTestMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogTestMsg.setStatus("current")
_FlWorkFWCtrlDiagSyslogMsgGroupTable_Object = MibTable
flWorkFWCtrlDiagSyslogMsgGroupTable = _FlWorkFWCtrlDiagSyslogMsgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 4)
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogMsgGroupTable.setStatus("current")
_FlWorkFWCtrlDiagSyslogMsgGroupEntry_Object = MibTableRow
flWorkFWCtrlDiagSyslogMsgGroupEntry = _FlWorkFWCtrlDiagSyslogMsgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 4, 1)
)
flWorkFWCtrlDiagSyslogMsgGroupEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDiagSyslogMsgGroupIndex"),
)
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogMsgGroupEntry.setStatus("current")


class _FlWorkFWCtrlDiagSyslogMsgGroupIndex_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSyslogMsgGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkFWCtrlDiagSyslogMsgGroupIndex_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSyslogMsgGroupIndex_Object = MibTableColumn
flWorkFWCtrlDiagSyslogMsgGroupIndex = _FlWorkFWCtrlDiagSyslogMsgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 4, 1, 1),
    _FlWorkFWCtrlDiagSyslogMsgGroupIndex_Type()
)
flWorkFWCtrlDiagSyslogMsgGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogMsgGroupIndex.setStatus("current")
_FlWorkFWCtrlDiagSyslogMsgGroupName_Type = DisplayString
_FlWorkFWCtrlDiagSyslogMsgGroupName_Object = MibTableColumn
flWorkFWCtrlDiagSyslogMsgGroupName = _FlWorkFWCtrlDiagSyslogMsgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 4, 1, 2),
    _FlWorkFWCtrlDiagSyslogMsgGroupName_Type()
)
flWorkFWCtrlDiagSyslogMsgGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogMsgGroupName.setStatus("current")


class _FlWorkFWCtrlDiagSyslogMsgGroupState_Type(Integer32):
    """Custom type flWorkFWCtrlDiagSyslogMsgGroupState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkFWCtrlDiagSyslogMsgGroupState_Type.__name__ = "Integer32"
_FlWorkFWCtrlDiagSyslogMsgGroupState_Object = MibTableColumn
flWorkFWCtrlDiagSyslogMsgGroupState = _FlWorkFWCtrlDiagSyslogMsgGroupState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 11, 2, 23, 3, 4, 1, 3),
    _FlWorkFWCtrlDiagSyslogMsgGroupState_Type()
)
flWorkFWCtrlDiagSyslogMsgGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkFWCtrlDiagSyslogMsgGroupState.setStatus("current")
_FlSwitch_ObjectIdentity = ObjectIdentity
flSwitch = _FlSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15)
)
_FlSwitchCtrl_ObjectIdentity = ObjectIdentity
flSwitchCtrl = _FlSwitchCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1)
)


class _FlSwitchCtrlSpanTree_Type(Integer32):
    """Custom type flSwitchCtrlSpanTree based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchCtrlSpanTree_Type.__name__ = "Integer32"
_FlSwitchCtrlSpanTree_Object = MibScalar
flSwitchCtrlSpanTree = _FlSwitchCtrlSpanTree_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 1),
    _FlSwitchCtrlSpanTree_Type()
)
flSwitchCtrlSpanTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlSpanTree.setStatus("current")


class _FlSwitchCtrlRedundancy_Type(Integer32):
    """Custom type flSwitchCtrlRedundancy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRedundancy", 1),
          ("spanningTree", 2))
    )


_FlSwitchCtrlRedundancy_Type.__name__ = "Integer32"
_FlSwitchCtrlRedundancy_Object = MibScalar
flSwitchCtrlRedundancy = _FlSwitchCtrlRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 2),
    _FlSwitchCtrlRedundancy_Type()
)
flSwitchCtrlRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlRedundancy.setStatus("current")


class _FlSwitchCtrlMulticast_Type(Integer32):
    """Custom type flSwitchCtrlMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchCtrlMulticast_Type.__name__ = "Integer32"
_FlSwitchCtrlMulticast_Object = MibScalar
flSwitchCtrlMulticast = _FlSwitchCtrlMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 3),
    _FlSwitchCtrlMulticast_Type()
)
flSwitchCtrlMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlMulticast.setStatus("current")


class _FlSwitchCtrlVlan_Type(Integer32):
    """Custom type flSwitchCtrlVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchCtrlVlan_Type.__name__ = "Integer32"
_FlSwitchCtrlVlan_Object = MibScalar
flSwitchCtrlVlan = _FlSwitchCtrlVlan_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 4),
    _FlSwitchCtrlVlan_Type()
)
flSwitchCtrlVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlVlan.setStatus("current")


class _FlSwitchCtrlVlanTagMode_Type(Integer32):
    """Custom type flSwitchCtrlVlanTagMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlanTransparent", 1),
          ("vlanTagging", 2))
    )


_FlSwitchCtrlVlanTagMode_Type.__name__ = "Integer32"
_FlSwitchCtrlVlanTagMode_Object = MibScalar
flSwitchCtrlVlanTagMode = _FlSwitchCtrlVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 5),
    _FlSwitchCtrlVlanTagMode_Type()
)
flSwitchCtrlVlanTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlVlanTagMode.setStatus("current")


class _FlSwitchCtrlVlanTagStatus_Type(Integer32):
    """Custom type flSwitchCtrlVlanTagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlanTransparent", 1),
          ("vlanTagging", 2))
    )


_FlSwitchCtrlVlanTagStatus_Type.__name__ = "Integer32"
_FlSwitchCtrlVlanTagStatus_Object = MibScalar
flSwitchCtrlVlanTagStatus = _FlSwitchCtrlVlanTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 6),
    _FlSwitchCtrlVlanTagStatus_Type()
)
flSwitchCtrlVlanTagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchCtrlVlanTagStatus.setStatus("current")


class _FlSwitchCtrlLldp_Type(Integer32):
    """Custom type flSwitchCtrlLldp based on Integer32"""
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
        *(("disable", 1),
          ("enable", 2),
          ("transmit", 3),
          ("receive", 4))
    )


_FlSwitchCtrlLldp_Type.__name__ = "Integer32"
_FlSwitchCtrlLldp_Object = MibScalar
flSwitchCtrlLldp = _FlSwitchCtrlLldp_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 7),
    _FlSwitchCtrlLldp_Type()
)
flSwitchCtrlLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlLldp.setStatus("current")


class _FlSwitchCtrlRSTPLargeTreeSupport_Type(Integer32):
    """Custom type flSwitchCtrlRSTPLargeTreeSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchCtrlRSTPLargeTreeSupport_Type.__name__ = "Integer32"
_FlSwitchCtrlRSTPLargeTreeSupport_Object = MibScalar
flSwitchCtrlRSTPLargeTreeSupport = _FlSwitchCtrlRSTPLargeTreeSupport_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 8),
    _FlSwitchCtrlRSTPLargeTreeSupport_Type()
)
flSwitchCtrlRSTPLargeTreeSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlRSTPLargeTreeSupport.setStatus("current")


class _FlSwitchCtrlMacHashMode_Type(Integer32):
    """Custom type flSwitchCtrlMacHashMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("randomMacAddresses", 1),
          ("successiveMacAddresses", 2))
    )


_FlSwitchCtrlMacHashMode_Type.__name__ = "Integer32"
_FlSwitchCtrlMacHashMode_Object = MibScalar
flSwitchCtrlMacHashMode = _FlSwitchCtrlMacHashMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 9),
    _FlSwitchCtrlMacHashMode_Type()
)
flSwitchCtrlMacHashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlMacHashMode.setStatus("current")


class _FlSwitchCtrlDhcpRelayAgentUi_Type(Integer32):
    """Custom type flSwitchCtrlDhcpRelayAgentUi based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchCtrlDhcpRelayAgentUi_Type.__name__ = "Integer32"
_FlSwitchCtrlDhcpRelayAgentUi_Object = MibScalar
flSwitchCtrlDhcpRelayAgentUi = _FlSwitchCtrlDhcpRelayAgentUi_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 10),
    _FlSwitchCtrlDhcpRelayAgentUi_Type()
)
flSwitchCtrlDhcpRelayAgentUi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlDhcpRelayAgentUi.setStatus("current")


class _FlSwitchCtrlMacTableErase_Type(Integer32):
    """Custom type flSwitchCtrlMacTableErase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("eraseMacTable", 2))
    )


_FlSwitchCtrlMacTableErase_Type.__name__ = "Integer32"
_FlSwitchCtrlMacTableErase_Object = MibScalar
flSwitchCtrlMacTableErase = _FlSwitchCtrlMacTableErase_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 11),
    _FlSwitchCtrlMacTableErase_Type()
)
flSwitchCtrlMacTableErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlMacTableErase.setStatus("current")


class _FlSwitchCtrlRmonHistory_Type(Integer32):
    """Custom type flSwitchCtrlRmonHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchCtrlRmonHistory_Type.__name__ = "Integer32"
_FlSwitchCtrlRmonHistory_Object = MibScalar
flSwitchCtrlRmonHistory = _FlSwitchCtrlRmonHistory_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 14),
    _FlSwitchCtrlRmonHistory_Type()
)
flSwitchCtrlRmonHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlRmonHistory.setStatus("current")


class _FlSwitchCtrlLldpFlooding_Type(Integer32):
    """Custom type flSwitchCtrlLldpFlooding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchCtrlLldpFlooding_Type.__name__ = "Integer32"
_FlSwitchCtrlLldpFlooding_Object = MibScalar
flSwitchCtrlLldpFlooding = _FlSwitchCtrlLldpFlooding_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 15),
    _FlSwitchCtrlLldpFlooding_Type()
)
flSwitchCtrlLldpFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlLldpFlooding.setStatus("current")


class _FlSwitchCtrlQosProfile_Type(Integer32):
    """Custom type flSwitchCtrlQosProfile based on Integer32"""
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
        *(("universal", 1),
          ("profinet", 2),
          ("ethernetIP", 3))
    )


_FlSwitchCtrlQosProfile_Type.__name__ = "Integer32"
_FlSwitchCtrlQosProfile_Object = MibScalar
flSwitchCtrlQosProfile = _FlSwitchCtrlQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 1, 18),
    _FlSwitchCtrlQosProfile_Type()
)
flSwitchCtrlQosProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlQosProfile.setStatus("current")
_FlSwitchPortMirr_ObjectIdentity = ObjectIdentity
flSwitchPortMirr = _FlSwitchPortMirr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 2)
)


class _FlSwitchPortMirrDestinationPort_Type(Integer32):
    """Custom type flSwitchPortMirrDestinationPort based on Integer32"""
    defaultValue = 0


_FlSwitchPortMirrDestinationPort_Type.__name__ = "Integer32"
_FlSwitchPortMirrDestinationPort_Object = MibScalar
flSwitchPortMirrDestinationPort = _FlSwitchPortMirrDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 2, 1),
    _FlSwitchPortMirrDestinationPort_Type()
)
flSwitchPortMirrDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchPortMirrDestinationPort.setStatus("current")


class _FlSwitchPortMirrSourcePort_Type(Integer32):
    """Custom type flSwitchPortMirrSourcePort based on Integer32"""
    defaultValue = 0


_FlSwitchPortMirrSourcePort_Type.__name__ = "Integer32"
_FlSwitchPortMirrSourcePort_Object = MibScalar
flSwitchPortMirrSourcePort = _FlSwitchPortMirrSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 2, 2),
    _FlSwitchPortMirrSourcePort_Type()
)
flSwitchPortMirrSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchPortMirrSourcePort.setStatus("current")


class _FlSwitchPortMirrStatus_Type(Integer32):
    """Custom type flSwitchPortMirrStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchPortMirrStatus_Type.__name__ = "Integer32"
_FlSwitchPortMirrStatus_Object = MibScalar
flSwitchPortMirrStatus = _FlSwitchPortMirrStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 2, 3),
    _FlSwitchPortMirrStatus_Type()
)
flSwitchPortMirrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchPortMirrStatus.setStatus("current")
_FlSwitchPortMirrIngressSourcePort_Type = OctetString
_FlSwitchPortMirrIngressSourcePort_Object = MibScalar
flSwitchPortMirrIngressSourcePort = _FlSwitchPortMirrIngressSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 2, 4),
    _FlSwitchPortMirrIngressSourcePort_Type()
)
flSwitchPortMirrIngressSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchPortMirrIngressSourcePort.setStatus("current")
_FlSwitchPortMirrEgressSourcePort_Type = OctetString
_FlSwitchPortMirrEgressSourcePort_Object = MibScalar
flSwitchPortMirrEgressSourcePort = _FlSwitchPortMirrEgressSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 2, 5),
    _FlSwitchPortMirrEgressSourcePort_Type()
)
flSwitchPortMirrEgressSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchPortMirrEgressSourcePort.setStatus("current")
_FlSwitchIgmp_ObjectIdentity = ObjectIdentity
flSwitchIgmp = _FlSwitchIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3)
)
_FlSwitchIgmpSnoop_ObjectIdentity = ObjectIdentity
flSwitchIgmpSnoop = _FlSwitchIgmpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1)
)


class _FlSwitchIgmpSnoopEnable_Type(Integer32):
    """Custom type flSwitchIgmpSnoopEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchIgmpSnoopEnable_Type.__name__ = "Integer32"
_FlSwitchIgmpSnoopEnable_Object = MibScalar
flSwitchIgmpSnoopEnable = _FlSwitchIgmpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 1),
    _FlSwitchIgmpSnoopEnable_Type()
)
flSwitchIgmpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchIgmpSnoopEnable.setStatus("current")


class _FlSwitchIgmpSnoopAging_Type(Integer32):
    """Custom type flSwitchIgmpSnoopAging based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_FlSwitchIgmpSnoopAging_Type.__name__ = "Integer32"
_FlSwitchIgmpSnoopAging_Object = MibScalar
flSwitchIgmpSnoopAging = _FlSwitchIgmpSnoopAging_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 3),
    _FlSwitchIgmpSnoopAging_Type()
)
flSwitchIgmpSnoopAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchIgmpSnoopAging.setStatus("current")
_FlSwitchIgmpSnoopTable_Object = MibTable
flSwitchIgmpSnoopTable = _FlSwitchIgmpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 4)
)
if mibBuilder.loadTexts:
    flSwitchIgmpSnoopTable.setStatus("current")
_FlSwitchIgmpSnoopEntry_Object = MibTableRow
flSwitchIgmpSnoopEntry = _FlSwitchIgmpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    flSwitchIgmpSnoopEntry.setStatus("current")
_FlSwitchIgmpSnoopEgressPorts_Type = PortList
_FlSwitchIgmpSnoopEgressPorts_Object = MibTableColumn
flSwitchIgmpSnoopEgressPorts = _FlSwitchIgmpSnoopEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 4, 1, 1),
    _FlSwitchIgmpSnoopEgressPorts_Type()
)
flSwitchIgmpSnoopEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchIgmpSnoopEgressPorts.setStatus("current")
_FlSwitchIgmpSnoopExtended_ObjectIdentity = ObjectIdentity
flSwitchIgmpSnoopExtended = _FlSwitchIgmpSnoopExtended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 5)
)


class _FlSwitchBlockUnknownMulticastAtQuerier_Type(Integer32):
    """Custom type flSwitchBlockUnknownMulticastAtQuerier based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchBlockUnknownMulticastAtQuerier_Type.__name__ = "Integer32"
_FlSwitchBlockUnknownMulticastAtQuerier_Object = MibScalar
flSwitchBlockUnknownMulticastAtQuerier = _FlSwitchBlockUnknownMulticastAtQuerier_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 5, 1),
    _FlSwitchBlockUnknownMulticastAtQuerier_Type()
)
flSwitchBlockUnknownMulticastAtQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchBlockUnknownMulticastAtQuerier.setStatus("current")


class _FlSwitchForwardUnknownMulticastToQuerier_Type(Integer32):
    """Custom type flSwitchForwardUnknownMulticastToQuerier based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchForwardUnknownMulticastToQuerier_Type.__name__ = "Integer32"
_FlSwitchForwardUnknownMulticastToQuerier_Object = MibScalar
flSwitchForwardUnknownMulticastToQuerier = _FlSwitchForwardUnknownMulticastToQuerier_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 5, 2),
    _FlSwitchForwardUnknownMulticastToQuerier_Type()
)
flSwitchForwardUnknownMulticastToQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchForwardUnknownMulticastToQuerier.setStatus("current")


class _FlSwitchIGMPAutoQueryPort_Type(Integer32):
    """Custom type flSwitchIGMPAutoQueryPort based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchIGMPAutoQueryPort_Type.__name__ = "Integer32"
_FlSwitchIGMPAutoQueryPort_Object = MibScalar
flSwitchIGMPAutoQueryPort = _FlSwitchIGMPAutoQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 5, 3),
    _FlSwitchIGMPAutoQueryPort_Type()
)
flSwitchIGMPAutoQueryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchIGMPAutoQueryPort.setStatus("current")


class _FlSwitchIGMPAutoQueryPortsClear_Type(Integer32):
    """Custom type flSwitchIGMPAutoQueryPortsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("clear", 2))
    )


_FlSwitchIGMPAutoQueryPortsClear_Type.__name__ = "Integer32"
_FlSwitchIGMPAutoQueryPortsClear_Object = MibScalar
flSwitchIGMPAutoQueryPortsClear = _FlSwitchIGMPAutoQueryPortsClear_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 5, 4),
    _FlSwitchIGMPAutoQueryPortsClear_Type()
)
flSwitchIGMPAutoQueryPortsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchIGMPAutoQueryPortsClear.setStatus("current")
_FlSwitchIGMPStaticQueryPorts_Type = PortList
_FlSwitchIGMPStaticQueryPorts_Object = MibScalar
flSwitchIGMPStaticQueryPorts = _FlSwitchIGMPStaticQueryPorts_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 1, 5, 5),
    _FlSwitchIGMPStaticQueryPorts_Type()
)
flSwitchIGMPStaticQueryPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchIGMPStaticQueryPorts.setStatus("current")
_FlSwitchIgmpQuery_ObjectIdentity = ObjectIdentity
flSwitchIgmpQuery = _FlSwitchIgmpQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 2)
)
_FlSwitchIgmpQueryTable_Object = MibTable
flSwitchIgmpQueryTable = _FlSwitchIgmpQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 2, 1)
)
if mibBuilder.loadTexts:
    flSwitchIgmpQueryTable.setStatus("current")
_FlSwitchIgmpQueryEntry_Object = MibTableRow
flSwitchIgmpQueryEntry = _FlSwitchIgmpQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 2, 1, 1)
)
flSwitchIgmpQueryEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    flSwitchIgmpQueryEntry.setStatus("current")
_FlSwitchIgmpQueryPorts_Type = PortList
_FlSwitchIgmpQueryPorts_Object = MibTableColumn
flSwitchIgmpQueryPorts = _FlSwitchIgmpQueryPorts_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 2, 1, 1, 1),
    _FlSwitchIgmpQueryPorts_Type()
)
flSwitchIgmpQueryPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchIgmpQueryPorts.setStatus("current")


class _FlSwitchIgmpQueryEnable_Type(Integer32):
    """Custom type flSwitchIgmpQueryEnable based on Integer32"""
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
        *(("disable", 1),
          ("version1", 2),
          ("version2", 3))
    )


_FlSwitchIgmpQueryEnable_Type.__name__ = "Integer32"
_FlSwitchIgmpQueryEnable_Object = MibScalar
flSwitchIgmpQueryEnable = _FlSwitchIgmpQueryEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 2, 2),
    _FlSwitchIgmpQueryEnable_Type()
)
flSwitchIgmpQueryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchIgmpQueryEnable.setStatus("current")


class _FlSwitchIgmpQueryInterval_Type(Integer32):
    """Custom type flSwitchIgmpQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_FlSwitchIgmpQueryInterval_Type.__name__ = "Integer32"
_FlSwitchIgmpQueryInterval_Object = MibScalar
flSwitchIgmpQueryInterval = _FlSwitchIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 2, 3),
    _FlSwitchIgmpQueryInterval_Type()
)
flSwitchIgmpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchIgmpQueryInterval.setStatus("current")
_FlSwitchIgmpQueryActiveIP_Type = IpAddress
_FlSwitchIgmpQueryActiveIP_Object = MibScalar
flSwitchIgmpQueryActiveIP = _FlSwitchIgmpQueryActiveIP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 2, 4),
    _FlSwitchIgmpQueryActiveIP_Type()
)
flSwitchIgmpQueryActiveIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchIgmpQueryActiveIP.setStatus("current")


class _FlSwitchIgmpTablesErase_Type(Integer32):
    """Custom type flSwitchIgmpTablesErase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("eraseIgmpTables", 2))
    )


_FlSwitchIgmpTablesErase_Type.__name__ = "Integer32"
_FlSwitchIgmpTablesErase_Object = MibScalar
flSwitchIgmpTablesErase = _FlSwitchIgmpTablesErase_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 3, 3),
    _FlSwitchIgmpTablesErase_Type()
)
flSwitchIgmpTablesErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchIgmpTablesErase.setStatus("current")
_FlSwitchRedundancy_ObjectIdentity = ObjectIdentity
flSwitchRedundancy = _FlSwitchRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4)
)


class _FlSwitchCtrlRSTPFastRingDetection_Type(Integer32):
    """Custom type flSwitchCtrlRSTPFastRingDetection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchCtrlRSTPFastRingDetection_Type.__name__ = "Integer32"
_FlSwitchCtrlRSTPFastRingDetection_Object = MibScalar
flSwitchCtrlRSTPFastRingDetection = _FlSwitchCtrlRSTPFastRingDetection_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 1),
    _FlSwitchCtrlRSTPFastRingDetection_Type()
)
flSwitchCtrlRSTPFastRingDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchCtrlRSTPFastRingDetection.setStatus("current")
_FlSwitchRSTPRingTable_Object = MibTable
flSwitchRSTPRingTable = _FlSwitchRSTPRingTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 2)
)
if mibBuilder.loadTexts:
    flSwitchRSTPRingTable.setStatus("current")
_FlSwitchRSTPRingEntry_Object = MibTableRow
flSwitchRSTPRingEntry = _FlSwitchRSTPRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 2, 1)
)
flSwitchRSTPRingEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchRSTPRingIndex"),
)
if mibBuilder.loadTexts:
    flSwitchRSTPRingEntry.setStatus("current")


class _FlSwitchRSTPRingIndex_Type(Integer32):
    """Custom type flSwitchRSTPRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlSwitchRSTPRingIndex_Type.__name__ = "Integer32"
_FlSwitchRSTPRingIndex_Object = MibTableColumn
flSwitchRSTPRingIndex = _FlSwitchRSTPRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 2, 1, 1),
    _FlSwitchRSTPRingIndex_Type()
)
flSwitchRSTPRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRSTPRingIndex.setStatus("current")
_FlSwitchRSTPRingMAC_Type = MacAddress
_FlSwitchRSTPRingMAC_Object = MibTableColumn
flSwitchRSTPRingMAC = _FlSwitchRSTPRingMAC_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 2, 1, 2),
    _FlSwitchRSTPRingMAC_Type()
)
flSwitchRSTPRingMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRSTPRingMAC.setStatus("current")
_FlSwitchRSTPRingBlockPort_Type = Integer32
_FlSwitchRSTPRingBlockPort_Object = MibTableColumn
flSwitchRSTPRingBlockPort = _FlSwitchRSTPRingBlockPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 2, 1, 3),
    _FlSwitchRSTPRingBlockPort_Type()
)
flSwitchRSTPRingBlockPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRSTPRingBlockPort.setStatus("current")
_FlSwitchRSTPRingRootPort_Type = Integer32
_FlSwitchRSTPRingRootPort_Object = MibTableColumn
flSwitchRSTPRingRootPort = _FlSwitchRSTPRingRootPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 2, 1, 4),
    _FlSwitchRSTPRingRootPort_Type()
)
flSwitchRSTPRingRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRSTPRingRootPort.setStatus("current")
_FlSwitchRSTPRingDesPort_Type = Integer32
_FlSwitchRSTPRingDesPort_Object = MibTableColumn
flSwitchRSTPRingDesPort = _FlSwitchRSTPRingDesPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 2, 1, 5),
    _FlSwitchRSTPRingDesPort_Type()
)
flSwitchRSTPRingDesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRSTPRingDesPort.setStatus("current")


class _FlSwitchRSTPRingStatus_Type(Integer32):
    """Custom type flSwitchRSTPRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("closed", 3),
          ("breaked", 6),
          ("failed", 7))
    )


_FlSwitchRSTPRingStatus_Type.__name__ = "Integer32"
_FlSwitchRSTPRingStatus_Object = MibTableColumn
flSwitchRSTPRingStatus = _FlSwitchRSTPRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 2, 1, 6),
    _FlSwitchRSTPRingStatus_Type()
)
flSwitchRSTPRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRSTPRingStatus.setStatus("current")
_FlSwitchRSTPRingFailedPort_Type = Integer32
_FlSwitchRSTPRingFailedPort_Object = MibScalar
flSwitchRSTPRingFailedPort = _FlSwitchRSTPRingFailedPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 3),
    _FlSwitchRSTPRingFailedPort_Type()
)
flSwitchRSTPRingFailedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRSTPRingFailedPort.setStatus("current")
_FlSwitchRSTPextPortTable_Object = MibTable
flSwitchRSTPextPortTable = _FlSwitchRSTPextPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 4)
)
if mibBuilder.loadTexts:
    flSwitchRSTPextPortTable.setStatus("current")
_FlSwitchRSTPextPortEntry_Object = MibTableRow
flSwitchRSTPextPortEntry = _FlSwitchRSTPextPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 4, 1)
)
flSwitchRSTPextPortEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchRSTPextPortNum"),
)
if mibBuilder.loadTexts:
    flSwitchRSTPextPortEntry.setStatus("current")


class _FlSwitchRSTPextPortNum_Type(Integer32):
    """Custom type flSwitchRSTPextPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlSwitchRSTPextPortNum_Type.__name__ = "Integer32"
_FlSwitchRSTPextPortNum_Object = MibTableColumn
flSwitchRSTPextPortNum = _FlSwitchRSTPextPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 4, 1, 1),
    _FlSwitchRSTPextPortNum_Type()
)
flSwitchRSTPextPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRSTPextPortNum.setStatus("current")


class _FlSwitchRSTPextAutoEdge_Type(Integer32):
    """Custom type flSwitchRSTPextAutoEdge based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchRSTPextAutoEdge_Type.__name__ = "Integer32"
_FlSwitchRSTPextAutoEdge_Object = MibTableColumn
flSwitchRSTPextAutoEdge = _FlSwitchRSTPextAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 4, 1, 2),
    _FlSwitchRSTPextAutoEdge_Type()
)
flSwitchRSTPextAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchRSTPextAutoEdge.setStatus("current")


class _FlSwitchRSTPextBPDUFlood_Type(Integer32):
    """Custom type flSwitchRSTPextBPDUFlood based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchRSTPextBPDUFlood_Type.__name__ = "Integer32"
_FlSwitchRSTPextBPDUFlood_Object = MibTableColumn
flSwitchRSTPextBPDUFlood = _FlSwitchRSTPextBPDUFlood_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 4, 4, 1, 3),
    _FlSwitchRSTPextBPDUFlood_Type()
)
flSwitchRSTPextBPDUFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchRSTPextBPDUFlood.setStatus("current")
_FlSwitchRelayAgentDhcp_ObjectIdentity = ObjectIdentity
flSwitchRelayAgentDhcp = _FlSwitchRelayAgentDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 5)
)


class _FlSwitchRelayAgentDhcpCtrl_Type(Integer32):
    """Custom type flSwitchRelayAgentDhcpCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchRelayAgentDhcpCtrl_Type.__name__ = "Integer32"
_FlSwitchRelayAgentDhcpCtrl_Object = MibScalar
flSwitchRelayAgentDhcpCtrl = _FlSwitchRelayAgentDhcpCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 5, 1),
    _FlSwitchRelayAgentDhcpCtrl_Type()
)
flSwitchRelayAgentDhcpCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchRelayAgentDhcpCtrl.setStatus("current")
_FlSwitchRelayAgentDhcpIpAddress_Type = IpAddress
_FlSwitchRelayAgentDhcpIpAddress_Object = MibScalar
flSwitchRelayAgentDhcpIpAddress = _FlSwitchRelayAgentDhcpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 5, 2),
    _FlSwitchRelayAgentDhcpIpAddress_Type()
)
flSwitchRelayAgentDhcpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchRelayAgentDhcpIpAddress.setStatus("current")


class _FlSwitchRelayAgentDhcpStatus_Type(OctetString):
    """Custom type flSwitchRelayAgentDhcpStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FlSwitchRelayAgentDhcpStatus_Type.__name__ = "OctetString"
_FlSwitchRelayAgentDhcpStatus_Object = MibScalar
flSwitchRelayAgentDhcpStatus = _FlSwitchRelayAgentDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 5, 3),
    _FlSwitchRelayAgentDhcpStatus_Type()
)
flSwitchRelayAgentDhcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRelayAgentDhcpStatus.setStatus("current")


class _FlSwitchRelayAgentDhcpRIdType_Type(Integer32):
    """Custom type flSwitchRelayAgentDhcpRIdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddress", 1),
          ("macAddress", 2))
    )


_FlSwitchRelayAgentDhcpRIdType_Type.__name__ = "Integer32"
_FlSwitchRelayAgentDhcpRIdType_Object = MibScalar
flSwitchRelayAgentDhcpRIdType = _FlSwitchRelayAgentDhcpRIdType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 5, 4),
    _FlSwitchRelayAgentDhcpRIdType_Type()
)
flSwitchRelayAgentDhcpRIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchRelayAgentDhcpRIdType.setStatus("current")
_FlSwitchRelayAgentDhcpPortTable_Object = MibTable
flSwitchRelayAgentDhcpPortTable = _FlSwitchRelayAgentDhcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 5, 5)
)
if mibBuilder.loadTexts:
    flSwitchRelayAgentDhcpPortTable.setStatus("current")
_FlSwitchRelayAgentDhcpPortEntry_Object = MibTableRow
flSwitchRelayAgentDhcpPortEntry = _FlSwitchRelayAgentDhcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 5, 5, 1)
)
flSwitchRelayAgentDhcpPortEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchRelayAgentDhcpPortCtrlIndex"),
)
if mibBuilder.loadTexts:
    flSwitchRelayAgentDhcpPortEntry.setStatus("current")


class _FlSwitchRelayAgentDhcpPortCtrlIndex_Type(Integer32):
    """Custom type flSwitchRelayAgentDhcpPortCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlSwitchRelayAgentDhcpPortCtrlIndex_Type.__name__ = "Integer32"
_FlSwitchRelayAgentDhcpPortCtrlIndex_Object = MibTableColumn
flSwitchRelayAgentDhcpPortCtrlIndex = _FlSwitchRelayAgentDhcpPortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 5, 5, 1, 1),
    _FlSwitchRelayAgentDhcpPortCtrlIndex_Type()
)
flSwitchRelayAgentDhcpPortCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchRelayAgentDhcpPortCtrlIndex.setStatus("current")


class _FlSwitchRelayAgentDhcpPortCtrlOperation_Type(Integer32):
    """Custom type flSwitchRelayAgentDhcpPortCtrlOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchRelayAgentDhcpPortCtrlOperation_Type.__name__ = "Integer32"
_FlSwitchRelayAgentDhcpPortCtrlOperation_Object = MibTableColumn
flSwitchRelayAgentDhcpPortCtrlOperation = _FlSwitchRelayAgentDhcpPortCtrlOperation_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 5, 5, 1, 2),
    _FlSwitchRelayAgentDhcpPortCtrlOperation_Type()
)
flSwitchRelayAgentDhcpPortCtrlOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchRelayAgentDhcpPortCtrlOperation.setStatus("current")
_FlSwitchRateCtrl_ObjectIdentity = ObjectIdentity
flSwitchRateCtrl = _FlSwitchRateCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6)
)


class _FlSwitchRateCtrlBroadcast_Type(Integer32):
    """Custom type flSwitchRateCtrlBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchRateCtrlBroadcast_Type.__name__ = "Integer32"
_FlSwitchRateCtrlBroadcast_Object = MibScalar
flSwitchRateCtrlBroadcast = _FlSwitchRateCtrlBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 1),
    _FlSwitchRateCtrlBroadcast_Type()
)
flSwitchRateCtrlBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchRateCtrlBroadcast.setStatus("current")


class _FlSwitchRateCtrlMulticast_Type(Integer32):
    """Custom type flSwitchRateCtrlMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchRateCtrlMulticast_Type.__name__ = "Integer32"
_FlSwitchRateCtrlMulticast_Object = MibScalar
flSwitchRateCtrlMulticast = _FlSwitchRateCtrlMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 2),
    _FlSwitchRateCtrlMulticast_Type()
)
flSwitchRateCtrlMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchRateCtrlMulticast.setStatus("current")


class _FlSwitchRateCtrlBitrate_Type(Integer32):
    """Custom type flSwitchRateCtrlBitrate based on Integer32"""
    defaultValue = 0


_FlSwitchRateCtrlBitrate_Type.__name__ = "Integer32"
_FlSwitchRateCtrlBitrate_Object = MibScalar
flSwitchRateCtrlBitrate = _FlSwitchRateCtrlBitrate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 3),
    _FlSwitchRateCtrlBitrate_Type()
)
flSwitchRateCtrlBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchRateCtrlBitrate.setStatus("current")


class _FlSwitchDot3FlowControlMode_Type(Integer32):
    """Custom type flSwitchDot3FlowControlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlSwitchDot3FlowControlMode_Type.__name__ = "Integer32"
_FlSwitchDot3FlowControlMode_Object = MibScalar
flSwitchDot3FlowControlMode = _FlSwitchDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 4),
    _FlSwitchDot3FlowControlMode_Type()
)
flSwitchDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDot3FlowControlMode.setStatus("current")


class _FlSwitchBroadcastControlMode_Type(Integer32):
    """Custom type flSwitchBroadcastControlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlSwitchBroadcastControlMode_Type.__name__ = "Integer32"
_FlSwitchBroadcastControlMode_Object = MibScalar
flSwitchBroadcastControlMode = _FlSwitchBroadcastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 5),
    _FlSwitchBroadcastControlMode_Type()
)
flSwitchBroadcastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchBroadcastControlMode.setStatus("current")


class _FlSwitchBroadcastControlThreshold_Type(Unsigned32):
    """Custom type flSwitchBroadcastControlThreshold based on Unsigned32"""
    defaultValue = 1220

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_FlSwitchBroadcastControlThreshold_Type.__name__ = "Unsigned32"
_FlSwitchBroadcastControlThreshold_Object = MibScalar
flSwitchBroadcastControlThreshold = _FlSwitchBroadcastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 6),
    _FlSwitchBroadcastControlThreshold_Type()
)
flSwitchBroadcastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchBroadcastControlThreshold.setStatus("current")


class _FlSwitchMulticastControlMode_Type(Integer32):
    """Custom type flSwitchMulticastControlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlSwitchMulticastControlMode_Type.__name__ = "Integer32"
_FlSwitchMulticastControlMode_Object = MibScalar
flSwitchMulticastControlMode = _FlSwitchMulticastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 7),
    _FlSwitchMulticastControlMode_Type()
)
flSwitchMulticastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchMulticastControlMode.setStatus("current")


class _FlSwitchMulticastControlThreshold_Type(Unsigned32):
    """Custom type flSwitchMulticastControlThreshold based on Unsigned32"""
    defaultValue = 1220

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_FlSwitchMulticastControlThreshold_Type.__name__ = "Unsigned32"
_FlSwitchMulticastControlThreshold_Object = MibScalar
flSwitchMulticastControlThreshold = _FlSwitchMulticastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 8),
    _FlSwitchMulticastControlThreshold_Type()
)
flSwitchMulticastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchMulticastControlThreshold.setStatus("current")


class _FlSwitchUnicastControlMode_Type(Integer32):
    """Custom type flSwitchUnicastControlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlSwitchUnicastControlMode_Type.__name__ = "Integer32"
_FlSwitchUnicastControlMode_Object = MibScalar
flSwitchUnicastControlMode = _FlSwitchUnicastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 9),
    _FlSwitchUnicastControlMode_Type()
)
flSwitchUnicastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchUnicastControlMode.setStatus("current")


class _FlSwitchUnicastControlThreshold_Type(Unsigned32):
    """Custom type flSwitchUnicastControlThreshold based on Unsigned32"""
    defaultValue = 1220

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_FlSwitchUnicastControlThreshold_Type.__name__ = "Unsigned32"
_FlSwitchUnicastControlThreshold_Object = MibScalar
flSwitchUnicastControlThreshold = _FlSwitchUnicastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 10),
    _FlSwitchUnicastControlThreshold_Type()
)
flSwitchUnicastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchUnicastControlThreshold.setStatus("current")
_FlSwitchStormCtrlTable_Object = MibTable
flSwitchStormCtrlTable = _FlSwitchStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11)
)
if mibBuilder.loadTexts:
    flSwitchStormCtrlTable.setStatus("current")
_FlSwitchStormCtrlEntry_Object = MibTableRow
flSwitchStormCtrlEntry = _FlSwitchStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1)
)
flSwitchStormCtrlEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchStormCtrlPortNum"),
)
if mibBuilder.loadTexts:
    flSwitchStormCtrlEntry.setStatus("current")


class _FlSwitchStormCtrlPortNum_Type(Integer32):
    """Custom type flSwitchStormCtrlPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlSwitchStormCtrlPortNum_Type.__name__ = "Integer32"
_FlSwitchStormCtrlPortNum_Object = MibTableColumn
flSwitchStormCtrlPortNum = _FlSwitchStormCtrlPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 1),
    _FlSwitchStormCtrlPortNum_Type()
)
flSwitchStormCtrlPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchStormCtrlPortNum.setStatus("current")


class _FlSwitchStormCtrlBroadcast_Type(Integer32):
    """Custom type flSwitchStormCtrlBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchStormCtrlBroadcast_Type.__name__ = "Integer32"
_FlSwitchStormCtrlBroadcast_Object = MibTableColumn
flSwitchStormCtrlBroadcast = _FlSwitchStormCtrlBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 2),
    _FlSwitchStormCtrlBroadcast_Type()
)
flSwitchStormCtrlBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlBroadcast.setStatus("current")


class _FlSwitchStormCtrlMulticast_Type(Integer32):
    """Custom type flSwitchStormCtrlMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchStormCtrlMulticast_Type.__name__ = "Integer32"
_FlSwitchStormCtrlMulticast_Object = MibTableColumn
flSwitchStormCtrlMulticast = _FlSwitchStormCtrlMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 3),
    _FlSwitchStormCtrlMulticast_Type()
)
flSwitchStormCtrlMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlMulticast.setStatus("current")


class _FlSwitchStormCtrlUnicast_Type(Integer32):
    """Custom type flSwitchStormCtrlUnicast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchStormCtrlUnicast_Type.__name__ = "Integer32"
_FlSwitchStormCtrlUnicast_Object = MibTableColumn
flSwitchStormCtrlUnicast = _FlSwitchStormCtrlUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 4),
    _FlSwitchStormCtrlUnicast_Type()
)
flSwitchStormCtrlUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlUnicast.setStatus("current")


class _FlSwitchStormCtrlThreshold_Type(DisplayString):
    """Custom type flSwitchStormCtrlThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_FlSwitchStormCtrlThreshold_Type.__name__ = "DisplayString"
_FlSwitchStormCtrlThreshold_Object = MibTableColumn
flSwitchStormCtrlThreshold = _FlSwitchStormCtrlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 5),
    _FlSwitchStormCtrlThreshold_Type()
)
flSwitchStormCtrlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlThreshold.setStatus("current")


class _FlSwitchStormCtrlThresholdUnicast_Type(DisplayString):
    """Custom type flSwitchStormCtrlThresholdUnicast based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_FlSwitchStormCtrlThresholdUnicast_Type.__name__ = "DisplayString"
_FlSwitchStormCtrlThresholdUnicast_Object = MibTableColumn
flSwitchStormCtrlThresholdUnicast = _FlSwitchStormCtrlThresholdUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 6),
    _FlSwitchStormCtrlThresholdUnicast_Type()
)
flSwitchStormCtrlThresholdUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlThresholdUnicast.setStatus("current")


class _FlSwitchStormCtrlThresholdBroadcast_Type(DisplayString):
    """Custom type flSwitchStormCtrlThresholdBroadcast based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_FlSwitchStormCtrlThresholdBroadcast_Type.__name__ = "DisplayString"
_FlSwitchStormCtrlThresholdBroadcast_Object = MibTableColumn
flSwitchStormCtrlThresholdBroadcast = _FlSwitchStormCtrlThresholdBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 7),
    _FlSwitchStormCtrlThresholdBroadcast_Type()
)
flSwitchStormCtrlThresholdBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlThresholdBroadcast.setStatus("current")


class _FlSwitchStormCtrlThresholdMulticast_Type(DisplayString):
    """Custom type flSwitchStormCtrlThresholdMulticast based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_FlSwitchStormCtrlThresholdMulticast_Type.__name__ = "DisplayString"
_FlSwitchStormCtrlThresholdMulticast_Object = MibTableColumn
flSwitchStormCtrlThresholdMulticast = _FlSwitchStormCtrlThresholdMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 8),
    _FlSwitchStormCtrlThresholdMulticast_Type()
)
flSwitchStormCtrlThresholdMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlThresholdMulticast.setStatus("current")


class _FlSwitchStormCtrlBandwidthUnicast_Type(Gauge32):
    """Custom type flSwitchStormCtrlBandwidthUnicast based on Gauge32"""
    defaultValue = 5000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FlSwitchStormCtrlBandwidthUnicast_Type.__name__ = "Gauge32"
_FlSwitchStormCtrlBandwidthUnicast_Object = MibTableColumn
flSwitchStormCtrlBandwidthUnicast = _FlSwitchStormCtrlBandwidthUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 9),
    _FlSwitchStormCtrlBandwidthUnicast_Type()
)
flSwitchStormCtrlBandwidthUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlBandwidthUnicast.setStatus("current")


class _FlSwitchStormCtrlBandwidthBroadcast_Type(Gauge32):
    """Custom type flSwitchStormCtrlBandwidthBroadcast based on Gauge32"""
    defaultValue = 5000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FlSwitchStormCtrlBandwidthBroadcast_Type.__name__ = "Gauge32"
_FlSwitchStormCtrlBandwidthBroadcast_Object = MibTableColumn
flSwitchStormCtrlBandwidthBroadcast = _FlSwitchStormCtrlBandwidthBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 10),
    _FlSwitchStormCtrlBandwidthBroadcast_Type()
)
flSwitchStormCtrlBandwidthBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlBandwidthBroadcast.setStatus("current")


class _FlSwitchStormCtrlBandwidthMulticast_Type(Gauge32):
    """Custom type flSwitchStormCtrlBandwidthMulticast based on Gauge32"""
    defaultValue = 5000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FlSwitchStormCtrlBandwidthMulticast_Type.__name__ = "Gauge32"
_FlSwitchStormCtrlBandwidthMulticast_Object = MibTableColumn
flSwitchStormCtrlBandwidthMulticast = _FlSwitchStormCtrlBandwidthMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 11),
    _FlSwitchStormCtrlBandwidthMulticast_Type()
)
flSwitchStormCtrlBandwidthMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlBandwidthMulticast.setStatus("current")


class _FlSwitchStormCtrlFrameLimitUnicast_Type(Gauge32):
    """Custom type flSwitchStormCtrlFrameLimitUnicast based on Gauge32"""
    defaultValue = 1220

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FlSwitchStormCtrlFrameLimitUnicast_Type.__name__ = "Gauge32"
_FlSwitchStormCtrlFrameLimitUnicast_Object = MibTableColumn
flSwitchStormCtrlFrameLimitUnicast = _FlSwitchStormCtrlFrameLimitUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 12),
    _FlSwitchStormCtrlFrameLimitUnicast_Type()
)
flSwitchStormCtrlFrameLimitUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlFrameLimitUnicast.setStatus("current")


class _FlSwitchStormCtrlFrameLimitBroadcast_Type(Gauge32):
    """Custom type flSwitchStormCtrlFrameLimitBroadcast based on Gauge32"""
    defaultValue = 1220

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FlSwitchStormCtrlFrameLimitBroadcast_Type.__name__ = "Gauge32"
_FlSwitchStormCtrlFrameLimitBroadcast_Object = MibTableColumn
flSwitchStormCtrlFrameLimitBroadcast = _FlSwitchStormCtrlFrameLimitBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 13),
    _FlSwitchStormCtrlFrameLimitBroadcast_Type()
)
flSwitchStormCtrlFrameLimitBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlFrameLimitBroadcast.setStatus("current")


class _FlSwitchStormCtrlFrameLimitMulticast_Type(Gauge32):
    """Custom type flSwitchStormCtrlFrameLimitMulticast based on Gauge32"""
    defaultValue = 1220

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FlSwitchStormCtrlFrameLimitMulticast_Type.__name__ = "Gauge32"
_FlSwitchStormCtrlFrameLimitMulticast_Object = MibTableColumn
flSwitchStormCtrlFrameLimitMulticast = _FlSwitchStormCtrlFrameLimitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 6, 11, 1, 14),
    _FlSwitchStormCtrlFrameLimitMulticast_Type()
)
flSwitchStormCtrlFrameLimitMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchStormCtrlFrameLimitMulticast.setStatus("current")
_FlSwitchTrafficShaping_ObjectIdentity = ObjectIdentity
flSwitchTrafficShaping = _FlSwitchTrafficShaping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 7)
)
_FlSwitchTrafficShapingTable_Object = MibTable
flSwitchTrafficShapingTable = _FlSwitchTrafficShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 7, 1)
)
if mibBuilder.loadTexts:
    flSwitchTrafficShapingTable.setStatus("current")
_FlSwitchTrafficShapingEntry_Object = MibTableRow
flSwitchTrafficShapingEntry = _FlSwitchTrafficShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 7, 1, 1)
)
flSwitchTrafficShapingEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchTrafficShapingIntfIndex"),
)
if mibBuilder.loadTexts:
    flSwitchTrafficShapingEntry.setStatus("current")
_FlSwitchTrafficShapingIntfIndex_Type = InterfaceIndexOrZero
_FlSwitchTrafficShapingIntfIndex_Object = MibTableColumn
flSwitchTrafficShapingIntfIndex = _FlSwitchTrafficShapingIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 7, 1, 1, 1),
    _FlSwitchTrafficShapingIntfIndex_Type()
)
flSwitchTrafficShapingIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flSwitchTrafficShapingIntfIndex.setStatus("current")


class _FlSwitchTrafficShapingIntfRate_Type(Unsigned32):
    """Custom type flSwitchTrafficShapingIntfRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FlSwitchTrafficShapingIntfRate_Type.__name__ = "Unsigned32"
_FlSwitchTrafficShapingIntfRate_Object = MibTableColumn
flSwitchTrafficShapingIntfRate = _FlSwitchTrafficShapingIntfRate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 7, 1, 1, 2),
    _FlSwitchTrafficShapingIntfRate_Type()
)
flSwitchTrafficShapingIntfRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchTrafficShapingIntfRate.setStatus("current")
_FlSwitchLagConfig_ObjectIdentity = ObjectIdentity
flSwitchLagConfig = _FlSwitchLagConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8)
)


class _FlSwitchLagCreate_Type(DisplayString):
    """Custom type flSwitchLagCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 15),
    )


_FlSwitchLagCreate_Type.__name__ = "DisplayString"
_FlSwitchLagCreate_Object = MibScalar
flSwitchLagCreate = _FlSwitchLagCreate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 1),
    _FlSwitchLagCreate_Type()
)
flSwitchLagCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagCreate.setStatus("current")
_FlSwitchLagSummaryTable_Object = MibTable
flSwitchLagSummaryTable = _FlSwitchLagSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2)
)
if mibBuilder.loadTexts:
    flSwitchLagSummaryTable.setStatus("current")
_FlSwitchLagSummaryEntry_Object = MibTableRow
flSwitchLagSummaryEntry = _FlSwitchLagSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1)
)
flSwitchLagSummaryEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchLagIndex"),
)
if mibBuilder.loadTexts:
    flSwitchLagSummaryEntry.setStatus("current")


class _FlSwitchLagIndex_Type(Integer32):
    """Custom type flSwitchLagIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlSwitchLagIndex_Type.__name__ = "Integer32"
_FlSwitchLagIndex_Object = MibTableColumn
flSwitchLagIndex = _FlSwitchLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 1),
    _FlSwitchLagIndex_Type()
)
flSwitchLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchLagIndex.setStatus("current")


class _FlSwitchLagName_Type(DisplayString):
    """Custom type flSwitchLagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FlSwitchLagName_Type.__name__ = "DisplayString"
_FlSwitchLagName_Object = MibTableColumn
flSwitchLagName = _FlSwitchLagName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 2),
    _FlSwitchLagName_Type()
)
flSwitchLagName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagName.setStatus("current")


class _FlSwitchLagLinkTrap_Type(Integer32):
    """Custom type flSwitchLagLinkTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlSwitchLagLinkTrap_Type.__name__ = "Integer32"
_FlSwitchLagLinkTrap_Object = MibTableColumn
flSwitchLagLinkTrap = _FlSwitchLagLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 4),
    _FlSwitchLagLinkTrap_Type()
)
flSwitchLagLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagLinkTrap.setStatus("current")


class _FlSwitchLagAdminMode_Type(Integer32):
    """Custom type flSwitchLagAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlSwitchLagAdminMode_Type.__name__ = "Integer32"
_FlSwitchLagAdminMode_Object = MibTableColumn
flSwitchLagAdminMode = _FlSwitchLagAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 5),
    _FlSwitchLagAdminMode_Type()
)
flSwitchLagAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagAdminMode.setStatus("current")


class _FlSwitchLagStpMode_Type(Integer32):
    """Custom type flSwitchLagStpMode based on Integer32"""
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
        *(("dot1d", 1),
          ("fast", 2),
          ("off", 3),
          ("dot1s", 4))
    )


_FlSwitchLagStpMode_Type.__name__ = "Integer32"
_FlSwitchLagStpMode_Object = MibTableColumn
flSwitchLagStpMode = _FlSwitchLagStpMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 6),
    _FlSwitchLagStpMode_Type()
)
flSwitchLagStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagStpMode.setStatus("current")
_FlSwitchLagAddPort_Type = Integer32
_FlSwitchLagAddPort_Object = MibTableColumn
flSwitchLagAddPort = _FlSwitchLagAddPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 7),
    _FlSwitchLagAddPort_Type()
)
flSwitchLagAddPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagAddPort.setStatus("current")
_FlSwitchLagDeletePort_Type = Integer32
_FlSwitchLagDeletePort_Object = MibTableColumn
flSwitchLagDeletePort = _FlSwitchLagDeletePort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 8),
    _FlSwitchLagDeletePort_Type()
)
flSwitchLagDeletePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagDeletePort.setStatus("current")
_FlSwitchLagStatus_Type = RowStatus
_FlSwitchLagStatus_Object = MibTableColumn
flSwitchLagStatus = _FlSwitchLagStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 9),
    _FlSwitchLagStatus_Type()
)
flSwitchLagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagStatus.setStatus("current")


class _FlSwitchLagType_Type(Integer32):
    """Custom type flSwitchLagType based on Integer32"""
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


_FlSwitchLagType_Type.__name__ = "Integer32"
_FlSwitchLagType_Object = MibTableColumn
flSwitchLagType = _FlSwitchLagType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 10),
    _FlSwitchLagType_Type()
)
flSwitchLagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchLagType.setStatus("current")


class _FlSwitchLagStaticCapability_Type(Integer32):
    """Custom type flSwitchLagStaticCapability based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlSwitchLagStaticCapability_Type.__name__ = "Integer32"
_FlSwitchLagStaticCapability_Object = MibTableColumn
flSwitchLagStaticCapability = _FlSwitchLagStaticCapability_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 11),
    _FlSwitchLagStaticCapability_Type()
)
flSwitchLagStaticCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagStaticCapability.setStatus("current")


class _FlSwitchLagHashOption_Type(Integer32):
    """Custom type flSwitchLagHashOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FlSwitchLagHashOption_Type.__name__ = "Integer32"
_FlSwitchLagHashOption_Object = MibTableColumn
flSwitchLagHashOption = _FlSwitchLagHashOption_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 12),
    _FlSwitchLagHashOption_Type()
)
flSwitchLagHashOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagHashOption.setStatus("current")


class _FlSwitchLagMaxFrameSize_Type(Integer32):
    """Custom type flSwitchLagMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9216),
    )


_FlSwitchLagMaxFrameSize_Type.__name__ = "Integer32"
_FlSwitchLagMaxFrameSize_Object = MibTableColumn
flSwitchLagMaxFrameSize = _FlSwitchLagMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 13),
    _FlSwitchLagMaxFrameSize_Type()
)
flSwitchLagMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagMaxFrameSize.setStatus("current")


class _FlSwitchLagJumboFrame_Type(Integer32):
    """Custom type flSwitchLagJumboFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FlSwitchLagJumboFrame_Type.__name__ = "Integer32"
_FlSwitchLagJumboFrame_Object = MibTableColumn
flSwitchLagJumboFrame = _FlSwitchLagJumboFrame_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 14),
    _FlSwitchLagJumboFrame_Type()
)
flSwitchLagJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagJumboFrame.setStatus("current")


class _FlSwitchLagLinkStatus_Type(Integer32):
    """Custom type flSwitchLagLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FlSwitchLagLinkStatus_Type.__name__ = "Integer32"
_FlSwitchLagLinkStatus_Object = MibTableColumn
flSwitchLagLinkStatus = _FlSwitchLagLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 15),
    _FlSwitchLagLinkStatus_Type()
)
flSwitchLagLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchLagLinkStatus.setStatus("current")


class _FlSwitchLagMode_Type(Integer32):
    """Custom type flSwitchLagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("static", 2),
          ("lacp-passiv", 3),
          ("lacp-activ", 4))
    )


_FlSwitchLagMode_Type.__name__ = "Integer32"
_FlSwitchLagMode_Object = MibTableColumn
flSwitchLagMode = _FlSwitchLagMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 2, 1, 16),
    _FlSwitchLagMode_Type()
)
flSwitchLagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagMode.setStatus("current")
_FlSwitchLagConfigTable_Object = MibTable
flSwitchLagConfigTable = _FlSwitchLagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 3)
)
if mibBuilder.loadTexts:
    flSwitchLagConfigTable.setStatus("current")
_FlSwitchLagConfigEntry_Object = MibTableRow
flSwitchLagConfigEntry = _FlSwitchLagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 3, 1)
)
flSwitchLagConfigEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchLagConfigIndex"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchLagConfigIfIndex"),
)
if mibBuilder.loadTexts:
    flSwitchLagConfigEntry.setStatus("current")


class _FlSwitchLagConfigIndex_Type(Integer32):
    """Custom type flSwitchLagConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlSwitchLagConfigIndex_Type.__name__ = "Integer32"
_FlSwitchLagConfigIndex_Object = MibTableColumn
flSwitchLagConfigIndex = _FlSwitchLagConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 3, 1, 1),
    _FlSwitchLagConfigIndex_Type()
)
flSwitchLagConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchLagConfigIndex.setStatus("current")


class _FlSwitchLagConfigIfIndex_Type(Integer32):
    """Custom type flSwitchLagConfigIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlSwitchLagConfigIfIndex_Type.__name__ = "Integer32"
_FlSwitchLagConfigIfIndex_Object = MibTableColumn
flSwitchLagConfigIfIndex = _FlSwitchLagConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 3, 1, 2),
    _FlSwitchLagConfigIfIndex_Type()
)
flSwitchLagConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchLagConfigIfIndex.setStatus("current")
_FlSwitchLagConfigPortSpeed_Type = ObjectIdentifier
_FlSwitchLagConfigPortSpeed_Object = MibTableColumn
flSwitchLagConfigPortSpeed = _FlSwitchLagConfigPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 3, 1, 3),
    _FlSwitchLagConfigPortSpeed_Type()
)
flSwitchLagConfigPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchLagConfigPortSpeed.setStatus("current")


class _FlSwitchLagConfigPortStatus_Type(Integer32):
    """Custom type flSwitchLagConfigPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_FlSwitchLagConfigPortStatus_Type.__name__ = "Integer32"
_FlSwitchLagConfigPortStatus_Object = MibTableColumn
flSwitchLagConfigPortStatus = _FlSwitchLagConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 3, 1, 4),
    _FlSwitchLagConfigPortStatus_Type()
)
flSwitchLagConfigPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchLagConfigPortStatus.setStatus("current")


class _FlSwitchLagGlobalHashOption_Type(Integer32):
    """Custom type flSwitchLagGlobalHashOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FlSwitchLagGlobalHashOption_Type.__name__ = "Integer32"
_FlSwitchLagGlobalHashOption_Object = MibScalar
flSwitchLagGlobalHashOption = _FlSwitchLagGlobalHashOption_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 8, 4),
    _FlSwitchLagGlobalHashOption_Type()
)
flSwitchLagGlobalHashOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchLagGlobalHashOption.setStatus("current")
_FlSwitchDhcpServerConfig_ObjectIdentity = ObjectIdentity
flSwitchDhcpServerConfig = _FlSwitchDhcpServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9)
)


class _FlSwitchDhcpServerCtrl_Type(Integer32):
    """Custom type flSwitchDhcpServerCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchDhcpServerCtrl_Type.__name__ = "Integer32"
_FlSwitchDhcpServerCtrl_Object = MibScalar
flSwitchDhcpServerCtrl = _FlSwitchDhcpServerCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 1),
    _FlSwitchDhcpServerCtrl_Type()
)
flSwitchDhcpServerCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerCtrl.setStatus("current")
_FlSwitchDhcpServerStartAddress_Type = IpAddress
_FlSwitchDhcpServerStartAddress_Object = MibScalar
flSwitchDhcpServerStartAddress = _FlSwitchDhcpServerStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 2),
    _FlSwitchDhcpServerStartAddress_Type()
)
flSwitchDhcpServerStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerStartAddress.setStatus("current")
_FlSwitchDhcpServerEndAddress_Type = IpAddress
_FlSwitchDhcpServerEndAddress_Object = MibScalar
flSwitchDhcpServerEndAddress = _FlSwitchDhcpServerEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 3),
    _FlSwitchDhcpServerEndAddress_Type()
)
flSwitchDhcpServerEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerEndAddress.setStatus("current")
_FlSwitchDhcpServerSubnetmask_Type = IpAddress
_FlSwitchDhcpServerSubnetmask_Object = MibScalar
flSwitchDhcpServerSubnetmask = _FlSwitchDhcpServerSubnetmask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 4),
    _FlSwitchDhcpServerSubnetmask_Type()
)
flSwitchDhcpServerSubnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerSubnetmask.setStatus("current")
_FlSwitchDhcpServerGatewayAddress_Type = IpAddress
_FlSwitchDhcpServerGatewayAddress_Object = MibScalar
flSwitchDhcpServerGatewayAddress = _FlSwitchDhcpServerGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 5),
    _FlSwitchDhcpServerGatewayAddress_Type()
)
flSwitchDhcpServerGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerGatewayAddress.setStatus("current")
_FlSwitchDhcpServerDnsAddress_Type = IpAddress
_FlSwitchDhcpServerDnsAddress_Object = MibScalar
flSwitchDhcpServerDnsAddress = _FlSwitchDhcpServerDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 6),
    _FlSwitchDhcpServerDnsAddress_Type()
)
flSwitchDhcpServerDnsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerDnsAddress.setStatus("current")


class _FlSwitchDhcpServerLeaseTime_Type(Integer32):
    """Custom type flSwitchDhcpServerLeaseTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3600,
              86400,
              604800,
              2592000)
        )
    )
    namedValues = NamedValues(
        *(("hour", 3600),
          ("day", 86400),
          ("week", 604800),
          ("month", 2592000))
    )


_FlSwitchDhcpServerLeaseTime_Type.__name__ = "Integer32"
_FlSwitchDhcpServerLeaseTime_Object = MibScalar
flSwitchDhcpServerLeaseTime = _FlSwitchDhcpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 7),
    _FlSwitchDhcpServerLeaseTime_Type()
)
flSwitchDhcpServerLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerLeaseTime.setStatus("current")


class _FlSwitchDhcpServerStatus_Type(Integer32):
    """Custom type flSwitchDhcpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notModified", 1),
          ("modified", 2))
    )


_FlSwitchDhcpServerStatus_Type.__name__ = "Integer32"
_FlSwitchDhcpServerStatus_Object = MibScalar
flSwitchDhcpServerStatus = _FlSwitchDhcpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 8),
    _FlSwitchDhcpServerStatus_Type()
)
flSwitchDhcpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpServerStatus.setStatus("current")


class _FlSwitchDhcpServerApply_Type(Integer32):
    """Custom type flSwitchDhcpServerApply based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restore", 1),
          ("apply", 2))
    )


_FlSwitchDhcpServerApply_Type.__name__ = "Integer32"
_FlSwitchDhcpServerApply_Object = MibScalar
flSwitchDhcpServerApply = _FlSwitchDhcpServerApply_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 9),
    _FlSwitchDhcpServerApply_Type()
)
flSwitchDhcpServerApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerApply.setStatus("current")


class _FlSwitchDhcpServerAddressPoolSize_Type(Integer32):
    """Custom type flSwitchDhcpServerAddressPoolSize based on Integer32"""
    defaultValue = 10


_FlSwitchDhcpServerAddressPoolSize_Type.__name__ = "Integer32"
_FlSwitchDhcpServerAddressPoolSize_Object = MibScalar
flSwitchDhcpServerAddressPoolSize = _FlSwitchDhcpServerAddressPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 10),
    _FlSwitchDhcpServerAddressPoolSize_Type()
)
flSwitchDhcpServerAddressPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerAddressPoolSize.setStatus("current")


class _FlSwitchDhcpServerAcceptBootp_Type(Integer32):
    """Custom type flSwitchDhcpServerAcceptBootp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchDhcpServerAcceptBootp_Type.__name__ = "Integer32"
_FlSwitchDhcpServerAcceptBootp_Object = MibScalar
flSwitchDhcpServerAcceptBootp = _FlSwitchDhcpServerAcceptBootp_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 11),
    _FlSwitchDhcpServerAcceptBootp_Type()
)
flSwitchDhcpServerAcceptBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpServerAcceptBootp.setStatus("current")


class _FlSwitchDhcpServerRunning_Type(Integer32):
    """Custom type flSwitchDhcpServerRunning based on Integer32"""
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


_FlSwitchDhcpServerRunning_Type.__name__ = "Integer32"
_FlSwitchDhcpServerRunning_Object = MibScalar
flSwitchDhcpServerRunning = _FlSwitchDhcpServerRunning_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 12),
    _FlSwitchDhcpServerRunning_Type()
)
flSwitchDhcpServerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpServerRunning.setStatus("current")
_FlSwitchDhcpPortLocalService_ObjectIdentity = ObjectIdentity
flSwitchDhcpPortLocalService = _FlSwitchDhcpPortLocalService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100)
)
_FlSwitchDhcpPortLocalTable_Object = MibTable
flSwitchDhcpPortLocalTable = _FlSwitchDhcpPortLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100, 1)
)
if mibBuilder.loadTexts:
    flSwitchDhcpPortLocalTable.setStatus("current")
_FlSwitchDhcpPortLocalEntry_Object = MibTableRow
flSwitchDhcpPortLocalEntry = _FlSwitchDhcpPortLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100, 1, 1)
)
flSwitchDhcpPortLocalEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchDhcpPortLocalIndex"),
)
if mibBuilder.loadTexts:
    flSwitchDhcpPortLocalEntry.setStatus("current")


class _FlSwitchDhcpPortLocalIndex_Type(Integer32):
    """Custom type flSwitchDhcpPortLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlSwitchDhcpPortLocalIndex_Type.__name__ = "Integer32"
_FlSwitchDhcpPortLocalIndex_Object = MibTableColumn
flSwitchDhcpPortLocalIndex = _FlSwitchDhcpPortLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100, 1, 1, 1),
    _FlSwitchDhcpPortLocalIndex_Type()
)
flSwitchDhcpPortLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpPortLocalIndex.setStatus("current")


class _FlSwitchDhcpPortLocalOperation_Type(Integer32):
    """Custom type flSwitchDhcpPortLocalOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchDhcpPortLocalOperation_Type.__name__ = "Integer32"
_FlSwitchDhcpPortLocalOperation_Object = MibTableColumn
flSwitchDhcpPortLocalOperation = _FlSwitchDhcpPortLocalOperation_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100, 1, 1, 2),
    _FlSwitchDhcpPortLocalOperation_Type()
)
flSwitchDhcpPortLocalOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortLocalOperation.setStatus("current")
_FlSwitchDhcpPortLocalLeaseIP_Type = IpAddress
_FlSwitchDhcpPortLocalLeaseIP_Object = MibTableColumn
flSwitchDhcpPortLocalLeaseIP = _FlSwitchDhcpPortLocalLeaseIP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100, 1, 1, 3),
    _FlSwitchDhcpPortLocalLeaseIP_Type()
)
flSwitchDhcpPortLocalLeaseIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortLocalLeaseIP.setStatus("current")
_FlSwitchDhcpPortLocalNetmask_Type = IpAddress
_FlSwitchDhcpPortLocalNetmask_Object = MibTableColumn
flSwitchDhcpPortLocalNetmask = _FlSwitchDhcpPortLocalNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100, 1, 1, 4),
    _FlSwitchDhcpPortLocalNetmask_Type()
)
flSwitchDhcpPortLocalNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortLocalNetmask.setStatus("current")
_FlSwitchDhcpPortLocalGateway_Type = IpAddress
_FlSwitchDhcpPortLocalGateway_Object = MibTableColumn
flSwitchDhcpPortLocalGateway = _FlSwitchDhcpPortLocalGateway_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100, 1, 1, 5),
    _FlSwitchDhcpPortLocalGateway_Type()
)
flSwitchDhcpPortLocalGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortLocalGateway.setStatus("current")
_FlSwitchDhcpPortLocalDns_Type = IpAddress
_FlSwitchDhcpPortLocalDns_Object = MibTableColumn
flSwitchDhcpPortLocalDns = _FlSwitchDhcpPortLocalDns_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100, 1, 1, 6),
    _FlSwitchDhcpPortLocalDns_Type()
)
flSwitchDhcpPortLocalDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortLocalDns.setStatus("current")


class _FlSwitchDhcpPortLocalClear_Type(Integer32):
    """Custom type flSwitchDhcpPortLocalClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("clear", 2))
    )


_FlSwitchDhcpPortLocalClear_Type.__name__ = "Integer32"
_FlSwitchDhcpPortLocalClear_Object = MibScalar
flSwitchDhcpPortLocalClear = _FlSwitchDhcpPortLocalClear_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 100, 2),
    _FlSwitchDhcpPortLocalClear_Type()
)
flSwitchDhcpPortLocalClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortLocalClear.setStatus("current")
_FlSwitchDhcpCurrentLeases_ObjectIdentity = ObjectIdentity
flSwitchDhcpCurrentLeases = _FlSwitchDhcpCurrentLeases_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101)
)
_FlSwitchDhcpCurrentLeaseTable_Object = MibTable
flSwitchDhcpCurrentLeaseTable = _FlSwitchDhcpCurrentLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1)
)
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseTable.setStatus("current")
_FlSwitchDhcpCurrentLeaseEntry_Object = MibTableRow
flSwitchDhcpCurrentLeaseEntry = _FlSwitchDhcpCurrentLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1, 1)
)
flSwitchDhcpCurrentLeaseEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchDhcpCurrentLeaseIP"),
)
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseEntry.setStatus("current")
_FlSwitchDhcpCurrentLeaseIP_Type = IpAddress
_FlSwitchDhcpCurrentLeaseIP_Object = MibTableColumn
flSwitchDhcpCurrentLeaseIP = _FlSwitchDhcpCurrentLeaseIP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1, 1, 1),
    _FlSwitchDhcpCurrentLeaseIP_Type()
)
flSwitchDhcpCurrentLeaseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseIP.setStatus("current")
_FlSwitchDhcpCurrentLeaseClientID_Type = DisplayString
_FlSwitchDhcpCurrentLeaseClientID_Object = MibTableColumn
flSwitchDhcpCurrentLeaseClientID = _FlSwitchDhcpCurrentLeaseClientID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1, 1, 2),
    _FlSwitchDhcpCurrentLeaseClientID_Type()
)
flSwitchDhcpCurrentLeaseClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseClientID.setStatus("current")
_FlSwitchDhcpCurrentLeaseSystemUpTime_Type = TimeTicks
_FlSwitchDhcpCurrentLeaseSystemUpTime_Object = MibTableColumn
flSwitchDhcpCurrentLeaseSystemUpTime = _FlSwitchDhcpCurrentLeaseSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1, 1, 3),
    _FlSwitchDhcpCurrentLeaseSystemUpTime_Type()
)
flSwitchDhcpCurrentLeaseSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseSystemUpTime.setStatus("current")
_FlSwitchDhcpCurrentLeaseTime_Type = OctetString
_FlSwitchDhcpCurrentLeaseTime_Object = MibTableColumn
flSwitchDhcpCurrentLeaseTime = _FlSwitchDhcpCurrentLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1, 1, 4),
    _FlSwitchDhcpCurrentLeaseTime_Type()
)
flSwitchDhcpCurrentLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseTime.setStatus("current")
_FlSwitchDhcpCurrentLeaseDate_Type = OctetString
_FlSwitchDhcpCurrentLeaseDate_Object = MibTableColumn
flSwitchDhcpCurrentLeaseDate = _FlSwitchDhcpCurrentLeaseDate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1, 1, 5),
    _FlSwitchDhcpCurrentLeaseDate_Type()
)
flSwitchDhcpCurrentLeaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseDate.setStatus("current")
_FlSwitchDhcpCurrentLeaseSeconds_Type = Unsigned32
_FlSwitchDhcpCurrentLeaseSeconds_Object = MibTableColumn
flSwitchDhcpCurrentLeaseSeconds = _FlSwitchDhcpCurrentLeaseSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1, 1, 6),
    _FlSwitchDhcpCurrentLeaseSeconds_Type()
)
flSwitchDhcpCurrentLeaseSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseSeconds.setStatus("current")


class _FlSwitchDhcpCurrentLeaseStatus_Type(Integer32):
    """Custom type flSwitchDhcpCurrentLeaseStatus based on Integer32"""
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
        *(("new", 1),
          ("renewed", 2),
          ("processing", 3),
          ("forever", 4),
          ("conflicted", 5),
          ("reserved", 6),
          ("portlocal", 7),
          ("static", 8))
    )


_FlSwitchDhcpCurrentLeaseStatus_Type.__name__ = "Integer32"
_FlSwitchDhcpCurrentLeaseStatus_Object = MibTableColumn
flSwitchDhcpCurrentLeaseStatus = _FlSwitchDhcpCurrentLeaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1, 1, 7),
    _FlSwitchDhcpCurrentLeaseStatus_Type()
)
flSwitchDhcpCurrentLeaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseStatus.setStatus("current")
_FlSwitchDhcpCurrentLeaseLocalPort_Type = Integer32
_FlSwitchDhcpCurrentLeaseLocalPort_Object = MibTableColumn
flSwitchDhcpCurrentLeaseLocalPort = _FlSwitchDhcpCurrentLeaseLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 1, 1, 8),
    _FlSwitchDhcpCurrentLeaseLocalPort_Type()
)
flSwitchDhcpCurrentLeaseLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeaseLocalPort.setStatus("current")


class _FlSwitchDhcpCurrentLeasesRelease_Type(Integer32):
    """Custom type flSwitchDhcpCurrentLeasesRelease based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("release", 2))
    )


_FlSwitchDhcpCurrentLeasesRelease_Type.__name__ = "Integer32"
_FlSwitchDhcpCurrentLeasesRelease_Object = MibScalar
flSwitchDhcpCurrentLeasesRelease = _FlSwitchDhcpCurrentLeasesRelease_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 101, 2),
    _FlSwitchDhcpCurrentLeasesRelease_Type()
)
flSwitchDhcpCurrentLeasesRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpCurrentLeasesRelease.setStatus("current")
_FlSwitchDhcpStaticBinding_ObjectIdentity = ObjectIdentity
flSwitchDhcpStaticBinding = _FlSwitchDhcpStaticBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 102)
)
_FlSwitchDhcpStaticBindingTable_Object = MibTable
flSwitchDhcpStaticBindingTable = _FlSwitchDhcpStaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 102, 1)
)
if mibBuilder.loadTexts:
    flSwitchDhcpStaticBindingTable.setStatus("current")
_FlSwitchDhcpStaticBindingEntry_Object = MibTableRow
flSwitchDhcpStaticBindingEntry = _FlSwitchDhcpStaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 102, 1, 1)
)
flSwitchDhcpStaticBindingEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchDhcpStaticBindingIP"),
)
if mibBuilder.loadTexts:
    flSwitchDhcpStaticBindingEntry.setStatus("current")
_FlSwitchDhcpStaticBindingIP_Type = IpAddress
_FlSwitchDhcpStaticBindingIP_Object = MibTableColumn
flSwitchDhcpStaticBindingIP = _FlSwitchDhcpStaticBindingIP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 102, 1, 1, 1),
    _FlSwitchDhcpStaticBindingIP_Type()
)
flSwitchDhcpStaticBindingIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpStaticBindingIP.setStatus("current")
_FlSwitchDhcpStaticBindingClientID_Type = DisplayString
_FlSwitchDhcpStaticBindingClientID_Object = MibTableColumn
flSwitchDhcpStaticBindingClientID = _FlSwitchDhcpStaticBindingClientID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 102, 1, 1, 2),
    _FlSwitchDhcpStaticBindingClientID_Type()
)
flSwitchDhcpStaticBindingClientID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpStaticBindingClientID.setStatus("current")


class _FlSwitchDhcpStaticBindingClear_Type(Integer32):
    """Custom type flSwitchDhcpStaticBindingClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("clear", 2))
    )


_FlSwitchDhcpStaticBindingClear_Type.__name__ = "Integer32"
_FlSwitchDhcpStaticBindingClear_Object = MibScalar
flSwitchDhcpStaticBindingClear = _FlSwitchDhcpStaticBindingClear_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 102, 2),
    _FlSwitchDhcpStaticBindingClear_Type()
)
flSwitchDhcpStaticBindingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpStaticBindingClear.setStatus("current")
_FlSwitchDhcpPortServerService_ObjectIdentity = ObjectIdentity
flSwitchDhcpPortServerService = _FlSwitchDhcpPortServerService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103)
)
_FlSwitchDhcpPortServerTable_Object = MibTable
flSwitchDhcpPortServerTable = _FlSwitchDhcpPortServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1)
)
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerTable.setStatus("current")
_FlSwitchDhcpPortServerEntry_Object = MibTableRow
flSwitchDhcpPortServerEntry = _FlSwitchDhcpPortServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1, 1)
)
flSwitchDhcpPortServerEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchDhcpPortServerIndex"),
)
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerEntry.setStatus("current")


class _FlSwitchDhcpPortServerIndex_Type(Integer32):
    """Custom type flSwitchDhcpPortServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5096),
    )


_FlSwitchDhcpPortServerIndex_Type.__name__ = "Integer32"
_FlSwitchDhcpPortServerIndex_Object = MibTableColumn
flSwitchDhcpPortServerIndex = _FlSwitchDhcpPortServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1, 1, 1),
    _FlSwitchDhcpPortServerIndex_Type()
)
flSwitchDhcpPortServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerIndex.setStatus("current")


class _FlSwitchDhcpPortServerOperation_Type(Integer32):
    """Custom type flSwitchDhcpPortServerOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchDhcpPortServerOperation_Type.__name__ = "Integer32"
_FlSwitchDhcpPortServerOperation_Object = MibTableColumn
flSwitchDhcpPortServerOperation = _FlSwitchDhcpPortServerOperation_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1, 1, 2),
    _FlSwitchDhcpPortServerOperation_Type()
)
flSwitchDhcpPortServerOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerOperation.setStatus("current")
_FlSwitchDhcpPortServerStartAddress_Type = IpAddress
_FlSwitchDhcpPortServerStartAddress_Object = MibTableColumn
flSwitchDhcpPortServerStartAddress = _FlSwitchDhcpPortServerStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1, 1, 3),
    _FlSwitchDhcpPortServerStartAddress_Type()
)
flSwitchDhcpPortServerStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerStartAddress.setStatus("current")


class _FlSwitchDhcpPortServerAddressPoolSize_Type(Integer32):
    """Custom type flSwitchDhcpPortServerAddressPoolSize based on Integer32"""
    defaultValue = 10


_FlSwitchDhcpPortServerAddressPoolSize_Type.__name__ = "Integer32"
_FlSwitchDhcpPortServerAddressPoolSize_Object = MibTableColumn
flSwitchDhcpPortServerAddressPoolSize = _FlSwitchDhcpPortServerAddressPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1, 1, 4),
    _FlSwitchDhcpPortServerAddressPoolSize_Type()
)
flSwitchDhcpPortServerAddressPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerAddressPoolSize.setStatus("current")
_FlSwitchDhcpPortServerSubnetmask_Type = IpAddress
_FlSwitchDhcpPortServerSubnetmask_Object = MibTableColumn
flSwitchDhcpPortServerSubnetmask = _FlSwitchDhcpPortServerSubnetmask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1, 1, 5),
    _FlSwitchDhcpPortServerSubnetmask_Type()
)
flSwitchDhcpPortServerSubnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerSubnetmask.setStatus("current")
_FlSwitchDhcpPortServerGatewayAddress_Type = IpAddress
_FlSwitchDhcpPortServerGatewayAddress_Object = MibTableColumn
flSwitchDhcpPortServerGatewayAddress = _FlSwitchDhcpPortServerGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1, 1, 6),
    _FlSwitchDhcpPortServerGatewayAddress_Type()
)
flSwitchDhcpPortServerGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerGatewayAddress.setStatus("current")
_FlSwitchDhcpPortServerDnsAddress_Type = IpAddress
_FlSwitchDhcpPortServerDnsAddress_Object = MibTableColumn
flSwitchDhcpPortServerDnsAddress = _FlSwitchDhcpPortServerDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1, 1, 7),
    _FlSwitchDhcpPortServerDnsAddress_Type()
)
flSwitchDhcpPortServerDnsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerDnsAddress.setStatus("current")


class _FlSwitchDhcpPortServerLeaseTime_Type(Integer32):
    """Custom type flSwitchDhcpPortServerLeaseTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3600,
              86400,
              604800,
              2592000)
        )
    )
    namedValues = NamedValues(
        *(("hour", 3600),
          ("day", 86400),
          ("week", 604800),
          ("month", 2592000))
    )


_FlSwitchDhcpPortServerLeaseTime_Type.__name__ = "Integer32"
_FlSwitchDhcpPortServerLeaseTime_Object = MibTableColumn
flSwitchDhcpPortServerLeaseTime = _FlSwitchDhcpPortServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 9, 103, 1, 1, 8),
    _FlSwitchDhcpPortServerLeaseTime_Type()
)
flSwitchDhcpPortServerLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDhcpPortServerLeaseTime.setStatus("current")
_FlSwitchDiffServConfig_ObjectIdentity = ObjectIdentity
flSwitchDiffServConfig = _FlSwitchDiffServConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15)
)


class _FlSwitchDiffServEnable_Type(Integer32):
    """Custom type flSwitchDiffServEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlSwitchDiffServEnable_Type.__name__ = "Integer32"
_FlSwitchDiffServEnable_Object = MibScalar
flSwitchDiffServEnable = _FlSwitchDiffServEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 1),
    _FlSwitchDiffServEnable_Type()
)
flSwitchDiffServEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSwitchDiffServEnable.setStatus("current")
_FlSwitchDiffServConfigTable_Object = MibTable
flSwitchDiffServConfigTable = _FlSwitchDiffServConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2)
)
if mibBuilder.loadTexts:
    flSwitchDiffServConfigTable.setStatus("current")
_FlSwitchDiffServConfigEntry_Object = MibTableRow
flSwitchDiffServConfigEntry = _FlSwitchDiffServConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1)
)
flSwitchDiffServConfigEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flSwitchDiffServCSIndex"),
)
if mibBuilder.loadTexts:
    flSwitchDiffServConfigEntry.setStatus("current")


class _FlSwitchDiffServCSIndex_Type(Integer32):
    """Custom type flSwitchDiffServCSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlSwitchDiffServCSIndex_Type.__name__ = "Integer32"
_FlSwitchDiffServCSIndex_Object = MibTableColumn
flSwitchDiffServCSIndex = _FlSwitchDiffServCSIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 1),
    _FlSwitchDiffServCSIndex_Type()
)
flSwitchDiffServCSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSwitchDiffServCSIndex.setStatus("current")


class _FlSwitchDiffServCSName_Type(DisplayString):
    """Custom type flSwitchDiffServCSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FlSwitchDiffServCSName_Type.__name__ = "DisplayString"
_FlSwitchDiffServCSName_Object = MibTableColumn
flSwitchDiffServCSName = _FlSwitchDiffServCSName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 2),
    _FlSwitchDiffServCSName_Type()
)
flSwitchDiffServCSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServCSName.setStatus("current")


class _FlSwitchDiffServCriType_Type(Integer32):
    """Custom type flSwitchDiffServCriType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethertype", 1),
          ("ipPrecedence", 2),
          ("ipTos", 3))
    )


_FlSwitchDiffServCriType_Type.__name__ = "Integer32"
_FlSwitchDiffServCriType_Object = MibTableColumn
flSwitchDiffServCriType = _FlSwitchDiffServCriType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 3),
    _FlSwitchDiffServCriType_Type()
)
flSwitchDiffServCriType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServCriType.setStatus("current")


class _FlSwitchDiffServCriEtypeValue_Type(Integer32):
    """Custom type flSwitchDiffServCriEtypeValue based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("user-value", 0),
          ("appletalk", 1),
          ("arp", 2),
          ("ibmsna", 3),
          ("ipv4", 4),
          ("ipv6", 5),
          ("ipx", 6),
          ("mpls-multicast", 7),
          ("mpls-unicast", 8),
          ("netbios", 9),
          ("novell", 10),
          ("pppoe", 11),
          ("reverse-arp", 12))
    )


_FlSwitchDiffServCriEtypeValue_Type.__name__ = "Integer32"
_FlSwitchDiffServCriEtypeValue_Object = MibTableColumn
flSwitchDiffServCriEtypeValue = _FlSwitchDiffServCriEtypeValue_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 4),
    _FlSwitchDiffServCriEtypeValue_Type()
)
flSwitchDiffServCriEtypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServCriEtypeValue.setStatus("current")
_FlSwitchDiffServCriEtypeValueCustom_Type = EtypeValue
_FlSwitchDiffServCriEtypeValueCustom_Object = MibTableColumn
flSwitchDiffServCriEtypeValueCustom = _FlSwitchDiffServCriEtypeValueCustom_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 5),
    _FlSwitchDiffServCriEtypeValueCustom_Type()
)
flSwitchDiffServCriEtypeValueCustom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServCriEtypeValueCustom.setStatus("current")


class _FlSwitchDiffServCriIpTosBits_Type(OctetString):
    """Custom type flSwitchDiffServCriIpTosBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_FlSwitchDiffServCriIpTosBits_Type.__name__ = "OctetString"
_FlSwitchDiffServCriIpTosBits_Object = MibTableColumn
flSwitchDiffServCriIpTosBits = _FlSwitchDiffServCriIpTosBits_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 6),
    _FlSwitchDiffServCriIpTosBits_Type()
)
flSwitchDiffServCriIpTosBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServCriIpTosBits.setStatus("current")


class _FlSwitchDiffServCriIpTosMask_Type(OctetString):
    """Custom type flSwitchDiffServCriIpTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_FlSwitchDiffServCriIpTosMask_Type.__name__ = "OctetString"
_FlSwitchDiffServCriIpTosMask_Object = MibTableColumn
flSwitchDiffServCriIpTosMask = _FlSwitchDiffServCriIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 7),
    _FlSwitchDiffServCriIpTosMask_Type()
)
flSwitchDiffServCriIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServCriIpTosMask.setStatus("current")


class _FlSwitchDiffServCriIpPrecedence_Type(Unsigned32):
    """Custom type flSwitchDiffServCriIpPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FlSwitchDiffServCriIpPrecedence_Type.__name__ = "Unsigned32"
_FlSwitchDiffServCriIpPrecedence_Object = MibTableColumn
flSwitchDiffServCriIpPrecedence = _FlSwitchDiffServCriIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 8),
    _FlSwitchDiffServCriIpPrecedence_Type()
)
flSwitchDiffServCriIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServCriIpPrecedence.setStatus("current")


class _FlSwitchDiffServServiceType_Type(Integer32):
    """Custom type flSwitchDiffServServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("assignQueue", 1)
    )


_FlSwitchDiffServServiceType_Type.__name__ = "Integer32"
_FlSwitchDiffServServiceType_Object = MibTableColumn
flSwitchDiffServServiceType = _FlSwitchDiffServServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 9),
    _FlSwitchDiffServServiceType_Type()
)
flSwitchDiffServServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServServiceType.setStatus("current")
_FlSwitchDiffServServiceAssignQueueID_Type = Unsigned32
_FlSwitchDiffServServiceAssignQueueID_Object = MibTableColumn
flSwitchDiffServServiceAssignQueueID = _FlSwitchDiffServServiceAssignQueueID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 10),
    _FlSwitchDiffServServiceAssignQueueID_Type()
)
flSwitchDiffServServiceAssignQueueID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServServiceAssignQueueID.setStatus("current")


class _FlSwitchDiffServIncludedPorts_Type(OctetString):
    """Custom type flSwitchDiffServIncludedPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FlSwitchDiffServIncludedPorts_Type.__name__ = "OctetString"
_FlSwitchDiffServIncludedPorts_Object = MibTableColumn
flSwitchDiffServIncludedPorts = _FlSwitchDiffServIncludedPorts_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 11),
    _FlSwitchDiffServIncludedPorts_Type()
)
flSwitchDiffServIncludedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServIncludedPorts.setStatus("current")
_FlSwitchDiffServRowStatus_Type = RowStatus
_FlSwitchDiffServRowStatus_Object = MibTableColumn
flSwitchDiffServRowStatus = _FlSwitchDiffServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 15, 15, 2, 1, 12),
    _FlSwitchDiffServRowStatus_Type()
)
flSwitchDiffServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flSwitchDiffServRowStatus.setStatus("current")
_FlWorkSecGateway_ObjectIdentity = ObjectIdentity
flWorkSecGateway = _FlWorkSecGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 20)
)
_FlWorkSecurityCtrl_ObjectIdentity = ObjectIdentity
flWorkSecurityCtrl = _FlWorkSecurityCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 20, 1)
)
_FlWorkSecurityCtrlClientAuth_ObjectIdentity = ObjectIdentity
flWorkSecurityCtrlClientAuth = _FlWorkSecurityCtrlClientAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 20, 1, 5)
)


class _FlWorkSecurityCtrlGenSecurityContext_Type(Integer32):
    """Custom type flWorkSecurityCtrlGenSecurityContext based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notGenerate", 1),
          ("generate", 2))
    )


_FlWorkSecurityCtrlGenSecurityContext_Type.__name__ = "Integer32"
_FlWorkSecurityCtrlGenSecurityContext_Object = MibScalar
flWorkSecurityCtrlGenSecurityContext = _FlWorkSecurityCtrlGenSecurityContext_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 20, 1, 5, 3),
    _FlWorkSecurityCtrlGenSecurityContext_Type()
)
flWorkSecurityCtrlGenSecurityContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkSecurityCtrlGenSecurityContext.setStatus("current")
_FlWorkTimeSynch_ObjectIdentity = ObjectIdentity
flWorkTimeSynch = _FlWorkTimeSynch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21)
)
_FlWorkTimeSynchSntp_ObjectIdentity = ObjectIdentity
flWorkTimeSynchSntp = _FlWorkTimeSynchSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1)
)


class _FlWorkTimeSynchSntpEnable_Type(Integer32):
    """Custom type flWorkTimeSynchSntpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkTimeSynchSntpEnable_Type.__name__ = "Integer32"
_FlWorkTimeSynchSntpEnable_Object = MibScalar
flWorkTimeSynchSntpEnable = _FlWorkTimeSynchSntpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 1),
    _FlWorkTimeSynchSntpEnable_Type()
)
flWorkTimeSynchSntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpEnable.setStatus("current")


class _FlWorkTimeSynchSntpMode_Type(Integer32):
    """Custom type flWorkTimeSynchSntpMode based on Integer32"""
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
        *(("unicast", 1),
          ("broadcast", 2),
          ("manycast", 3))
    )


_FlWorkTimeSynchSntpMode_Type.__name__ = "Integer32"
_FlWorkTimeSynchSntpMode_Object = MibScalar
flWorkTimeSynchSntpMode = _FlWorkTimeSynchSntpMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 2),
    _FlWorkTimeSynchSntpMode_Type()
)
flWorkTimeSynchSntpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpMode.setStatus("current")


class _FlWorkTimeSynchSntpPollInterval_Type(Integer32):
    """Custom type flWorkTimeSynchSntpPollInterval based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_FlWorkTimeSynchSntpPollInterval_Type.__name__ = "Integer32"
_FlWorkTimeSynchSntpPollInterval_Object = MibScalar
flWorkTimeSynchSntpPollInterval = _FlWorkTimeSynchSntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 3),
    _FlWorkTimeSynchSntpPollInterval_Type()
)
flWorkTimeSynchSntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpPollInterval.setStatus("current")
_FlWorkTimeSynchSntpServerIpAddress_Type = IpAddress
_FlWorkTimeSynchSntpServerIpAddress_Object = MibScalar
flWorkTimeSynchSntpServerIpAddress = _FlWorkTimeSynchSntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 4),
    _FlWorkTimeSynchSntpServerIpAddress_Type()
)
flWorkTimeSynchSntpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpServerIpAddress.setStatus("current")
_FlWorkTimeSynchSntpBackupServerIpAddress_Type = IpAddress
_FlWorkTimeSynchSntpBackupServerIpAddress_Object = MibScalar
flWorkTimeSynchSntpBackupServerIpAddress = _FlWorkTimeSynchSntpBackupServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 5),
    _FlWorkTimeSynchSntpBackupServerIpAddress_Type()
)
flWorkTimeSynchSntpBackupServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpBackupServerIpAddress.setStatus("current")
_FlWorkTimeSynchSntpBroadcastIpAddress_Type = IpAddress
_FlWorkTimeSynchSntpBroadcastIpAddress_Object = MibScalar
flWorkTimeSynchSntpBroadcastIpAddress = _FlWorkTimeSynchSntpBroadcastIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 6),
    _FlWorkTimeSynchSntpBroadcastIpAddress_Type()
)
flWorkTimeSynchSntpBroadcastIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpBroadcastIpAddress.setStatus("current")


class _FlWorkTimeSynchSntpStratum_Type(Integer32):
    """Custom type flWorkTimeSynchSntpStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FlWorkTimeSynchSntpStratum_Type.__name__ = "Integer32"
_FlWorkTimeSynchSntpStratum_Object = MibScalar
flWorkTimeSynchSntpStratum = _FlWorkTimeSynchSntpStratum_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 7),
    _FlWorkTimeSynchSntpStratum_Type()
)
flWorkTimeSynchSntpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpStratum.setStatus("current")
_FlWorkTimeSynchSntpTime_Type = OctetString
_FlWorkTimeSynchSntpTime_Object = MibScalar
flWorkTimeSynchSntpTime = _FlWorkTimeSynchSntpTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 8),
    _FlWorkTimeSynchSntpTime_Type()
)
flWorkTimeSynchSntpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpTime.setStatus("current")
_FlWorkTimeSynchSntpDate_Type = OctetString
_FlWorkTimeSynchSntpDate_Object = MibScalar
flWorkTimeSynchSntpDate = _FlWorkTimeSynchSntpDate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 9),
    _FlWorkTimeSynchSntpDate_Type()
)
flWorkTimeSynchSntpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpDate.setStatus("current")
_FlWorkTimeSynchSntpSeconds_Type = Unsigned32
_FlWorkTimeSynchSntpSeconds_Object = MibScalar
flWorkTimeSynchSntpSeconds = _FlWorkTimeSynchSntpSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 10),
    _FlWorkTimeSynchSntpSeconds_Type()
)
flWorkTimeSynchSntpSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpSeconds.setStatus("current")
_FlWorkTimeSynchSntpFractionalSeconds_Type = Unsigned32
_FlWorkTimeSynchSntpFractionalSeconds_Object = MibScalar
flWorkTimeSynchSntpFractionalSeconds = _FlWorkTimeSynchSntpFractionalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 11),
    _FlWorkTimeSynchSntpFractionalSeconds_Type()
)
flWorkTimeSynchSntpFractionalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpFractionalSeconds.setStatus("current")


class _FlWorkTimeSynchSntpUtcOffset_Type(Integer32):
    """Custom type flWorkTimeSynchSntpUtcOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_FlWorkTimeSynchSntpUtcOffset_Type.__name__ = "Integer32"
_FlWorkTimeSynchSntpUtcOffset_Object = MibScalar
flWorkTimeSynchSntpUtcOffset = _FlWorkTimeSynchSntpUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 12),
    _FlWorkTimeSynchSntpUtcOffset_Type()
)
flWorkTimeSynchSntpUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpUtcOffset.setStatus("current")


class _FlWorkTimeSynchSntpServerDesc_Type(DisplayString):
    """Custom type flWorkTimeSynchSntpServerDesc based on DisplayString"""
    defaultValue = OctetString("")


_FlWorkTimeSynchSntpServerDesc_Type.__name__ = "DisplayString"
_FlWorkTimeSynchSntpServerDesc_Object = MibScalar
flWorkTimeSynchSntpServerDesc = _FlWorkTimeSynchSntpServerDesc_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 24),
    _FlWorkTimeSynchSntpServerDesc_Type()
)
flWorkTimeSynchSntpServerDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpServerDesc.setStatus("current")


class _FlWorkTimeSynchSntpBackupServerDesc_Type(DisplayString):
    """Custom type flWorkTimeSynchSntpBackupServerDesc based on DisplayString"""
    defaultValue = OctetString("")


_FlWorkTimeSynchSntpBackupServerDesc_Type.__name__ = "DisplayString"
_FlWorkTimeSynchSntpBackupServerDesc_Object = MibScalar
flWorkTimeSynchSntpBackupServerDesc = _FlWorkTimeSynchSntpBackupServerDesc_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 25),
    _FlWorkTimeSynchSntpBackupServerDesc_Type()
)
flWorkTimeSynchSntpBackupServerDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpBackupServerDesc.setStatus("current")


class _FlWorkTimeSynchSntpServerName_Type(DisplayString):
    """Custom type flWorkTimeSynchSntpServerName based on DisplayString"""
    defaultValue = OctetString("")


_FlWorkTimeSynchSntpServerName_Type.__name__ = "DisplayString"
_FlWorkTimeSynchSntpServerName_Object = MibScalar
flWorkTimeSynchSntpServerName = _FlWorkTimeSynchSntpServerName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 26),
    _FlWorkTimeSynchSntpServerName_Type()
)
flWorkTimeSynchSntpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpServerName.setStatus("current")


class _FlWorkTimeSynchSntpBackupServerName_Type(DisplayString):
    """Custom type flWorkTimeSynchSntpBackupServerName based on DisplayString"""
    defaultValue = OctetString("")


_FlWorkTimeSynchSntpBackupServerName_Type.__name__ = "DisplayString"
_FlWorkTimeSynchSntpBackupServerName_Object = MibScalar
flWorkTimeSynchSntpBackupServerName = _FlWorkTimeSynchSntpBackupServerName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 1, 27),
    _FlWorkTimeSynchSntpBackupServerName_Type()
)
flWorkTimeSynchSntpBackupServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchSntpBackupServerName.setStatus("current")
_FlWorkTimeSynchRTC_ObjectIdentity = ObjectIdentity
flWorkTimeSynchRTC = _FlWorkTimeSynchRTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 2)
)
_FlWorkTimeSynchRTCDateTime_Type = OctetString
_FlWorkTimeSynchRTCDateTime_Object = MibScalar
flWorkTimeSynchRTCDateTime = _FlWorkTimeSynchRTCDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 2, 1),
    _FlWorkTimeSynchRTCDateTime_Type()
)
flWorkTimeSynchRTCDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchRTCDateTime.setStatus("current")
_FlWorkTimeSynchRTCSeconds_Type = Unsigned32
_FlWorkTimeSynchRTCSeconds_Object = MibScalar
flWorkTimeSynchRTCSeconds = _FlWorkTimeSynchRTCSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 2, 2),
    _FlWorkTimeSynchRTCSeconds_Type()
)
flWorkTimeSynchRTCSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchRTCSeconds.setStatus("current")
_FlWorkTimeSynchPTP_ObjectIdentity = ObjectIdentity
flWorkTimeSynchPTP = _FlWorkTimeSynchPTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 3)
)
_FlWorkTimeSynchPTPPortTable_Object = MibTable
flWorkTimeSynchPTPPortTable = _FlWorkTimeSynchPTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 3, 1)
)
if mibBuilder.loadTexts:
    flWorkTimeSynchPTPPortTable.setStatus("current")
_FlWorkTimeSynchPTPPortEntry_Object = MibTableRow
flWorkTimeSynchPTPPortEntry = _FlWorkTimeSynchPTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 3, 1, 1)
)
flWorkTimeSynchPTPPortEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkTimeSynchPTPPortIndex"),
)
if mibBuilder.loadTexts:
    flWorkTimeSynchPTPPortEntry.setStatus("current")


class _FlWorkTimeSynchPTPPortIndex_Type(Integer32):
    """Custom type flWorkTimeSynchPTPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FlWorkTimeSynchPTPPortIndex_Type.__name__ = "Integer32"
_FlWorkTimeSynchPTPPortIndex_Object = MibTableColumn
flWorkTimeSynchPTPPortIndex = _FlWorkTimeSynchPTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 3, 1, 1, 1),
    _FlWorkTimeSynchPTPPortIndex_Type()
)
flWorkTimeSynchPTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkTimeSynchPTPPortIndex.setStatus("current")


class _FlWorkTimeSynchPTPPortAdminStatus_Type(Integer32):
    """Custom type flWorkTimeSynchPTPPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rxAndTx", 1),
          ("rxOnly", 2))
    )


_FlWorkTimeSynchPTPPortAdminStatus_Type.__name__ = "Integer32"
_FlWorkTimeSynchPTPPortAdminStatus_Object = MibTableColumn
flWorkTimeSynchPTPPortAdminStatus = _FlWorkTimeSynchPTPPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 21, 3, 1, 1, 2),
    _FlWorkTimeSynchPTPPortAdminStatus_Type()
)
flWorkTimeSynchPTPPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkTimeSynchPTPPortAdminStatus.setStatus("current")
_FlWorkWlan_ObjectIdentity = ObjectIdentity
flWorkWlan = _FlWorkWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22)
)


class _FlWorkWlanOpMode_Type(Integer32):
    """Custom type flWorkWlanOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("transbridge", 1)
    )


_FlWorkWlanOpMode_Type.__name__ = "Integer32"
_FlWorkWlanOpMode_Object = MibScalar
flWorkWlanOpMode = _FlWorkWlanOpMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 10),
    _FlWorkWlanOpMode_Type()
)
flWorkWlanOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanOpMode.setStatus("current")


class _FlWorkWlanSetOnlyMode_Type(Integer32):
    """Custom type flWorkWlanSetOnlyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FlWorkWlanSetOnlyMode_Type.__name__ = "Integer32"
_FlWorkWlanSetOnlyMode_Object = MibScalar
flWorkWlanSetOnlyMode = _FlWorkWlanSetOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 11),
    _FlWorkWlanSetOnlyMode_Type()
)
flWorkWlanSetOnlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanSetOnlyMode.setStatus("current")


class _FlWorkWlanCountry_Type(OctetString):
    """Custom type flWorkWlanCountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_FlWorkWlanCountry_Type.__name__ = "OctetString"
_FlWorkWlanCountry_Object = MibScalar
flWorkWlanCountry = _FlWorkWlanCountry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 12),
    _FlWorkWlanCountry_Type()
)
flWorkWlanCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanCountry.setStatus("current")
_FlWorkWlanIf1_ObjectIdentity = ObjectIdentity
flWorkWlanIf1 = _FlWorkWlanIf1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20)
)
_FlWorkWlanIf1Parameter_ObjectIdentity = ObjectIdentity
flWorkWlanIf1Parameter = _FlWorkWlanIf1Parameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1)
)
_FlWorkWlanIf1ParamState_Type = EnabledDisabledStatus
_FlWorkWlanIf1ParamState_Object = MibScalar
flWorkWlanIf1ParamState = _FlWorkWlanIf1ParamState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 1),
    _FlWorkWlanIf1ParamState_Type()
)
flWorkWlanIf1ParamState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1ParamState.setStatus("current")
_FlWorkWlanIf1ParamOpMode_Type = OpModeType
_FlWorkWlanIf1ParamOpMode_Object = MibScalar
flWorkWlanIf1ParamOpMode = _FlWorkWlanIf1ParamOpMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 2),
    _FlWorkWlanIf1ParamOpMode_Type()
)
flWorkWlanIf1ParamOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1ParamOpMode.setStatus("current")


class _FlWorkWlanIf1ParamSSID_Type(OctetString):
    """Custom type flWorkWlanIf1ParamSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FlWorkWlanIf1ParamSSID_Type.__name__ = "OctetString"
_FlWorkWlanIf1ParamSSID_Object = MibScalar
flWorkWlanIf1ParamSSID = _FlWorkWlanIf1ParamSSID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 3),
    _FlWorkWlanIf1ParamSSID_Type()
)
flWorkWlanIf1ParamSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1ParamSSID.setStatus("current")


class _FlWorkWlanIf1ParamMode_Type(Integer32):
    """Custom type flWorkWlanIf1ParamMode based on Integer32"""
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
        *(("abg", 0),
          ("a", 1),
          ("b", 2),
          ("bg", 3),
          ("an", 4),
          ("gn", 5))
    )


_FlWorkWlanIf1ParamMode_Type.__name__ = "Integer32"
_FlWorkWlanIf1ParamMode_Object = MibScalar
flWorkWlanIf1ParamMode = _FlWorkWlanIf1ParamMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 4),
    _FlWorkWlanIf1ParamMode_Type()
)
flWorkWlanIf1ParamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1ParamMode.setStatus("current")


class _FlWorkWlanIf1ParamChannel_Type(Integer32):
    """Custom type flWorkWlanIf1ParamChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkWlanIf1ParamChannel_Type.__name__ = "Integer32"
_FlWorkWlanIf1ParamChannel_Object = MibScalar
flWorkWlanIf1ParamChannel = _FlWorkWlanIf1ParamChannel_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 5),
    _FlWorkWlanIf1ParamChannel_Type()
)
flWorkWlanIf1ParamChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1ParamChannel.setStatus("current")
_FlWorkWlanIf1ParamOutdoor_Type = EnabledDisabledStatus
_FlWorkWlanIf1ParamOutdoor_Object = MibScalar
flWorkWlanIf1ParamOutdoor = _FlWorkWlanIf1ParamOutdoor_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 6),
    _FlWorkWlanIf1ParamOutdoor_Type()
)
flWorkWlanIf1ParamOutdoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1ParamOutdoor.setStatus("current")


class _FlWorkWlanIf1AntennaOutput_Type(Integer32):
    """Custom type flWorkWlanIf1AntennaOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FlWorkWlanIf1AntennaOutput_Type.__name__ = "Integer32"
_FlWorkWlanIf1AntennaOutput_Object = MibScalar
flWorkWlanIf1AntennaOutput = _FlWorkWlanIf1AntennaOutput_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 7),
    _FlWorkWlanIf1AntennaOutput_Type()
)
flWorkWlanIf1AntennaOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1AntennaOutput.setStatus("current")


class _FlWorkWlanIf1OutputPower_Type(Integer32):
    """Custom type flWorkWlanIf1OutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 23),
    )


_FlWorkWlanIf1OutputPower_Type.__name__ = "Integer32"
_FlWorkWlanIf1OutputPower_Object = MibScalar
flWorkWlanIf1OutputPower = _FlWorkWlanIf1OutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 8),
    _FlWorkWlanIf1OutputPower_Type()
)
flWorkWlanIf1OutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1OutputPower.setStatus("current")


class _FlWorkWlanIf1STBC_Type(Integer32):
    """Custom type flWorkWlanIf1STBC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkWlanIf1STBC_Type.__name__ = "Integer32"
_FlWorkWlanIf1STBC_Object = MibScalar
flWorkWlanIf1STBC = _FlWorkWlanIf1STBC_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 9),
    _FlWorkWlanIf1STBC_Type()
)
flWorkWlanIf1STBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1STBC.setStatus("current")


class _FlWorkWlanIf1Fragmentation_Type(Integer32):
    """Custom type flWorkWlanIf1Fragmentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2600),
    )


_FlWorkWlanIf1Fragmentation_Type.__name__ = "Integer32"
_FlWorkWlanIf1Fragmentation_Object = MibScalar
flWorkWlanIf1Fragmentation = _FlWorkWlanIf1Fragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 10),
    _FlWorkWlanIf1Fragmentation_Type()
)
flWorkWlanIf1Fragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1Fragmentation.setStatus("current")


class _FlWorkWlanIf1RtsCts_Type(Integer32):
    """Custom type flWorkWlanIf1RtsCts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2600),
    )


_FlWorkWlanIf1RtsCts_Type.__name__ = "Integer32"
_FlWorkWlanIf1RtsCts_Object = MibScalar
flWorkWlanIf1RtsCts = _FlWorkWlanIf1RtsCts_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 11),
    _FlWorkWlanIf1RtsCts_Type()
)
flWorkWlanIf1RtsCts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1RtsCts.setStatus("current")


class _FlWorkWlanIf1LongDistance_Type(Integer32):
    """Custom type flWorkWlanIf1LongDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 50000),
    )


_FlWorkWlanIf1LongDistance_Type.__name__ = "Integer32"
_FlWorkWlanIf1LongDistance_Object = MibScalar
flWorkWlanIf1LongDistance = _FlWorkWlanIf1LongDistance_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 12),
    _FlWorkWlanIf1LongDistance_Type()
)
flWorkWlanIf1LongDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1LongDistance.setStatus("current")
_FlWorkWlanIf1ScbMacAddress_Type = MacAddress
_FlWorkWlanIf1ScbMacAddress_Object = MibScalar
flWorkWlanIf1ScbMacAddress = _FlWorkWlanIf1ScbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 13),
    _FlWorkWlanIf1ScbMacAddress_Type()
)
flWorkWlanIf1ScbMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1ScbMacAddress.setStatus("current")


class _FlWorkWlanIf1ScbManMacMode_Type(Integer32):
    """Custom type flWorkWlanIf1ScbManMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FlWorkWlanIf1ScbManMacMode_Type.__name__ = "Integer32"
_FlWorkWlanIf1ScbManMacMode_Object = MibScalar
flWorkWlanIf1ScbManMacMode = _FlWorkWlanIf1ScbManMacMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 14),
    _FlWorkWlanIf1ScbManMacMode_Type()
)
flWorkWlanIf1ScbManMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1ScbManMacMode.setStatus("current")


class _FlWorkWlanIf1IAPP_Type(Integer32):
    """Custom type flWorkWlanIf1IAPP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FlWorkWlanIf1IAPP_Type.__name__ = "Integer32"
_FlWorkWlanIf1IAPP_Object = MibScalar
flWorkWlanIf1IAPP = _FlWorkWlanIf1IAPP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 15),
    _FlWorkWlanIf1IAPP_Type()
)
flWorkWlanIf1IAPP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1IAPP.setStatus("current")
_FlWorkWlanIf1MachineAdmin_ObjectIdentity = ObjectIdentity
flWorkWlanIf1MachineAdmin = _FlWorkWlanIf1MachineAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 16)
)


class _FlWorkWlanIf1MachineAdminSSID_Type(OctetString):
    """Custom type flWorkWlanIf1MachineAdminSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FlWorkWlanIf1MachineAdminSSID_Type.__name__ = "OctetString"
_FlWorkWlanIf1MachineAdminSSID_Object = MibScalar
flWorkWlanIf1MachineAdminSSID = _FlWorkWlanIf1MachineAdminSSID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 16, 1),
    _FlWorkWlanIf1MachineAdminSSID_Type()
)
flWorkWlanIf1MachineAdminSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1MachineAdminSSID.setStatus("current")


class _FlWorkWlanIf1MachineAdminPsk_Type(OctetString):
    """Custom type flWorkWlanIf1MachineAdminPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_FlWorkWlanIf1MachineAdminPsk_Type.__name__ = "OctetString"
_FlWorkWlanIf1MachineAdminPsk_Object = MibScalar
flWorkWlanIf1MachineAdminPsk = _FlWorkWlanIf1MachineAdminPsk_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 16, 2),
    _FlWorkWlanIf1MachineAdminPsk_Type()
)
flWorkWlanIf1MachineAdminPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1MachineAdminPsk.setStatus("current")
_FlWorkWlanIf1MachineAdminIp_Type = IpAddress
_FlWorkWlanIf1MachineAdminIp_Object = MibScalar
flWorkWlanIf1MachineAdminIp = _FlWorkWlanIf1MachineAdminIp_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 1, 16, 3),
    _FlWorkWlanIf1MachineAdminIp_Type()
)
flWorkWlanIf1MachineAdminIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1MachineAdminIp.setStatus("current")
_FlWorkWlanIf1Security_ObjectIdentity = ObjectIdentity
flWorkWlanIf1Security = _FlWorkWlanIf1Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 2)
)


class _FlWorkWlanIf1SecMode_Type(Integer32):
    """Custom type flWorkWlanIf1SecMode based on Integer32"""
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
        *(("none", 0),
          ("wpa-psk", 1),
          ("wep64", 2),
          ("wep128", 3),
          ("wpa2-psk", 4),
          ("wpa2-eap", 5))
    )


_FlWorkWlanIf1SecMode_Type.__name__ = "Integer32"
_FlWorkWlanIf1SecMode_Object = MibScalar
flWorkWlanIf1SecMode = _FlWorkWlanIf1SecMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 2, 1),
    _FlWorkWlanIf1SecMode_Type()
)
flWorkWlanIf1SecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1SecMode.setStatus("current")


class _FlWorkWlanIf1SecWpaEncryptionAlgorithm_Type(Integer32):
    """Custom type flWorkWlanIf1SecWpaEncryptionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("both", 3))
    )


_FlWorkWlanIf1SecWpaEncryptionAlgorithm_Type.__name__ = "Integer32"
_FlWorkWlanIf1SecWpaEncryptionAlgorithm_Object = MibScalar
flWorkWlanIf1SecWpaEncryptionAlgorithm = _FlWorkWlanIf1SecWpaEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 2, 2),
    _FlWorkWlanIf1SecWpaEncryptionAlgorithm_Type()
)
flWorkWlanIf1SecWpaEncryptionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1SecWpaEncryptionAlgorithm.setStatus("current")


class _FlWorkWlanIf1SecWpaPsk_Type(OctetString):
    """Custom type flWorkWlanIf1SecWpaPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_FlWorkWlanIf1SecWpaPsk_Type.__name__ = "OctetString"
_FlWorkWlanIf1SecWpaPsk_Object = MibScalar
flWorkWlanIf1SecWpaPsk = _FlWorkWlanIf1SecWpaPsk_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 2, 3),
    _FlWorkWlanIf1SecWpaPsk_Type()
)
flWorkWlanIf1SecWpaPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1SecWpaPsk.setStatus("current")


class _FlWorkWlanIf1SecWepAuthType_Type(Integer32):
    """Custom type flWorkWlanIf1SecWepAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open-system", 1),
          ("shared-key", 2),
          ("automatic", 3))
    )


_FlWorkWlanIf1SecWepAuthType_Type.__name__ = "Integer32"
_FlWorkWlanIf1SecWepAuthType_Object = MibScalar
flWorkWlanIf1SecWepAuthType = _FlWorkWlanIf1SecWepAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 2, 4),
    _FlWorkWlanIf1SecWepAuthType_Type()
)
flWorkWlanIf1SecWepAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1SecWepAuthType.setStatus("current")


class _FlWorkWlanIf1SecWepKeyEncoding_Type(Integer32):
    """Custom type flWorkWlanIf1SecWepKeyEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hex", 0),
          ("ascii", 1))
    )


_FlWorkWlanIf1SecWepKeyEncoding_Type.__name__ = "Integer32"
_FlWorkWlanIf1SecWepKeyEncoding_Object = MibScalar
flWorkWlanIf1SecWepKeyEncoding = _FlWorkWlanIf1SecWepKeyEncoding_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 2, 5),
    _FlWorkWlanIf1SecWepKeyEncoding_Type()
)
flWorkWlanIf1SecWepKeyEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1SecWepKeyEncoding.setStatus("current")


class _FlWorkWlanIf1SecWepKey_Type(OctetString):
    """Custom type flWorkWlanIf1SecWepKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 26),
    )


_FlWorkWlanIf1SecWepKey_Type.__name__ = "OctetString"
_FlWorkWlanIf1SecWepKey_Object = MibScalar
flWorkWlanIf1SecWepKey = _FlWorkWlanIf1SecWepKey_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 2, 6),
    _FlWorkWlanIf1SecWepKey_Type()
)
flWorkWlanIf1SecWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1SecWepKey.setStatus("current")
_FlWorkWlanIf1FastRoaming_ObjectIdentity = ObjectIdentity
flWorkWlanIf1FastRoaming = _FlWorkWlanIf1FastRoaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 3)
)
_FlWorkWlanIf1FastRoamingTable_Object = MibTable
flWorkWlanIf1FastRoamingTable = _FlWorkWlanIf1FastRoamingTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 3, 1)
)
if mibBuilder.loadTexts:
    flWorkWlanIf1FastRoamingTable.setStatus("current")
_FlWorkWlanIf1FastRoamingEntry_Object = MibTableRow
flWorkWlanIf1FastRoamingEntry = _FlWorkWlanIf1FastRoamingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 3, 1, 1)
)
flWorkWlanIf1FastRoamingEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkWlanIf1FastRoamingEntryIdx"),
)
if mibBuilder.loadTexts:
    flWorkWlanIf1FastRoamingEntry.setStatus("current")


class _FlWorkWlanIf1FastRoamingEntryIdx_Type(Integer32):
    """Custom type flWorkWlanIf1FastRoamingEntryIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_FlWorkWlanIf1FastRoamingEntryIdx_Type.__name__ = "Integer32"
_FlWorkWlanIf1FastRoamingEntryIdx_Object = MibTableColumn
flWorkWlanIf1FastRoamingEntryIdx = _FlWorkWlanIf1FastRoamingEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 3, 1, 1, 1),
    _FlWorkWlanIf1FastRoamingEntryIdx_Type()
)
flWorkWlanIf1FastRoamingEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkWlanIf1FastRoamingEntryIdx.setStatus("current")


class _FlWorkWlanIf1FastRoamingEntryThreshold_Type(Integer32):
    """Custom type flWorkWlanIf1FastRoamingEntryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_FlWorkWlanIf1FastRoamingEntryThreshold_Type.__name__ = "Integer32"
_FlWorkWlanIf1FastRoamingEntryThreshold_Object = MibTableColumn
flWorkWlanIf1FastRoamingEntryThreshold = _FlWorkWlanIf1FastRoamingEntryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 3, 1, 1, 2),
    _FlWorkWlanIf1FastRoamingEntryThreshold_Type()
)
flWorkWlanIf1FastRoamingEntryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1FastRoamingEntryThreshold.setStatus("current")


class _FlWorkWlanIf1FastRoamingEntryChannel_Type(Integer32):
    """Custom type flWorkWlanIf1FastRoamingEntryChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkWlanIf1FastRoamingEntryChannel_Type.__name__ = "Integer32"
_FlWorkWlanIf1FastRoamingEntryChannel_Object = MibTableColumn
flWorkWlanIf1FastRoamingEntryChannel = _FlWorkWlanIf1FastRoamingEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 3, 1, 1, 3),
    _FlWorkWlanIf1FastRoamingEntryChannel_Type()
)
flWorkWlanIf1FastRoamingEntryChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1FastRoamingEntryChannel.setStatus("current")
_FlWorkWlanIf1FastRoamingEntryAddress_Type = MacAddress
_FlWorkWlanIf1FastRoamingEntryAddress_Object = MibTableColumn
flWorkWlanIf1FastRoamingEntryAddress = _FlWorkWlanIf1FastRoamingEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 3, 1, 1, 4),
    _FlWorkWlanIf1FastRoamingEntryAddress_Type()
)
flWorkWlanIf1FastRoamingEntryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1FastRoamingEntryAddress.setStatus("current")
_FlWorkWlanIf1FastRoamingEnabled_Type = EnabledDisabledStatus
_FlWorkWlanIf1FastRoamingEnabled_Object = MibScalar
flWorkWlanIf1FastRoamingEnabled = _FlWorkWlanIf1FastRoamingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 3, 2),
    _FlWorkWlanIf1FastRoamingEnabled_Type()
)
flWorkWlanIf1FastRoamingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1FastRoamingEnabled.setStatus("current")


class _FlWorkWlanIf1FastRoamToAP_Type(Integer32):
    """Custom type flWorkWlanIf1FastRoamToAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_FlWorkWlanIf1FastRoamToAP_Type.__name__ = "Integer32"
_FlWorkWlanIf1FastRoamToAP_Object = MibScalar
flWorkWlanIf1FastRoamToAP = _FlWorkWlanIf1FastRoamToAP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 3, 3),
    _FlWorkWlanIf1FastRoamToAP_Type()
)
flWorkWlanIf1FastRoamToAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1FastRoamToAP.setStatus("current")
_FlWorkWlanIf1Mcast_ObjectIdentity = ObjectIdentity
flWorkWlanIf1Mcast = _FlWorkWlanIf1Mcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4)
)


class _FlWorkWlanIf1McastEnhance_Type(Integer32):
    """Custom type flWorkWlanIf1McastEnhance based on Integer32"""
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
        *(("disable", 0),
          ("tunneling", 1),
          ("translating", 2),
          ("adv-tunnel", 3))
    )


_FlWorkWlanIf1McastEnhance_Type.__name__ = "Integer32"
_FlWorkWlanIf1McastEnhance_Object = MibScalar
flWorkWlanIf1McastEnhance = _FlWorkWlanIf1McastEnhance_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 1),
    _FlWorkWlanIf1McastEnhance_Type()
)
flWorkWlanIf1McastEnhance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastEnhance.setStatus("current")


class _FlWorkWlanIf1McastDrop_Type(Integer32):
    """Custom type flWorkWlanIf1McastDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("learned", 1),
          ("all", 2))
    )


_FlWorkWlanIf1McastDrop_Type.__name__ = "Integer32"
_FlWorkWlanIf1McastDrop_Object = MibScalar
flWorkWlanIf1McastDrop = _FlWorkWlanIf1McastDrop_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 2),
    _FlWorkWlanIf1McastDrop_Type()
)
flWorkWlanIf1McastDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastDrop.setStatus("current")
_FlWorkWlanIf1McastAutoAdd_Type = EnabledDisabledStatus
_FlWorkWlanIf1McastAutoAdd_Object = MibScalar
flWorkWlanIf1McastAutoAdd = _FlWorkWlanIf1McastAutoAdd_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 3),
    _FlWorkWlanIf1McastAutoAdd_Type()
)
flWorkWlanIf1McastAutoAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastAutoAdd.setStatus("current")
_FlWorkWlanIf1McastAdvSnooping_Type = EnabledDisabledStatus
_FlWorkWlanIf1McastAdvSnooping_Object = MibScalar
flWorkWlanIf1McastAdvSnooping = _FlWorkWlanIf1McastAdvSnooping_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 4),
    _FlWorkWlanIf1McastAdvSnooping_Type()
)
flWorkWlanIf1McastAdvSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastAdvSnooping.setStatus("current")
_FlWorkWlanIf1McastTable_Object = MibTable
flWorkWlanIf1McastTable = _FlWorkWlanIf1McastTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 10)
)
if mibBuilder.loadTexts:
    flWorkWlanIf1McastTable.setStatus("current")
_FlWorkWlanIf1McastEntry_Object = MibTableRow
flWorkWlanIf1McastEntry = _FlWorkWlanIf1McastEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 10, 1)
)
flWorkWlanIf1McastEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkWlanIf1McastTableEntryIdx"),
)
if mibBuilder.loadTexts:
    flWorkWlanIf1McastEntry.setStatus("current")


class _FlWorkWlanIf1McastTableEntryIdx_Type(Integer32):
    """Custom type flWorkWlanIf1McastTableEntryIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_FlWorkWlanIf1McastTableEntryIdx_Type.__name__ = "Integer32"
_FlWorkWlanIf1McastTableEntryIdx_Object = MibTableColumn
flWorkWlanIf1McastTableEntryIdx = _FlWorkWlanIf1McastTableEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 10, 1, 1),
    _FlWorkWlanIf1McastTableEntryIdx_Type()
)
flWorkWlanIf1McastTableEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastTableEntryIdx.setStatus("current")
_FlWorkWlanIf1McastTableEntryGroup_Type = MacAddress
_FlWorkWlanIf1McastTableEntryGroup_Object = MibTableColumn
flWorkWlanIf1McastTableEntryGroup = _FlWorkWlanIf1McastTableEntryGroup_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 10, 1, 2),
    _FlWorkWlanIf1McastTableEntryGroup_Type()
)
flWorkWlanIf1McastTableEntryGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastTableEntryGroup.setStatus("current")
_FlWorkWlanIf1McastTableEntryMember_Type = MacAddress
_FlWorkWlanIf1McastTableEntryMember_Object = MibTableColumn
flWorkWlanIf1McastTableEntryMember = _FlWorkWlanIf1McastTableEntryMember_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 10, 1, 3),
    _FlWorkWlanIf1McastTableEntryMember_Type()
)
flWorkWlanIf1McastTableEntryMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastTableEntryMember.setStatus("current")
_FlWorkWlanIf1McastTableEntrySta_Type = MacAddress
_FlWorkWlanIf1McastTableEntrySta_Object = MibTableColumn
flWorkWlanIf1McastTableEntrySta = _FlWorkWlanIf1McastTableEntrySta_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 10, 1, 4),
    _FlWorkWlanIf1McastTableEntrySta_Type()
)
flWorkWlanIf1McastTableEntrySta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastTableEntrySta.setStatus("current")
_FlWorkWlanIf1McastDenyConfig_ObjectIdentity = ObjectIdentity
flWorkWlanIf1McastDenyConfig = _FlWorkWlanIf1McastDenyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 20)
)
_FlWorkWlanIf1McastDenyCreate_Type = IpAddress
_FlWorkWlanIf1McastDenyCreate_Object = MibScalar
flWorkWlanIf1McastDenyCreate = _FlWorkWlanIf1McastDenyCreate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 20, 1),
    _FlWorkWlanIf1McastDenyCreate_Type()
)
flWorkWlanIf1McastDenyCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastDenyCreate.setStatus("current")
_FlWorkWlanIf1McastDenyTable_Object = MibTable
flWorkWlanIf1McastDenyTable = _FlWorkWlanIf1McastDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 20, 2)
)
if mibBuilder.loadTexts:
    flWorkWlanIf1McastDenyTable.setStatus("current")
_FlWorkWlanIf1McastDenyEntry_Object = MibTableRow
flWorkWlanIf1McastDenyEntry = _FlWorkWlanIf1McastDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 20, 2, 1)
)
flWorkWlanIf1McastDenyEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkWlanIf1McastDenyTableEntryIdx"),
)
if mibBuilder.loadTexts:
    flWorkWlanIf1McastDenyEntry.setStatus("current")


class _FlWorkWlanIf1McastDenyTableEntryIdx_Type(Integer32):
    """Custom type flWorkWlanIf1McastDenyTableEntryIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_FlWorkWlanIf1McastDenyTableEntryIdx_Type.__name__ = "Integer32"
_FlWorkWlanIf1McastDenyTableEntryIdx_Object = MibTableColumn
flWorkWlanIf1McastDenyTableEntryIdx = _FlWorkWlanIf1McastDenyTableEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 20, 2, 1, 1),
    _FlWorkWlanIf1McastDenyTableEntryIdx_Type()
)
flWorkWlanIf1McastDenyTableEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastDenyTableEntryIdx.setStatus("current")
_FlWorkWlanIf1McastDenyTableEntryGroup_Type = IpAddress
_FlWorkWlanIf1McastDenyTableEntryGroup_Object = MibTableColumn
flWorkWlanIf1McastDenyTableEntryGroup = _FlWorkWlanIf1McastDenyTableEntryGroup_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 20, 2, 1, 2),
    _FlWorkWlanIf1McastDenyTableEntryGroup_Type()
)
flWorkWlanIf1McastDenyTableEntryGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastDenyTableEntryGroup.setStatus("current")
_FlWorkWlanIf1McastDenyTableEntryStatus_Type = RowStatus
_FlWorkWlanIf1McastDenyTableEntryStatus_Object = MibTableColumn
flWorkWlanIf1McastDenyTableEntryStatus = _FlWorkWlanIf1McastDenyTableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 4, 20, 2, 1, 3),
    _FlWorkWlanIf1McastDenyTableEntryStatus_Type()
)
flWorkWlanIf1McastDenyTableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf1McastDenyTableEntryStatus.setStatus("current")
_FlWorkWlanIf1StationsTable_Object = MibTable
flWorkWlanIf1StationsTable = _FlWorkWlanIf1StationsTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 10)
)
if mibBuilder.loadTexts:
    flWorkWlanIf1StationsTable.setStatus("current")
_FlWorkWlanIf1StationsEntry_Object = MibTableRow
flWorkWlanIf1StationsEntry = _FlWorkWlanIf1StationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 10, 1)
)
flWorkWlanIf1StationsEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkWlanIf1StationEntryIdx"),
)
if mibBuilder.loadTexts:
    flWorkWlanIf1StationsEntry.setStatus("current")


class _FlWorkWlanIf1StationEntryIdx_Type(Integer32):
    """Custom type flWorkWlanIf1StationEntryIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_FlWorkWlanIf1StationEntryIdx_Type.__name__ = "Integer32"
_FlWorkWlanIf1StationEntryIdx_Object = MibTableColumn
flWorkWlanIf1StationEntryIdx = _FlWorkWlanIf1StationEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 10, 1, 1),
    _FlWorkWlanIf1StationEntryIdx_Type()
)
flWorkWlanIf1StationEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkWlanIf1StationEntryIdx.setStatus("current")


class _FlWorkWlanIf1StationEntrySNR_Type(Integer32):
    """Custom type flWorkWlanIf1StationEntrySNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_FlWorkWlanIf1StationEntrySNR_Type.__name__ = "Integer32"
_FlWorkWlanIf1StationEntrySNR_Object = MibTableColumn
flWorkWlanIf1StationEntrySNR = _FlWorkWlanIf1StationEntrySNR_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 10, 1, 2),
    _FlWorkWlanIf1StationEntrySNR_Type()
)
flWorkWlanIf1StationEntrySNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1StationEntrySNR.setStatus("current")


class _FlWorkWlanIf1StationEntryRate_Type(Integer32):
    """Custom type flWorkWlanIf1StationEntryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkWlanIf1StationEntryRate_Type.__name__ = "Integer32"
_FlWorkWlanIf1StationEntryRate_Object = MibTableColumn
flWorkWlanIf1StationEntryRate = _FlWorkWlanIf1StationEntryRate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 10, 1, 3),
    _FlWorkWlanIf1StationEntryRate_Type()
)
flWorkWlanIf1StationEntryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1StationEntryRate.setStatus("current")


class _FlWorkWlanIf1StationEntryPower_Type(Integer32):
    """Custom type flWorkWlanIf1StationEntryPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkWlanIf1StationEntryPower_Type.__name__ = "Integer32"
_FlWorkWlanIf1StationEntryPower_Object = MibTableColumn
flWorkWlanIf1StationEntryPower = _FlWorkWlanIf1StationEntryPower_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 10, 1, 4),
    _FlWorkWlanIf1StationEntryPower_Type()
)
flWorkWlanIf1StationEntryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1StationEntryPower.setStatus("current")
_FlWorkWlanIf1StationEntryAddress_Type = MacAddress
_FlWorkWlanIf1StationEntryAddress_Object = MibTableColumn
flWorkWlanIf1StationEntryAddress = _FlWorkWlanIf1StationEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 10, 1, 5),
    _FlWorkWlanIf1StationEntryAddress_Type()
)
flWorkWlanIf1StationEntryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1StationEntryAddress.setStatus("current")
_FlWorkWlanIf1VisibleAccessPointTable_Object = MibTable
flWorkWlanIf1VisibleAccessPointTable = _FlWorkWlanIf1VisibleAccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20)
)
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointTable.setStatus("current")
_FlWorkWlanIf1VisibleAccessPointEntry_Object = MibTableRow
flWorkWlanIf1VisibleAccessPointEntry = _FlWorkWlanIf1VisibleAccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1)
)
flWorkWlanIf1VisibleAccessPointEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkWlanIf1VisibleAccessPointEntryIdx"),
)
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntry.setStatus("current")


class _FlWorkWlanIf1VisibleAccessPointEntryIdx_Type(Integer32):
    """Custom type flWorkWlanIf1VisibleAccessPointEntryIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_FlWorkWlanIf1VisibleAccessPointEntryIdx_Type.__name__ = "Integer32"
_FlWorkWlanIf1VisibleAccessPointEntryIdx_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntryIdx = _FlWorkWlanIf1VisibleAccessPointEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 1),
    _FlWorkWlanIf1VisibleAccessPointEntryIdx_Type()
)
flWorkWlanIf1VisibleAccessPointEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntryIdx.setStatus("current")


class _FlWorkWlanIf1VisibleAccessPointEntrySNR_Type(Integer32):
    """Custom type flWorkWlanIf1VisibleAccessPointEntrySNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_FlWorkWlanIf1VisibleAccessPointEntrySNR_Type.__name__ = "Integer32"
_FlWorkWlanIf1VisibleAccessPointEntrySNR_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntrySNR = _FlWorkWlanIf1VisibleAccessPointEntrySNR_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 2),
    _FlWorkWlanIf1VisibleAccessPointEntrySNR_Type()
)
flWorkWlanIf1VisibleAccessPointEntrySNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntrySNR.setStatus("current")


class _FlWorkWlanIf1VisibleAccessPointEntryChannel_Type(Integer32):
    """Custom type flWorkWlanIf1VisibleAccessPointEntryChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkWlanIf1VisibleAccessPointEntryChannel_Type.__name__ = "Integer32"
_FlWorkWlanIf1VisibleAccessPointEntryChannel_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntryChannel = _FlWorkWlanIf1VisibleAccessPointEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 3),
    _FlWorkWlanIf1VisibleAccessPointEntryChannel_Type()
)
flWorkWlanIf1VisibleAccessPointEntryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntryChannel.setStatus("current")


class _FlWorkWlanIf1VisibleAccessPointEntryPower_Type(Integer32):
    """Custom type flWorkWlanIf1VisibleAccessPointEntryPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkWlanIf1VisibleAccessPointEntryPower_Type.__name__ = "Integer32"
_FlWorkWlanIf1VisibleAccessPointEntryPower_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntryPower = _FlWorkWlanIf1VisibleAccessPointEntryPower_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 4),
    _FlWorkWlanIf1VisibleAccessPointEntryPower_Type()
)
flWorkWlanIf1VisibleAccessPointEntryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntryPower.setStatus("current")
_FlWorkWlanIf1VisibleAccessPointEntrySSID_Type = OctetString
_FlWorkWlanIf1VisibleAccessPointEntrySSID_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntrySSID = _FlWorkWlanIf1VisibleAccessPointEntrySSID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 5),
    _FlWorkWlanIf1VisibleAccessPointEntrySSID_Type()
)
flWorkWlanIf1VisibleAccessPointEntrySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntrySSID.setStatus("current")
_FlWorkWlanIf1VisibleAccessPointEntrySecurity_Type = OctetString
_FlWorkWlanIf1VisibleAccessPointEntrySecurity_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntrySecurity = _FlWorkWlanIf1VisibleAccessPointEntrySecurity_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 6),
    _FlWorkWlanIf1VisibleAccessPointEntrySecurity_Type()
)
flWorkWlanIf1VisibleAccessPointEntrySecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntrySecurity.setStatus("current")
_FlWorkWlanIf1VisibleAccessPointEntryAddress_Type = MacAddress
_FlWorkWlanIf1VisibleAccessPointEntryAddress_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntryAddress = _FlWorkWlanIf1VisibleAccessPointEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 7),
    _FlWorkWlanIf1VisibleAccessPointEntryAddress_Type()
)
flWorkWlanIf1VisibleAccessPointEntryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntryAddress.setStatus("current")


class _FlWorkWlanIf1VisibleAccessPointEntryConnected_Type(Integer32):
    """Custom type flWorkWlanIf1VisibleAccessPointEntryConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 0),
          ("connected", 1))
    )


_FlWorkWlanIf1VisibleAccessPointEntryConnected_Type.__name__ = "Integer32"
_FlWorkWlanIf1VisibleAccessPointEntryConnected_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntryConnected = _FlWorkWlanIf1VisibleAccessPointEntryConnected_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 8),
    _FlWorkWlanIf1VisibleAccessPointEntryConnected_Type()
)
flWorkWlanIf1VisibleAccessPointEntryConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntryConnected.setStatus("current")


class _FlWorkWlanIf1VisibleAccessPointEntryRSSI_Type(Integer32):
    """Custom type flWorkWlanIf1VisibleAccessPointEntryRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 0),
          ("connected", 1))
    )


_FlWorkWlanIf1VisibleAccessPointEntryRSSI_Type.__name__ = "Integer32"
_FlWorkWlanIf1VisibleAccessPointEntryRSSI_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntryRSSI = _FlWorkWlanIf1VisibleAccessPointEntryRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 9),
    _FlWorkWlanIf1VisibleAccessPointEntryRSSI_Type()
)
flWorkWlanIf1VisibleAccessPointEntryRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntryRSSI.setStatus("current")
_FlWorkWlanIf1VisibleAccessPointEntryNoise_Type = Integer32
_FlWorkWlanIf1VisibleAccessPointEntryNoise_Object = MibTableColumn
flWorkWlanIf1VisibleAccessPointEntryNoise = _FlWorkWlanIf1VisibleAccessPointEntryNoise_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 20, 20, 1, 10),
    _FlWorkWlanIf1VisibleAccessPointEntryNoise_Type()
)
flWorkWlanIf1VisibleAccessPointEntryNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkWlanIf1VisibleAccessPointEntryNoise.setStatus("current")
_FlWorkWlanIf2_ObjectIdentity = ObjectIdentity
flWorkWlanIf2 = _FlWorkWlanIf2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30)
)
_FlWorkWlanIf2Parameter_ObjectIdentity = ObjectIdentity
flWorkWlanIf2Parameter = _FlWorkWlanIf2Parameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1)
)
_FlWorkWlanIf2ParamState_Type = EnabledDisabledStatus
_FlWorkWlanIf2ParamState_Object = MibScalar
flWorkWlanIf2ParamState = _FlWorkWlanIf2ParamState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 1),
    _FlWorkWlanIf2ParamState_Type()
)
flWorkWlanIf2ParamState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2ParamState.setStatus("current")
_FlWorkWlanIf2ParamOpMode_Type = OpModeType
_FlWorkWlanIf2ParamOpMode_Object = MibScalar
flWorkWlanIf2ParamOpMode = _FlWorkWlanIf2ParamOpMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 2),
    _FlWorkWlanIf2ParamOpMode_Type()
)
flWorkWlanIf2ParamOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2ParamOpMode.setStatus("current")


class _FlWorkWlanIf2ParamSSID_Type(OctetString):
    """Custom type flWorkWlanIf2ParamSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FlWorkWlanIf2ParamSSID_Type.__name__ = "OctetString"
_FlWorkWlanIf2ParamSSID_Object = MibScalar
flWorkWlanIf2ParamSSID = _FlWorkWlanIf2ParamSSID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 3),
    _FlWorkWlanIf2ParamSSID_Type()
)
flWorkWlanIf2ParamSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2ParamSSID.setStatus("current")


class _FlWorkWlanIf2ParamMode_Type(Integer32):
    """Custom type flWorkWlanIf2ParamMode based on Integer32"""
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
        *(("abg", 0),
          ("a", 1),
          ("b", 2),
          ("bg", 3),
          ("an", 4),
          ("gn", 5))
    )


_FlWorkWlanIf2ParamMode_Type.__name__ = "Integer32"
_FlWorkWlanIf2ParamMode_Object = MibScalar
flWorkWlanIf2ParamMode = _FlWorkWlanIf2ParamMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 4),
    _FlWorkWlanIf2ParamMode_Type()
)
flWorkWlanIf2ParamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2ParamMode.setStatus("current")


class _FlWorkWlanIf2ParamChannel_Type(Integer32):
    """Custom type flWorkWlanIf2ParamChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkWlanIf2ParamChannel_Type.__name__ = "Integer32"
_FlWorkWlanIf2ParamChannel_Object = MibScalar
flWorkWlanIf2ParamChannel = _FlWorkWlanIf2ParamChannel_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 5),
    _FlWorkWlanIf2ParamChannel_Type()
)
flWorkWlanIf2ParamChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2ParamChannel.setStatus("current")
_FlWorkWlanIf2ParamOutdoor_Type = EnabledDisabledStatus
_FlWorkWlanIf2ParamOutdoor_Object = MibScalar
flWorkWlanIf2ParamOutdoor = _FlWorkWlanIf2ParamOutdoor_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 6),
    _FlWorkWlanIf2ParamOutdoor_Type()
)
flWorkWlanIf2ParamOutdoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2ParamOutdoor.setStatus("current")


class _FlWorkWlanIf2AntennaOutput_Type(Integer32):
    """Custom type flWorkWlanIf2AntennaOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FlWorkWlanIf2AntennaOutput_Type.__name__ = "Integer32"
_FlWorkWlanIf2AntennaOutput_Object = MibScalar
flWorkWlanIf2AntennaOutput = _FlWorkWlanIf2AntennaOutput_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 7),
    _FlWorkWlanIf2AntennaOutput_Type()
)
flWorkWlanIf2AntennaOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2AntennaOutput.setStatus("current")


class _FlWorkWlanIf2OutputPower_Type(Integer32):
    """Custom type flWorkWlanIf2OutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 23),
    )


_FlWorkWlanIf2OutputPower_Type.__name__ = "Integer32"
_FlWorkWlanIf2OutputPower_Object = MibScalar
flWorkWlanIf2OutputPower = _FlWorkWlanIf2OutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 8),
    _FlWorkWlanIf2OutputPower_Type()
)
flWorkWlanIf2OutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2OutputPower.setStatus("current")


class _FlWorkWlanIf2STBC_Type(Integer32):
    """Custom type flWorkWlanIf2STBC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkWlanIf2STBC_Type.__name__ = "Integer32"
_FlWorkWlanIf2STBC_Object = MibScalar
flWorkWlanIf2STBC = _FlWorkWlanIf2STBC_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 9),
    _FlWorkWlanIf2STBC_Type()
)
flWorkWlanIf2STBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2STBC.setStatus("current")


class _FlWorkWlanIf2Fragmentation_Type(Integer32):
    """Custom type flWorkWlanIf2Fragmentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2600),
    )


_FlWorkWlanIf2Fragmentation_Type.__name__ = "Integer32"
_FlWorkWlanIf2Fragmentation_Object = MibScalar
flWorkWlanIf2Fragmentation = _FlWorkWlanIf2Fragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 10),
    _FlWorkWlanIf2Fragmentation_Type()
)
flWorkWlanIf2Fragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2Fragmentation.setStatus("current")


class _FlWorkWlanIf2RtsCts_Type(Integer32):
    """Custom type flWorkWlanIf2RtsCts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2600),
    )


_FlWorkWlanIf2RtsCts_Type.__name__ = "Integer32"
_FlWorkWlanIf2RtsCts_Object = MibScalar
flWorkWlanIf2RtsCts = _FlWorkWlanIf2RtsCts_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 11),
    _FlWorkWlanIf2RtsCts_Type()
)
flWorkWlanIf2RtsCts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2RtsCts.setStatus("current")


class _FlWorkWlanIf2LongDistance_Type(Integer32):
    """Custom type flWorkWlanIf2LongDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 50000),
    )


_FlWorkWlanIf2LongDistance_Type.__name__ = "Integer32"
_FlWorkWlanIf2LongDistance_Object = MibScalar
flWorkWlanIf2LongDistance = _FlWorkWlanIf2LongDistance_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 12),
    _FlWorkWlanIf2LongDistance_Type()
)
flWorkWlanIf2LongDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2LongDistance.setStatus("current")
_FlWorkWlanIf2ScbMacAddress_Type = MacAddress
_FlWorkWlanIf2ScbMacAddress_Object = MibScalar
flWorkWlanIf2ScbMacAddress = _FlWorkWlanIf2ScbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 13),
    _FlWorkWlanIf2ScbMacAddress_Type()
)
flWorkWlanIf2ScbMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2ScbMacAddress.setStatus("current")


class _FlWorkWlanIf2ScbManMacMode_Type(Integer32):
    """Custom type flWorkWlanIf2ScbManMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FlWorkWlanIf2ScbManMacMode_Type.__name__ = "Integer32"
_FlWorkWlanIf2ScbManMacMode_Object = MibScalar
flWorkWlanIf2ScbManMacMode = _FlWorkWlanIf2ScbManMacMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 14),
    _FlWorkWlanIf2ScbManMacMode_Type()
)
flWorkWlanIf2ScbManMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2ScbManMacMode.setStatus("current")


class _FlWorkWlanIf2IAPP_Type(Integer32):
    """Custom type flWorkWlanIf2IAPP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FlWorkWlanIf2IAPP_Type.__name__ = "Integer32"
_FlWorkWlanIf2IAPP_Object = MibScalar
flWorkWlanIf2IAPP = _FlWorkWlanIf2IAPP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 15),
    _FlWorkWlanIf2IAPP_Type()
)
flWorkWlanIf2IAPP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2IAPP.setStatus("current")
_FlWorkWlanIf2MachineAdmin_ObjectIdentity = ObjectIdentity
flWorkWlanIf2MachineAdmin = _FlWorkWlanIf2MachineAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 16)
)


class _FlWorkWlanIf2MachineAdminSSID_Type(OctetString):
    """Custom type flWorkWlanIf2MachineAdminSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FlWorkWlanIf2MachineAdminSSID_Type.__name__ = "OctetString"
_FlWorkWlanIf2MachineAdminSSID_Object = MibScalar
flWorkWlanIf2MachineAdminSSID = _FlWorkWlanIf2MachineAdminSSID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 16, 1),
    _FlWorkWlanIf2MachineAdminSSID_Type()
)
flWorkWlanIf2MachineAdminSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2MachineAdminSSID.setStatus("current")


class _FlWorkWlanIf2MachineAdminPsk_Type(OctetString):
    """Custom type flWorkWlanIf2MachineAdminPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_FlWorkWlanIf2MachineAdminPsk_Type.__name__ = "OctetString"
_FlWorkWlanIf2MachineAdminPsk_Object = MibScalar
flWorkWlanIf2MachineAdminPsk = _FlWorkWlanIf2MachineAdminPsk_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 16, 2),
    _FlWorkWlanIf2MachineAdminPsk_Type()
)
flWorkWlanIf2MachineAdminPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2MachineAdminPsk.setStatus("current")
_FlWorkWlanIf2MachineAdminIp_Type = IpAddress
_FlWorkWlanIf2MachineAdminIp_Object = MibScalar
flWorkWlanIf2MachineAdminIp = _FlWorkWlanIf2MachineAdminIp_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 1, 16, 3),
    _FlWorkWlanIf2MachineAdminIp_Type()
)
flWorkWlanIf2MachineAdminIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2MachineAdminIp.setStatus("current")
_FlWorkWlanIf2Security_ObjectIdentity = ObjectIdentity
flWorkWlanIf2Security = _FlWorkWlanIf2Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 2)
)


class _FlWorkWlanIf2SecMode_Type(Integer32):
    """Custom type flWorkWlanIf2SecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wpa-psk", 1),
          ("wpa2-psk", 4),
          ("wpa2-eap", 5))
    )


_FlWorkWlanIf2SecMode_Type.__name__ = "Integer32"
_FlWorkWlanIf2SecMode_Object = MibScalar
flWorkWlanIf2SecMode = _FlWorkWlanIf2SecMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 2, 1),
    _FlWorkWlanIf2SecMode_Type()
)
flWorkWlanIf2SecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2SecMode.setStatus("current")


class _FlWorkWlanIf2SecWpaEncryptionAlgorithm_Type(Integer32):
    """Custom type flWorkWlanIf2SecWpaEncryptionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("both", 3))
    )


_FlWorkWlanIf2SecWpaEncryptionAlgorithm_Type.__name__ = "Integer32"
_FlWorkWlanIf2SecWpaEncryptionAlgorithm_Object = MibScalar
flWorkWlanIf2SecWpaEncryptionAlgorithm = _FlWorkWlanIf2SecWpaEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 2, 2),
    _FlWorkWlanIf2SecWpaEncryptionAlgorithm_Type()
)
flWorkWlanIf2SecWpaEncryptionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2SecWpaEncryptionAlgorithm.setStatus("current")


class _FlWorkWlanIf2SecWpaPsk_Type(OctetString):
    """Custom type flWorkWlanIf2SecWpaPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_FlWorkWlanIf2SecWpaPsk_Type.__name__ = "OctetString"
_FlWorkWlanIf2SecWpaPsk_Object = MibScalar
flWorkWlanIf2SecWpaPsk = _FlWorkWlanIf2SecWpaPsk_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 2, 3),
    _FlWorkWlanIf2SecWpaPsk_Type()
)
flWorkWlanIf2SecWpaPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2SecWpaPsk.setStatus("current")


class _FlWorkWlanIf2SecWepAuthType_Type(Integer32):
    """Custom type flWorkWlanIf2SecWepAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open-system", 1),
          ("shared-key", 2),
          ("automatic", 3))
    )


_FlWorkWlanIf2SecWepAuthType_Type.__name__ = "Integer32"
_FlWorkWlanIf2SecWepAuthType_Object = MibScalar
flWorkWlanIf2SecWepAuthType = _FlWorkWlanIf2SecWepAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 2, 4),
    _FlWorkWlanIf2SecWepAuthType_Type()
)
flWorkWlanIf2SecWepAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2SecWepAuthType.setStatus("current")


class _FlWorkWlanIf2SecWepKeyEncoding_Type(Integer32):
    """Custom type flWorkWlanIf2SecWepKeyEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hex", 0),
          ("ascii", 1))
    )


_FlWorkWlanIf2SecWepKeyEncoding_Type.__name__ = "Integer32"
_FlWorkWlanIf2SecWepKeyEncoding_Object = MibScalar
flWorkWlanIf2SecWepKeyEncoding = _FlWorkWlanIf2SecWepKeyEncoding_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 2, 5),
    _FlWorkWlanIf2SecWepKeyEncoding_Type()
)
flWorkWlanIf2SecWepKeyEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2SecWepKeyEncoding.setStatus("current")


class _FlWorkWlanIf2SecWepKey_Type(OctetString):
    """Custom type flWorkWlanIf2SecWepKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 26),
    )


_FlWorkWlanIf2SecWepKey_Type.__name__ = "OctetString"
_FlWorkWlanIf2SecWepKey_Object = MibScalar
flWorkWlanIf2SecWepKey = _FlWorkWlanIf2SecWepKey_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 30, 2, 6),
    _FlWorkWlanIf2SecWepKey_Type()
)
flWorkWlanIf2SecWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanIf2SecWepKey.setStatus("current")
_FlWorkWlanMacFilter_ObjectIdentity = ObjectIdentity
flWorkWlanMacFilter = _FlWorkWlanMacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40)
)
_FlWorkWlanMacFilterTable_Object = MibTable
flWorkWlanMacFilterTable = _FlWorkWlanMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40, 1)
)
if mibBuilder.loadTexts:
    flWorkWlanMacFilterTable.setStatus("current")
_FlWorkWlanMacFilterEntry_Object = MibTableRow
flWorkWlanMacFilterEntry = _FlWorkWlanMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40, 1, 1)
)
flWorkWlanMacFilterEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkWlanMacEntryIdx"),
)
if mibBuilder.loadTexts:
    flWorkWlanMacFilterEntry.setStatus("current")


class _FlWorkWlanMacEntryIdx_Type(Integer32):
    """Custom type flWorkWlanMacEntryIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 499),
    )


_FlWorkWlanMacEntryIdx_Type.__name__ = "Integer32"
_FlWorkWlanMacEntryIdx_Object = MibTableColumn
flWorkWlanMacEntryIdx = _FlWorkWlanMacEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40, 1, 1, 1),
    _FlWorkWlanMacEntryIdx_Type()
)
flWorkWlanMacEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkWlanMacEntryIdx.setStatus("current")


class _FlWorkWlanMacEntryInterfaceName_Type(Integer32):
    """Custom type flWorkWlanMacEntryInterfaceName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("wlan-1", 1),
          ("wlan-2", 2))
    )


_FlWorkWlanMacEntryInterfaceName_Type.__name__ = "Integer32"
_FlWorkWlanMacEntryInterfaceName_Object = MibTableColumn
flWorkWlanMacEntryInterfaceName = _FlWorkWlanMacEntryInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40, 1, 1, 2),
    _FlWorkWlanMacEntryInterfaceName_Type()
)
flWorkWlanMacEntryInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanMacEntryInterfaceName.setStatus("current")


class _FlWorkWlanMacEntryAction_Type(Integer32):
    """Custom type flWorkWlanMacEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1),
          ("disabled", 2))
    )


_FlWorkWlanMacEntryAction_Type.__name__ = "Integer32"
_FlWorkWlanMacEntryAction_Object = MibTableColumn
flWorkWlanMacEntryAction = _FlWorkWlanMacEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40, 1, 1, 3),
    _FlWorkWlanMacEntryAction_Type()
)
flWorkWlanMacEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanMacEntryAction.setStatus("current")
_FlWorkWlanMacEntryAddress_Type = MacAddress
_FlWorkWlanMacEntryAddress_Object = MibTableColumn
flWorkWlanMacEntryAddress = _FlWorkWlanMacEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40, 1, 1, 4),
    _FlWorkWlanMacEntryAddress_Type()
)
flWorkWlanMacEntryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanMacEntryAddress.setStatus("current")


class _FlWorkWlanMacPolicyIf1_Type(Integer32):
    """Custom type flWorkWlanMacPolicyIf1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("allow", 1))
    )


_FlWorkWlanMacPolicyIf1_Type.__name__ = "Integer32"
_FlWorkWlanMacPolicyIf1_Object = MibScalar
flWorkWlanMacPolicyIf1 = _FlWorkWlanMacPolicyIf1_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40, 2),
    _FlWorkWlanMacPolicyIf1_Type()
)
flWorkWlanMacPolicyIf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanMacPolicyIf1.setStatus("current")


class _FlWorkWlanMacPolicyIf2_Type(Integer32):
    """Custom type flWorkWlanMacPolicyIf2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("allow", 1))
    )


_FlWorkWlanMacPolicyIf2_Type.__name__ = "Integer32"
_FlWorkWlanMacPolicyIf2_Object = MibScalar
flWorkWlanMacPolicyIf2 = _FlWorkWlanMacPolicyIf2_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40, 3),
    _FlWorkWlanMacPolicyIf2_Type()
)
flWorkWlanMacPolicyIf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanMacPolicyIf2.setStatus("current")
_FlWorkWlanMacFilterSyslog_Type = EnabledDisabledStatus
_FlWorkWlanMacFilterSyslog_Object = MibScalar
flWorkWlanMacFilterSyslog = _FlWorkWlanMacFilterSyslog_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 22, 40, 4),
    _FlWorkWlanMacFilterSyslog_Type()
)
flWorkWlanMacFilterSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkWlanMacFilterSyslog.setStatus("current")
_FlWorkRouting_ObjectIdentity = ObjectIdentity
flWorkRouting = _FlWorkRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23)
)
_FlWorkRoutingIp_ObjectIdentity = ObjectIdentity
flWorkRoutingIp = _FlWorkRoutingIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1)
)


class _FlWorkRoutingIpRoutingMode_Type(Integer32):
    """Custom type flWorkRoutingIpRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpRoutingMode_Type.__name__ = "Integer32"
_FlWorkRoutingIpRoutingMode_Object = MibScalar
flWorkRoutingIpRoutingMode = _FlWorkRoutingIpRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 1),
    _FlWorkRoutingIpRoutingMode_Type()
)
flWorkRoutingIpRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpRoutingMode.setStatus("current")
_FlWorkRoutingIpInterfaceTable_Object = MibTable
flWorkRoutingIpInterfaceTable = _FlWorkRoutingIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3)
)
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceTable.setStatus("current")
_FlWorkRoutingIpInterfaceEntry_Object = MibTableRow
flWorkRoutingIpInterfaceEntry = _FlWorkRoutingIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1)
)
flWorkRoutingIpInterfaceEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingIpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceEntry.setStatus("current")


class _FlWorkRoutingIpInterfaceIfIndex_Type(Integer32):
    """Custom type flWorkRoutingIpInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkRoutingIpInterfaceIfIndex_Type.__name__ = "Integer32"
_FlWorkRoutingIpInterfaceIfIndex_Object = MibTableColumn
flWorkRoutingIpInterfaceIfIndex = _FlWorkRoutingIpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 1),
    _FlWorkRoutingIpInterfaceIfIndex_Type()
)
flWorkRoutingIpInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceIfIndex.setStatus("current")
_FlWorkRoutingIpInterfaceIpAddress_Type = IpAddress
_FlWorkRoutingIpInterfaceIpAddress_Object = MibTableColumn
flWorkRoutingIpInterfaceIpAddress = _FlWorkRoutingIpInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 2),
    _FlWorkRoutingIpInterfaceIpAddress_Type()
)
flWorkRoutingIpInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceIpAddress.setStatus("current")
_FlWorkRoutingIpInterfaceNetMask_Type = IpAddress
_FlWorkRoutingIpInterfaceNetMask_Object = MibTableColumn
flWorkRoutingIpInterfaceNetMask = _FlWorkRoutingIpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 3),
    _FlWorkRoutingIpInterfaceNetMask_Type()
)
flWorkRoutingIpInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceNetMask.setStatus("current")


class _FlWorkRoutingIpInterfaceClearIp_Type(Integer32):
    """Custom type flWorkRoutingIpInterfaceClearIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpInterfaceClearIp_Type.__name__ = "Integer32"
_FlWorkRoutingIpInterfaceClearIp_Object = MibTableColumn
flWorkRoutingIpInterfaceClearIp = _FlWorkRoutingIpInterfaceClearIp_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 4),
    _FlWorkRoutingIpInterfaceClearIp_Type()
)
flWorkRoutingIpInterfaceClearIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceClearIp.setStatus("current")


class _FlWorkRoutingIpInterfaceRoutingMode_Type(Integer32):
    """Custom type flWorkRoutingIpInterfaceRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpInterfaceRoutingMode_Type.__name__ = "Integer32"
_FlWorkRoutingIpInterfaceRoutingMode_Object = MibTableColumn
flWorkRoutingIpInterfaceRoutingMode = _FlWorkRoutingIpInterfaceRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 5),
    _FlWorkRoutingIpInterfaceRoutingMode_Type()
)
flWorkRoutingIpInterfaceRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceRoutingMode.setStatus("current")


class _FlWorkRoutingIpInterfaceProxyARPMode_Type(Integer32):
    """Custom type flWorkRoutingIpInterfaceProxyARPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpInterfaceProxyARPMode_Type.__name__ = "Integer32"
_FlWorkRoutingIpInterfaceProxyARPMode_Object = MibTableColumn
flWorkRoutingIpInterfaceProxyARPMode = _FlWorkRoutingIpInterfaceProxyARPMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 6),
    _FlWorkRoutingIpInterfaceProxyARPMode_Type()
)
flWorkRoutingIpInterfaceProxyARPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceProxyARPMode.setStatus("current")


class _FlWorkRoutingIpInterfaceMtuValue_Type(Unsigned32):
    """Custom type flWorkRoutingIpInterfaceMtuValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 1500),
    )


_FlWorkRoutingIpInterfaceMtuValue_Type.__name__ = "Unsigned32"
_FlWorkRoutingIpInterfaceMtuValue_Object = MibTableColumn
flWorkRoutingIpInterfaceMtuValue = _FlWorkRoutingIpInterfaceMtuValue_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 7),
    _FlWorkRoutingIpInterfaceMtuValue_Type()
)
flWorkRoutingIpInterfaceMtuValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceMtuValue.setStatus("current")


class _FlWorkRoutingIpInterfaceBandwidth_Type(Unsigned32):
    """Custom type flWorkRoutingIpInterfaceBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000000),
    )


_FlWorkRoutingIpInterfaceBandwidth_Type.__name__ = "Unsigned32"
_FlWorkRoutingIpInterfaceBandwidth_Object = MibTableColumn
flWorkRoutingIpInterfaceBandwidth = _FlWorkRoutingIpInterfaceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 8),
    _FlWorkRoutingIpInterfaceBandwidth_Type()
)
flWorkRoutingIpInterfaceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceBandwidth.setStatus("current")
_FlWorkRoutingIpInterfaceUnnumberedIfIndex_Type = InterfaceIndexOrZero
_FlWorkRoutingIpInterfaceUnnumberedIfIndex_Object = MibTableColumn
flWorkRoutingIpInterfaceUnnumberedIfIndex = _FlWorkRoutingIpInterfaceUnnumberedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 9),
    _FlWorkRoutingIpInterfaceUnnumberedIfIndex_Type()
)
flWorkRoutingIpInterfaceUnnumberedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceUnnumberedIfIndex.setStatus("current")


class _FlWorkRoutingIpInterfaceIcmpUnreachables_Type(Integer32):
    """Custom type flWorkRoutingIpInterfaceIcmpUnreachables based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpInterfaceIcmpUnreachables_Type.__name__ = "Integer32"
_FlWorkRoutingIpInterfaceIcmpUnreachables_Object = MibTableColumn
flWorkRoutingIpInterfaceIcmpUnreachables = _FlWorkRoutingIpInterfaceIcmpUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 10),
    _FlWorkRoutingIpInterfaceIcmpUnreachables_Type()
)
flWorkRoutingIpInterfaceIcmpUnreachables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceIcmpUnreachables.setStatus("current")


class _FlWorkRoutingIpInterfaceIcmpRedirects_Type(Integer32):
    """Custom type flWorkRoutingIpInterfaceIcmpRedirects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpInterfaceIcmpRedirects_Type.__name__ = "Integer32"
_FlWorkRoutingIpInterfaceIcmpRedirects_Object = MibTableColumn
flWorkRoutingIpInterfaceIcmpRedirects = _FlWorkRoutingIpInterfaceIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 11),
    _FlWorkRoutingIpInterfaceIcmpRedirects_Type()
)
flWorkRoutingIpInterfaceIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceIcmpRedirects.setStatus("current")


class _FlWorkRoutingIpInterfaceManagementAccess_Type(Integer32):
    """Custom type flWorkRoutingIpInterfaceManagementAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpInterfaceManagementAccess_Type.__name__ = "Integer32"
_FlWorkRoutingIpInterfaceManagementAccess_Object = MibTableColumn
flWorkRoutingIpInterfaceManagementAccess = _FlWorkRoutingIpInterfaceManagementAccess_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 12),
    _FlWorkRoutingIpInterfaceManagementAccess_Type()
)
flWorkRoutingIpInterfaceManagementAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceManagementAccess.setStatus("current")


class _FlWorkRoutingIpInterfaceAssignMode_Type(Integer32):
    """Custom type flWorkRoutingIpInterfaceAssignMode based on Integer32"""
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
        *(("static", 1),
          ("bootp", 2),
          ("dhcp", 3),
          ("dcp", 4))
    )


_FlWorkRoutingIpInterfaceAssignMode_Type.__name__ = "Integer32"
_FlWorkRoutingIpInterfaceAssignMode_Object = MibTableColumn
flWorkRoutingIpInterfaceAssignMode = _FlWorkRoutingIpInterfaceAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 13),
    _FlWorkRoutingIpInterfaceAssignMode_Type()
)
flWorkRoutingIpInterfaceAssignMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceAssignMode.setStatus("current")


class _FlWorkRoutingIpInterfaceMapIdx2IfTable_Type(Integer32):
    """Custom type flWorkRoutingIpInterfaceMapIdx2IfTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkRoutingIpInterfaceMapIdx2IfTable_Type.__name__ = "Integer32"
_FlWorkRoutingIpInterfaceMapIdx2IfTable_Object = MibTableColumn
flWorkRoutingIpInterfaceMapIdx2IfTable = _FlWorkRoutingIpInterfaceMapIdx2IfTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 3, 1, 14),
    _FlWorkRoutingIpInterfaceMapIdx2IfTable_Type()
)
flWorkRoutingIpInterfaceMapIdx2IfTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingIpInterfaceMapIdx2IfTable.setStatus("current")
_FlWorkRoutingIpRouterDiscoveryTable_Object = MibTable
flWorkRoutingIpRouterDiscoveryTable = _FlWorkRoutingIpRouterDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 4)
)
if mibBuilder.loadTexts:
    flWorkRoutingIpRouterDiscoveryTable.setStatus("current")
_FlWorkRoutingIpRouterDiscoveryEntry_Object = MibTableRow
flWorkRoutingIpRouterDiscoveryEntry = _FlWorkRoutingIpRouterDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 4, 1)
)
flWorkRoutingIpRouterDiscoveryEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingIpRouterDiscoveryIfIndex"),
)
if mibBuilder.loadTexts:
    flWorkRoutingIpRouterDiscoveryEntry.setStatus("current")


class _FlWorkRoutingIpRouterDiscoveryIfIndex_Type(Integer32):
    """Custom type flWorkRoutingIpRouterDiscoveryIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkRoutingIpRouterDiscoveryIfIndex_Type.__name__ = "Integer32"
_FlWorkRoutingIpRouterDiscoveryIfIndex_Object = MibTableColumn
flWorkRoutingIpRouterDiscoveryIfIndex = _FlWorkRoutingIpRouterDiscoveryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 4, 1, 1),
    _FlWorkRoutingIpRouterDiscoveryIfIndex_Type()
)
flWorkRoutingIpRouterDiscoveryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingIpRouterDiscoveryIfIndex.setStatus("current")


class _FlWorkRoutingIpRouterDiscoveryAdvertiseMode_Type(Integer32):
    """Custom type flWorkRoutingIpRouterDiscoveryAdvertiseMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpRouterDiscoveryAdvertiseMode_Type.__name__ = "Integer32"
_FlWorkRoutingIpRouterDiscoveryAdvertiseMode_Object = MibTableColumn
flWorkRoutingIpRouterDiscoveryAdvertiseMode = _FlWorkRoutingIpRouterDiscoveryAdvertiseMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 4, 1, 2),
    _FlWorkRoutingIpRouterDiscoveryAdvertiseMode_Type()
)
flWorkRoutingIpRouterDiscoveryAdvertiseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpRouterDiscoveryAdvertiseMode.setStatus("current")


class _FlWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):
    """Custom type flWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_FlWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__ = "Integer32"
_FlWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval_Object = MibTableColumn
flWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval = _FlWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 4, 1, 3),
    _FlWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval_Type()
)
flWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval.setStatus("current")


class _FlWorkRoutingIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):
    """Custom type flWorkRoutingIpRouterDiscoveryMinAdvertisementInterval based on Integer32"""
    defaultValue = 450

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_FlWorkRoutingIpRouterDiscoveryMinAdvertisementInterval_Type.__name__ = "Integer32"
_FlWorkRoutingIpRouterDiscoveryMinAdvertisementInterval_Object = MibTableColumn
flWorkRoutingIpRouterDiscoveryMinAdvertisementInterval = _FlWorkRoutingIpRouterDiscoveryMinAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 4, 1, 4),
    _FlWorkRoutingIpRouterDiscoveryMinAdvertisementInterval_Type()
)
flWorkRoutingIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpRouterDiscoveryMinAdvertisementInterval.setStatus("current")


class _FlWorkRoutingIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):
    """Custom type flWorkRoutingIpRouterDiscoveryAdvertisementLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_FlWorkRoutingIpRouterDiscoveryAdvertisementLifetime_Type.__name__ = "Integer32"
_FlWorkRoutingIpRouterDiscoveryAdvertisementLifetime_Object = MibTableColumn
flWorkRoutingIpRouterDiscoveryAdvertisementLifetime = _FlWorkRoutingIpRouterDiscoveryAdvertisementLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 4, 1, 5),
    _FlWorkRoutingIpRouterDiscoveryAdvertisementLifetime_Type()
)
flWorkRoutingIpRouterDiscoveryAdvertisementLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpRouterDiscoveryAdvertisementLifetime.setStatus("current")


class _FlWorkRoutingIpRouterDiscoveryPreferenceLevel_Type(Integer32):
    """Custom type flWorkRoutingIpRouterDiscoveryPreferenceLevel based on Integer32"""
    defaultValue = 0


_FlWorkRoutingIpRouterDiscoveryPreferenceLevel_Type.__name__ = "Integer32"
_FlWorkRoutingIpRouterDiscoveryPreferenceLevel_Object = MibTableColumn
flWorkRoutingIpRouterDiscoveryPreferenceLevel = _FlWorkRoutingIpRouterDiscoveryPreferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 4, 1, 6),
    _FlWorkRoutingIpRouterDiscoveryPreferenceLevel_Type()
)
flWorkRoutingIpRouterDiscoveryPreferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpRouterDiscoveryPreferenceLevel.setStatus("current")


class _FlWorkRoutingIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):
    """Custom type flWorkRoutingIpRouterDiscoveryAdvertisementAddress based on IpAddress"""
    defaultHexValue = "E0000001"


_FlWorkRoutingIpRouterDiscoveryAdvertisementAddress_Type.__name__ = "IpAddress"
_FlWorkRoutingIpRouterDiscoveryAdvertisementAddress_Object = MibTableColumn
flWorkRoutingIpRouterDiscoveryAdvertisementAddress = _FlWorkRoutingIpRouterDiscoveryAdvertisementAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 4, 1, 7),
    _FlWorkRoutingIpRouterDiscoveryAdvertisementAddress_Type()
)
flWorkRoutingIpRouterDiscoveryAdvertisementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpRouterDiscoveryAdvertisementAddress.setStatus("current")
_FlWorkRoutingIpVlanTable_Object = MibTable
flWorkRoutingIpVlanTable = _FlWorkRoutingIpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 5)
)
if mibBuilder.loadTexts:
    flWorkRoutingIpVlanTable.setStatus("current")
_FlWorkRoutingIpVlanEntry_Object = MibTableRow
flWorkRoutingIpVlanEntry = _FlWorkRoutingIpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 5, 1)
)
flWorkRoutingIpVlanEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingIpVlanId"),
)
if mibBuilder.loadTexts:
    flWorkRoutingIpVlanEntry.setStatus("current")


class _FlWorkRoutingIpVlanId_Type(Integer32):
    """Custom type flWorkRoutingIpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FlWorkRoutingIpVlanId_Type.__name__ = "Integer32"
_FlWorkRoutingIpVlanId_Object = MibTableColumn
flWorkRoutingIpVlanId = _FlWorkRoutingIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 5, 1, 1),
    _FlWorkRoutingIpVlanId_Type()
)
flWorkRoutingIpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingIpVlanId.setStatus("current")


class _FlWorkRoutingIpVlanIfIndex_Type(Integer32):
    """Custom type flWorkRoutingIpVlanIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkRoutingIpVlanIfIndex_Type.__name__ = "Integer32"
_FlWorkRoutingIpVlanIfIndex_Object = MibTableColumn
flWorkRoutingIpVlanIfIndex = _FlWorkRoutingIpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 5, 1, 2),
    _FlWorkRoutingIpVlanIfIndex_Type()
)
flWorkRoutingIpVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingIpVlanIfIndex.setStatus("current")
_FlWorkRoutingIpVlanRoutingStatus_Type = RowStatus
_FlWorkRoutingIpVlanRoutingStatus_Object = MibTableColumn
flWorkRoutingIpVlanRoutingStatus = _FlWorkRoutingIpVlanRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 5, 1, 3),
    _FlWorkRoutingIpVlanRoutingStatus_Type()
)
flWorkRoutingIpVlanRoutingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingIpVlanRoutingStatus.setStatus("current")
_FlWorkRoutingSecondaryAddressTable_Object = MibTable
flWorkRoutingSecondaryAddressTable = _FlWorkRoutingSecondaryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 6)
)
if mibBuilder.loadTexts:
    flWorkRoutingSecondaryAddressTable.setStatus("current")
_FlWorkRoutingSecondaryAddressEntry_Object = MibTableRow
flWorkRoutingSecondaryAddressEntry = _FlWorkRoutingSecondaryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 6, 1)
)
flWorkRoutingSecondaryAddressEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingIpInterfaceIfIndex"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingSecondaryIpAddress"),
)
if mibBuilder.loadTexts:
    flWorkRoutingSecondaryAddressEntry.setStatus("current")
_FlWorkRoutingSecondaryIpAddress_Type = IpAddress
_FlWorkRoutingSecondaryIpAddress_Object = MibTableColumn
flWorkRoutingSecondaryIpAddress = _FlWorkRoutingSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 6, 1, 1),
    _FlWorkRoutingSecondaryIpAddress_Type()
)
flWorkRoutingSecondaryIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkRoutingSecondaryIpAddress.setStatus("current")
_FlWorkRoutingSecondaryNetMask_Type = IpAddress
_FlWorkRoutingSecondaryNetMask_Object = MibTableColumn
flWorkRoutingSecondaryNetMask = _FlWorkRoutingSecondaryNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 6, 1, 2),
    _FlWorkRoutingSecondaryNetMask_Type()
)
flWorkRoutingSecondaryNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingSecondaryNetMask.setStatus("current")
_FlWorkRoutingSecondaryStatus_Type = RowStatus
_FlWorkRoutingSecondaryStatus_Object = MibTableColumn
flWorkRoutingSecondaryStatus = _FlWorkRoutingSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 6, 1, 3),
    _FlWorkRoutingSecondaryStatus_Type()
)
flWorkRoutingSecondaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingSecondaryStatus.setStatus("current")
_FlWorkRoutingHelperAddressTable_Object = MibTable
flWorkRoutingHelperAddressTable = _FlWorkRoutingHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 7)
)
if mibBuilder.loadTexts:
    flWorkRoutingHelperAddressTable.setStatus("current")
_FlWorkRoutingHelperAddressEntry_Object = MibTableRow
flWorkRoutingHelperAddressEntry = _FlWorkRoutingHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 7, 1)
)
flWorkRoutingHelperAddressEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingIpInterfaceIfIndex"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingHelperIpAddress"),
)
if mibBuilder.loadTexts:
    flWorkRoutingHelperAddressEntry.setStatus("current")
_FlWorkRoutingHelperIpAddress_Type = IpAddress
_FlWorkRoutingHelperIpAddress_Object = MibTableColumn
flWorkRoutingHelperIpAddress = _FlWorkRoutingHelperIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 7, 1, 1),
    _FlWorkRoutingHelperIpAddress_Type()
)
flWorkRoutingHelperIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkRoutingHelperIpAddress.setStatus("current")
_FlWorkRoutingHelperStatus_Type = RowStatus
_FlWorkRoutingHelperStatus_Object = MibTableColumn
flWorkRoutingHelperStatus = _FlWorkRoutingHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 7, 1, 2),
    _FlWorkRoutingHelperStatus_Type()
)
flWorkRoutingHelperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingHelperStatus.setStatus("current")
_FlWorkRoutingIpIcmpControl_ObjectIdentity = ObjectIdentity
flWorkRoutingIpIcmpControl = _FlWorkRoutingIpIcmpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 8)
)


class _FlWorkRoutingIpIcmpEchoReplyMode_Type(Integer32):
    """Custom type flWorkRoutingIpIcmpEchoReplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpIcmpEchoReplyMode_Type.__name__ = "Integer32"
_FlWorkRoutingIpIcmpEchoReplyMode_Object = MibScalar
flWorkRoutingIpIcmpEchoReplyMode = _FlWorkRoutingIpIcmpEchoReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 8, 1),
    _FlWorkRoutingIpIcmpEchoReplyMode_Type()
)
flWorkRoutingIpIcmpEchoReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpIcmpEchoReplyMode.setStatus("current")


class _FlWorkRoutingIpIcmpRedirectsMode_Type(Integer32):
    """Custom type flWorkRoutingIpIcmpRedirectsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingIpIcmpRedirectsMode_Type.__name__ = "Integer32"
_FlWorkRoutingIpIcmpRedirectsMode_Object = MibScalar
flWorkRoutingIpIcmpRedirectsMode = _FlWorkRoutingIpIcmpRedirectsMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 8, 2),
    _FlWorkRoutingIpIcmpRedirectsMode_Type()
)
flWorkRoutingIpIcmpRedirectsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpIcmpRedirectsMode.setStatus("current")


class _FlWorkRoutingIpIcmpRateLimitInterval_Type(Integer32):
    """Custom type flWorkRoutingIpIcmpRateLimitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FlWorkRoutingIpIcmpRateLimitInterval_Type.__name__ = "Integer32"
_FlWorkRoutingIpIcmpRateLimitInterval_Object = MibScalar
flWorkRoutingIpIcmpRateLimitInterval = _FlWorkRoutingIpIcmpRateLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 8, 3),
    _FlWorkRoutingIpIcmpRateLimitInterval_Type()
)
flWorkRoutingIpIcmpRateLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpIcmpRateLimitInterval.setStatus("current")


class _FlWorkRoutingIpIcmpRateLimitBurstSize_Type(Integer32):
    """Custom type flWorkRoutingIpIcmpRateLimitBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_FlWorkRoutingIpIcmpRateLimitBurstSize_Type.__name__ = "Integer32"
_FlWorkRoutingIpIcmpRateLimitBurstSize_Object = MibScalar
flWorkRoutingIpIcmpRateLimitBurstSize = _FlWorkRoutingIpIcmpRateLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 8, 4),
    _FlWorkRoutingIpIcmpRateLimitBurstSize_Type()
)
flWorkRoutingIpIcmpRateLimitBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIpIcmpRateLimitBurstSize.setStatus("current")
_FlWorkRoutingStaticRouteTable_Object = MibTable
flWorkRoutingStaticRouteTable = _FlWorkRoutingStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 9)
)
if mibBuilder.loadTexts:
    flWorkRoutingStaticRouteTable.setStatus("current")
_FlWorkRoutingStaticRouteEntry_Object = MibTableRow
flWorkRoutingStaticRouteEntry = _FlWorkRoutingStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 9, 1)
)
flWorkRoutingStaticRouteEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingStaticRouteTableIndex"),
)
if mibBuilder.loadTexts:
    flWorkRoutingStaticRouteEntry.setStatus("current")


class _FlWorkRoutingStaticRouteTableIndex_Type(Integer32):
    """Custom type flWorkRoutingStaticRouteTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FlWorkRoutingStaticRouteTableIndex_Type.__name__ = "Integer32"
_FlWorkRoutingStaticRouteTableIndex_Object = MibTableColumn
flWorkRoutingStaticRouteTableIndex = _FlWorkRoutingStaticRouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 9, 1, 1),
    _FlWorkRoutingStaticRouteTableIndex_Type()
)
flWorkRoutingStaticRouteTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingStaticRouteTableIndex.setStatus("current")
_FlWorkRoutingStaticRouteTableDestNetwork_Type = IpAddress
_FlWorkRoutingStaticRouteTableDestNetwork_Object = MibTableColumn
flWorkRoutingStaticRouteTableDestNetwork = _FlWorkRoutingStaticRouteTableDestNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 9, 1, 2),
    _FlWorkRoutingStaticRouteTableDestNetwork_Type()
)
flWorkRoutingStaticRouteTableDestNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingStaticRouteTableDestNetwork.setStatus("current")
_FlWorkRoutingStaticRouteTableDestSubnetMask_Type = IpAddress
_FlWorkRoutingStaticRouteTableDestSubnetMask_Object = MibTableColumn
flWorkRoutingStaticRouteTableDestSubnetMask = _FlWorkRoutingStaticRouteTableDestSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 9, 1, 3),
    _FlWorkRoutingStaticRouteTableDestSubnetMask_Type()
)
flWorkRoutingStaticRouteTableDestSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingStaticRouteTableDestSubnetMask.setStatus("current")
_FlWorkRoutingStaticRouteTableNextHop_Type = IpAddress
_FlWorkRoutingStaticRouteTableNextHop_Object = MibTableColumn
flWorkRoutingStaticRouteTableNextHop = _FlWorkRoutingStaticRouteTableNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 9, 1, 4),
    _FlWorkRoutingStaticRouteTableNextHop_Type()
)
flWorkRoutingStaticRouteTableNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingStaticRouteTableNextHop.setStatus("current")


class _FlWorkRoutingStaticRouteTablePreference_Type(Integer32):
    """Custom type flWorkRoutingStaticRouteTablePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FlWorkRoutingStaticRouteTablePreference_Type.__name__ = "Integer32"
_FlWorkRoutingStaticRouteTablePreference_Object = MibTableColumn
flWorkRoutingStaticRouteTablePreference = _FlWorkRoutingStaticRouteTablePreference_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 9, 1, 5),
    _FlWorkRoutingStaticRouteTablePreference_Type()
)
flWorkRoutingStaticRouteTablePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingStaticRouteTablePreference.setStatus("current")


class _FlWorkRoutingStaticRouteTableActive_Type(Integer32):
    """Custom type flWorkRoutingStaticRouteTableActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkRoutingStaticRouteTableActive_Type.__name__ = "Integer32"
_FlWorkRoutingStaticRouteTableActive_Object = MibTableColumn
flWorkRoutingStaticRouteTableActive = _FlWorkRoutingStaticRouteTableActive_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 9, 1, 6),
    _FlWorkRoutingStaticRouteTableActive_Type()
)
flWorkRoutingStaticRouteTableActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingStaticRouteTableActive.setStatus("current")
_FlWorkRoutingStaticRouteTableStatus_Type = RowStatus
_FlWorkRoutingStaticRouteTableStatus_Object = MibTableColumn
flWorkRoutingStaticRouteTableStatus = _FlWorkRoutingStaticRouteTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 1, 9, 1, 7),
    _FlWorkRoutingStaticRouteTableStatus_Type()
)
flWorkRoutingStaticRouteTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingStaticRouteTableStatus.setStatus("current")
_FlWorkRoutingArp_ObjectIdentity = ObjectIdentity
flWorkRoutingArp = _FlWorkRoutingArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2)
)


class _FlWorkRoutingArpAgeoutTime_Type(Integer32):
    """Custom type flWorkRoutingArpAgeoutTime based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 21600),
    )


_FlWorkRoutingArpAgeoutTime_Type.__name__ = "Integer32"
_FlWorkRoutingArpAgeoutTime_Object = MibScalar
flWorkRoutingArpAgeoutTime = _FlWorkRoutingArpAgeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 1),
    _FlWorkRoutingArpAgeoutTime_Type()
)
flWorkRoutingArpAgeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingArpAgeoutTime.setStatus("current")


class _FlWorkRoutingArpResponseTime_Type(Integer32):
    """Custom type flWorkRoutingArpResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FlWorkRoutingArpResponseTime_Type.__name__ = "Integer32"
_FlWorkRoutingArpResponseTime_Object = MibScalar
flWorkRoutingArpResponseTime = _FlWorkRoutingArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 2),
    _FlWorkRoutingArpResponseTime_Type()
)
flWorkRoutingArpResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingArpResponseTime.setStatus("current")


class _FlWorkRoutingArpMaxRetries_Type(Integer32):
    """Custom type flWorkRoutingArpMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FlWorkRoutingArpMaxRetries_Type.__name__ = "Integer32"
_FlWorkRoutingArpMaxRetries_Object = MibScalar
flWorkRoutingArpMaxRetries = _FlWorkRoutingArpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 3),
    _FlWorkRoutingArpMaxRetries_Type()
)
flWorkRoutingArpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingArpMaxRetries.setStatus("current")
_FlWorkRoutingArpCacheSize_Type = Integer32
_FlWorkRoutingArpCacheSize_Object = MibScalar
flWorkRoutingArpCacheSize = _FlWorkRoutingArpCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 4),
    _FlWorkRoutingArpCacheSize_Type()
)
flWorkRoutingArpCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingArpCacheSize.setStatus("current")


class _FlWorkRoutingArpDynamicRenew_Type(Integer32):
    """Custom type flWorkRoutingArpDynamicRenew based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingArpDynamicRenew_Type.__name__ = "Integer32"
_FlWorkRoutingArpDynamicRenew_Object = MibScalar
flWorkRoutingArpDynamicRenew = _FlWorkRoutingArpDynamicRenew_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 5),
    _FlWorkRoutingArpDynamicRenew_Type()
)
flWorkRoutingArpDynamicRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingArpDynamicRenew.setStatus("current")
_FlWorkRoutingArpTotalEntryCountCurrent_Type = Gauge32
_FlWorkRoutingArpTotalEntryCountCurrent_Object = MibScalar
flWorkRoutingArpTotalEntryCountCurrent = _FlWorkRoutingArpTotalEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 6),
    _FlWorkRoutingArpTotalEntryCountCurrent_Type()
)
flWorkRoutingArpTotalEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingArpTotalEntryCountCurrent.setStatus("current")
_FlWorkRoutingArpTotalEntryCountPeak_Type = Gauge32
_FlWorkRoutingArpTotalEntryCountPeak_Object = MibScalar
flWorkRoutingArpTotalEntryCountPeak = _FlWorkRoutingArpTotalEntryCountPeak_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 7),
    _FlWorkRoutingArpTotalEntryCountPeak_Type()
)
flWorkRoutingArpTotalEntryCountPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingArpTotalEntryCountPeak.setStatus("current")
_FlWorkRoutingArpStaticEntryCountCurrent_Type = Gauge32
_FlWorkRoutingArpStaticEntryCountCurrent_Object = MibScalar
flWorkRoutingArpStaticEntryCountCurrent = _FlWorkRoutingArpStaticEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 8),
    _FlWorkRoutingArpStaticEntryCountCurrent_Type()
)
flWorkRoutingArpStaticEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingArpStaticEntryCountCurrent.setStatus("current")
_FlWorkRoutingArpStaticEntryCountMax_Type = Integer32
_FlWorkRoutingArpStaticEntryCountMax_Object = MibScalar
flWorkRoutingArpStaticEntryCountMax = _FlWorkRoutingArpStaticEntryCountMax_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 9),
    _FlWorkRoutingArpStaticEntryCountMax_Type()
)
flWorkRoutingArpStaticEntryCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingArpStaticEntryCountMax.setStatus("current")
_FlWorkRoutingLocalProxyArpTable_Object = MibTable
flWorkRoutingLocalProxyArpTable = _FlWorkRoutingLocalProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 11)
)
if mibBuilder.loadTexts:
    flWorkRoutingLocalProxyArpTable.setStatus("current")
_FlWorkRoutingLocalProxyArpEntry_Object = MibTableRow
flWorkRoutingLocalProxyArpEntry = _FlWorkRoutingLocalProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 11, 1)
)
flWorkRoutingLocalProxyArpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    flWorkRoutingLocalProxyArpEntry.setStatus("current")


class _FlWorkRoutingLocalProxyArpMode_Type(Integer32):
    """Custom type flWorkRoutingLocalProxyArpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingLocalProxyArpMode_Type.__name__ = "Integer32"
_FlWorkRoutingLocalProxyArpMode_Object = MibTableColumn
flWorkRoutingLocalProxyArpMode = _FlWorkRoutingLocalProxyArpMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 11, 1, 1),
    _FlWorkRoutingLocalProxyArpMode_Type()
)
flWorkRoutingLocalProxyArpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingLocalProxyArpMode.setStatus("current")
_FlWorkRoutingIntfArpTable_Object = MibTable
flWorkRoutingIntfArpTable = _FlWorkRoutingIntfArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 12)
)
if mibBuilder.loadTexts:
    flWorkRoutingIntfArpTable.setStatus("current")
_FlWorkRoutingIntfArpEntry_Object = MibTableRow
flWorkRoutingIntfArpEntry = _FlWorkRoutingIntfArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 12, 1)
)
flWorkRoutingIntfArpEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingIntfArpIpAddress"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingIntfArpIfIndex"),
)
if mibBuilder.loadTexts:
    flWorkRoutingIntfArpEntry.setStatus("current")
_FlWorkRoutingIntfArpIpAddress_Type = IpAddress
_FlWorkRoutingIntfArpIpAddress_Object = MibTableColumn
flWorkRoutingIntfArpIpAddress = _FlWorkRoutingIntfArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 12, 1, 1),
    _FlWorkRoutingIntfArpIpAddress_Type()
)
flWorkRoutingIntfArpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingIntfArpIpAddress.setStatus("current")
_FlWorkRoutingIntfArpIfIndex_Type = InterfaceIndex
_FlWorkRoutingIntfArpIfIndex_Object = MibTableColumn
flWorkRoutingIntfArpIfIndex = _FlWorkRoutingIntfArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 12, 1, 2),
    _FlWorkRoutingIntfArpIfIndex_Type()
)
flWorkRoutingIntfArpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingIntfArpIfIndex.setStatus("current")
_FlWorkRoutingIntfArpAge_Type = TimeTicks
_FlWorkRoutingIntfArpAge_Object = MibTableColumn
flWorkRoutingIntfArpAge = _FlWorkRoutingIntfArpAge_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 12, 1, 3),
    _FlWorkRoutingIntfArpAge_Type()
)
flWorkRoutingIntfArpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingIntfArpAge.setStatus("current")
_FlWorkRoutingIntfArpMacAddress_Type = MacAddress
_FlWorkRoutingIntfArpMacAddress_Object = MibTableColumn
flWorkRoutingIntfArpMacAddress = _FlWorkRoutingIntfArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 12, 1, 4),
    _FlWorkRoutingIntfArpMacAddress_Type()
)
flWorkRoutingIntfArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingIntfArpMacAddress.setStatus("current")


class _FlWorkRoutingIntfArpType_Type(Integer32):
    """Custom type flWorkRoutingIntfArpType based on Integer32"""
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
        *(("local", 1),
          ("gateway", 2),
          ("static", 3),
          ("dynamic", 4))
    )


_FlWorkRoutingIntfArpType_Type.__name__ = "Integer32"
_FlWorkRoutingIntfArpType_Object = MibTableColumn
flWorkRoutingIntfArpType = _FlWorkRoutingIntfArpType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 12, 1, 5),
    _FlWorkRoutingIntfArpType_Type()
)
flWorkRoutingIntfArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingIntfArpType.setStatus("current")
_FlWorkRoutingIntfArpStatus_Type = RowStatus
_FlWorkRoutingIntfArpStatus_Object = MibTableColumn
flWorkRoutingIntfArpStatus = _FlWorkRoutingIntfArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 2, 12, 1, 6),
    _FlWorkRoutingIntfArpStatus_Type()
)
flWorkRoutingIntfArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingIntfArpStatus.setStatus("current")
_FlWorkRoutingVrrp_ObjectIdentity = ObjectIdentity
flWorkRoutingVrrp = _FlWorkRoutingVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3)
)


class _FlWorkRoutingVrrpAdminState_Type(Integer32):
    """Custom type flWorkRoutingVrrpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingVrrpAdminState_Type.__name__ = "Integer32"
_FlWorkRoutingVrrpAdminState_Object = MibScalar
flWorkRoutingVrrpAdminState = _FlWorkRoutingVrrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 1),
    _FlWorkRoutingVrrpAdminState_Type()
)
flWorkRoutingVrrpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpAdminState.setStatus("current")
_FlWorkRoutingVrrpOperTable_Object = MibTable
flWorkRoutingVrrpOperTable = _FlWorkRoutingVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 2)
)
if mibBuilder.loadTexts:
    flWorkRoutingVrrpOperTable.setStatus("current")
_FlWorkRoutingVrrpOperEntry_Object = MibTableRow
flWorkRoutingVrrpOperEntry = _FlWorkRoutingVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 2, 1)
)
flWorkRoutingVrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    flWorkRoutingVrrpOperEntry.setStatus("current")


class _FlWorkRoutingVrrpOperPriority_Type(Integer32):
    """Custom type flWorkRoutingVrrpOperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkRoutingVrrpOperPriority_Type.__name__ = "Integer32"
_FlWorkRoutingVrrpOperPriority_Object = MibTableColumn
flWorkRoutingVrrpOperPriority = _FlWorkRoutingVrrpOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 2, 1, 1),
    _FlWorkRoutingVrrpOperPriority_Type()
)
flWorkRoutingVrrpOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpOperPriority.setStatus("current")
_FlWorkRoutingVrrpTrackIntfTable_Object = MibTable
flWorkRoutingVrrpTrackIntfTable = _FlWorkRoutingVrrpTrackIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 3)
)
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackIntfTable.setStatus("current")
_FlWorkRoutingVrrpTrackIntfEntry_Object = MibTableRow
flWorkRoutingVrrpTrackIntfEntry = _FlWorkRoutingVrrpTrackIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 3, 1)
)
flWorkRoutingVrrpTrackIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingVrrpTrackIntf"),
)
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackIntfEntry.setStatus("current")
_FlWorkRoutingVrrpTrackIntf_Type = InterfaceIndex
_FlWorkRoutingVrrpTrackIntf_Object = MibTableColumn
flWorkRoutingVrrpTrackIntf = _FlWorkRoutingVrrpTrackIntf_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 3, 1, 1),
    _FlWorkRoutingVrrpTrackIntf_Type()
)
flWorkRoutingVrrpTrackIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackIntf.setStatus("current")


class _FlWorkRoutingVrrpTrackIfPrioDec_Type(Integer32):
    """Custom type flWorkRoutingVrrpTrackIfPrioDec based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FlWorkRoutingVrrpTrackIfPrioDec_Type.__name__ = "Integer32"
_FlWorkRoutingVrrpTrackIfPrioDec_Object = MibTableColumn
flWorkRoutingVrrpTrackIfPrioDec = _FlWorkRoutingVrrpTrackIfPrioDec_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 3, 1, 2),
    _FlWorkRoutingVrrpTrackIfPrioDec_Type()
)
flWorkRoutingVrrpTrackIfPrioDec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackIfPrioDec.setStatus("current")
_FlWorkRoutingVrrpTrackIfState_Type = Integer32
_FlWorkRoutingVrrpTrackIfState_Object = MibTableColumn
flWorkRoutingVrrpTrackIfState = _FlWorkRoutingVrrpTrackIfState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 3, 1, 3),
    _FlWorkRoutingVrrpTrackIfState_Type()
)
flWorkRoutingVrrpTrackIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackIfState.setStatus("current")
_FlWorkRoutingVrrpTrackIfStatus_Type = RowStatus
_FlWorkRoutingVrrpTrackIfStatus_Object = MibTableColumn
flWorkRoutingVrrpTrackIfStatus = _FlWorkRoutingVrrpTrackIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 3, 1, 4),
    _FlWorkRoutingVrrpTrackIfStatus_Type()
)
flWorkRoutingVrrpTrackIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackIfStatus.setStatus("current")
_FlWorkRoutingVrrpTrackRouteTable_Object = MibTable
flWorkRoutingVrrpTrackRouteTable = _FlWorkRoutingVrrpTrackRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 4)
)
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackRouteTable.setStatus("current")
_FlWorkRoutingVrrpTrackRouteEntry_Object = MibTableRow
flWorkRoutingVrrpTrackRouteEntry = _FlWorkRoutingVrrpTrackRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 4, 1)
)
flWorkRoutingVrrpTrackRouteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingVrrpTrackRtPfx"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingVrrpTrackRtPfxLen"),
)
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackRouteEntry.setStatus("current")
_FlWorkRoutingVrrpTrackRtPfx_Type = IpAddress
_FlWorkRoutingVrrpTrackRtPfx_Object = MibTableColumn
flWorkRoutingVrrpTrackRtPfx = _FlWorkRoutingVrrpTrackRtPfx_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 4, 1, 1),
    _FlWorkRoutingVrrpTrackRtPfx_Type()
)
flWorkRoutingVrrpTrackRtPfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackRtPfx.setStatus("current")


class _FlWorkRoutingVrrpTrackRtPfxLen_Type(Integer32):
    """Custom type flWorkRoutingVrrpTrackRtPfxLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FlWorkRoutingVrrpTrackRtPfxLen_Type.__name__ = "Integer32"
_FlWorkRoutingVrrpTrackRtPfxLen_Object = MibTableColumn
flWorkRoutingVrrpTrackRtPfxLen = _FlWorkRoutingVrrpTrackRtPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 4, 1, 2),
    _FlWorkRoutingVrrpTrackRtPfxLen_Type()
)
flWorkRoutingVrrpTrackRtPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackRtPfxLen.setStatus("current")


class _FlWorkRoutingVrrpTrackRtPrioDec_Type(Integer32):
    """Custom type flWorkRoutingVrrpTrackRtPrioDec based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FlWorkRoutingVrrpTrackRtPrioDec_Type.__name__ = "Integer32"
_FlWorkRoutingVrrpTrackRtPrioDec_Object = MibTableColumn
flWorkRoutingVrrpTrackRtPrioDec = _FlWorkRoutingVrrpTrackRtPrioDec_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 4, 1, 3),
    _FlWorkRoutingVrrpTrackRtPrioDec_Type()
)
flWorkRoutingVrrpTrackRtPrioDec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackRtPrioDec.setStatus("current")
_FlWorkRoutingVrrpTrackRtReachable_Type = Integer32
_FlWorkRoutingVrrpTrackRtReachable_Object = MibTableColumn
flWorkRoutingVrrpTrackRtReachable = _FlWorkRoutingVrrpTrackRtReachable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 4, 1, 4),
    _FlWorkRoutingVrrpTrackRtReachable_Type()
)
flWorkRoutingVrrpTrackRtReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackRtReachable.setStatus("current")
_FlWorkRoutingVrrpTrackRtStatus_Type = RowStatus
_FlWorkRoutingVrrpTrackRtStatus_Object = MibTableColumn
flWorkRoutingVrrpTrackRtStatus = _FlWorkRoutingVrrpTrackRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 4, 1, 5),
    _FlWorkRoutingVrrpTrackRtStatus_Type()
)
flWorkRoutingVrrpTrackRtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpTrackRtStatus.setStatus("current")


class _FlWorkRoutingVrrpIcmpEcho_Type(Integer32):
    """Custom type flWorkRoutingVrrpIcmpEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingVrrpIcmpEcho_Type.__name__ = "Integer32"
_FlWorkRoutingVrrpIcmpEcho_Object = MibScalar
flWorkRoutingVrrpIcmpEcho = _FlWorkRoutingVrrpIcmpEcho_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 3, 5),
    _FlWorkRoutingVrrpIcmpEcho_Type()
)
flWorkRoutingVrrpIcmpEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingVrrpIcmpEcho.setStatus("current")
_FlWorkRoutingRip_ObjectIdentity = ObjectIdentity
flWorkRoutingRip = _FlWorkRoutingRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4)
)


class _FlWorkRoutingRipAdminState_Type(Integer32):
    """Custom type flWorkRoutingRipAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingRipAdminState_Type.__name__ = "Integer32"
_FlWorkRoutingRipAdminState_Object = MibScalar
flWorkRoutingRipAdminState = _FlWorkRoutingRipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 1),
    _FlWorkRoutingRipAdminState_Type()
)
flWorkRoutingRipAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipAdminState.setStatus("current")


class _FlWorkRoutingRipSplitHorizonMode_Type(Integer32):
    """Custom type flWorkRoutingRipSplitHorizonMode based on Integer32"""
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
        *(("none", 1),
          ("simple", 2),
          ("poisonReverse", 3))
    )


_FlWorkRoutingRipSplitHorizonMode_Type.__name__ = "Integer32"
_FlWorkRoutingRipSplitHorizonMode_Object = MibScalar
flWorkRoutingRipSplitHorizonMode = _FlWorkRoutingRipSplitHorizonMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 2),
    _FlWorkRoutingRipSplitHorizonMode_Type()
)
flWorkRoutingRipSplitHorizonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipSplitHorizonMode.setStatus("current")


class _FlWorkRoutingRipAutoSummaryMode_Type(Integer32):
    """Custom type flWorkRoutingRipAutoSummaryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingRipAutoSummaryMode_Type.__name__ = "Integer32"
_FlWorkRoutingRipAutoSummaryMode_Object = MibScalar
flWorkRoutingRipAutoSummaryMode = _FlWorkRoutingRipAutoSummaryMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 3),
    _FlWorkRoutingRipAutoSummaryMode_Type()
)
flWorkRoutingRipAutoSummaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipAutoSummaryMode.setStatus("current")


class _FlWorkRoutingRipHostRoutesAcceptMode_Type(Integer32):
    """Custom type flWorkRoutingRipHostRoutesAcceptMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingRipHostRoutesAcceptMode_Type.__name__ = "Integer32"
_FlWorkRoutingRipHostRoutesAcceptMode_Object = MibScalar
flWorkRoutingRipHostRoutesAcceptMode = _FlWorkRoutingRipHostRoutesAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 4),
    _FlWorkRoutingRipHostRoutesAcceptMode_Type()
)
flWorkRoutingRipHostRoutesAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipHostRoutesAcceptMode.setStatus("current")


class _FlWorkRoutingRipDefaultMetric_Type(Integer32):
    """Custom type flWorkRoutingRipDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FlWorkRoutingRipDefaultMetric_Type.__name__ = "Integer32"
_FlWorkRoutingRipDefaultMetric_Object = MibScalar
flWorkRoutingRipDefaultMetric = _FlWorkRoutingRipDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 5),
    _FlWorkRoutingRipDefaultMetric_Type()
)
flWorkRoutingRipDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipDefaultMetric.setStatus("current")
_FlWorkRoutingRipDefaultMetricConfigured_Type = TruthValue
_FlWorkRoutingRipDefaultMetricConfigured_Object = MibScalar
flWorkRoutingRipDefaultMetricConfigured = _FlWorkRoutingRipDefaultMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 6),
    _FlWorkRoutingRipDefaultMetricConfigured_Type()
)
flWorkRoutingRipDefaultMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipDefaultMetricConfigured.setStatus("current")


class _FlWorkRoutingRipDefaultInfoOriginate_Type(TruthValue):
    """Custom type flWorkRoutingRipDefaultInfoOriginate based on TruthValue"""
    defaultValue = 2


_FlWorkRoutingRipDefaultInfoOriginate_Type.__name__ = "TruthValue"
_FlWorkRoutingRipDefaultInfoOriginate_Object = MibScalar
flWorkRoutingRipDefaultInfoOriginate = _FlWorkRoutingRipDefaultInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 7),
    _FlWorkRoutingRipDefaultInfoOriginate_Type()
)
flWorkRoutingRipDefaultInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipDefaultInfoOriginate.setStatus("current")
_FlWorkRoutingRipRouteRedistTable_Object = MibTable
flWorkRoutingRipRouteRedistTable = _FlWorkRoutingRipRouteRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8)
)
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistTable.setStatus("current")
_FlWorkRoutingRipRouteRedistEntry_Object = MibTableRow
flWorkRoutingRipRouteRedistEntry = _FlWorkRoutingRipRouteRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1)
)
flWorkRoutingRipRouteRedistEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingRipRouteRedistSource"),
)
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistEntry.setStatus("current")


class _FlWorkRoutingRipRouteRedistSource_Type(Integer32):
    """Custom type flWorkRoutingRipRouteRedistSource based on Integer32"""
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
        *(("connected", 1),
          ("static", 2),
          ("ospf", 3),
          ("bgp", 4))
    )


_FlWorkRoutingRipRouteRedistSource_Type.__name__ = "Integer32"
_FlWorkRoutingRipRouteRedistSource_Object = MibTableColumn
flWorkRoutingRipRouteRedistSource = _FlWorkRoutingRipRouteRedistSource_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 1),
    _FlWorkRoutingRipRouteRedistSource_Type()
)
flWorkRoutingRipRouteRedistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistSource.setStatus("current")


class _FlWorkRoutingRipRouteRedistMode_Type(Integer32):
    """Custom type flWorkRoutingRipRouteRedistMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingRipRouteRedistMode_Type.__name__ = "Integer32"
_FlWorkRoutingRipRouteRedistMode_Object = MibTableColumn
flWorkRoutingRipRouteRedistMode = _FlWorkRoutingRipRouteRedistMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 2),
    _FlWorkRoutingRipRouteRedistMode_Type()
)
flWorkRoutingRipRouteRedistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistMode.setStatus("current")


class _FlWorkRoutingRipRouteRedistMetric_Type(Integer32):
    """Custom type flWorkRoutingRipRouteRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FlWorkRoutingRipRouteRedistMetric_Type.__name__ = "Integer32"
_FlWorkRoutingRipRouteRedistMetric_Object = MibTableColumn
flWorkRoutingRipRouteRedistMetric = _FlWorkRoutingRipRouteRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 3),
    _FlWorkRoutingRipRouteRedistMetric_Type()
)
flWorkRoutingRipRouteRedistMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistMetric.setStatus("current")
_FlWorkRoutingRipRouteRedistMetricConfigured_Type = TruthValue
_FlWorkRoutingRipRouteRedistMetricConfigured_Object = MibTableColumn
flWorkRoutingRipRouteRedistMetricConfigured = _FlWorkRoutingRipRouteRedistMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 4),
    _FlWorkRoutingRipRouteRedistMetricConfigured_Type()
)
flWorkRoutingRipRouteRedistMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistMetricConfigured.setStatus("current")


class _FlWorkRoutingRipRouteRedistMatchInternal_Type(Integer32):
    """Custom type flWorkRoutingRipRouteRedistMatchInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_FlWorkRoutingRipRouteRedistMatchInternal_Type.__name__ = "Integer32"
_FlWorkRoutingRipRouteRedistMatchInternal_Object = MibTableColumn
flWorkRoutingRipRouteRedistMatchInternal = _FlWorkRoutingRipRouteRedistMatchInternal_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 5),
    _FlWorkRoutingRipRouteRedistMatchInternal_Type()
)
flWorkRoutingRipRouteRedistMatchInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistMatchInternal.setStatus("current")


class _FlWorkRoutingRipRouteRedistMatchExternal1_Type(Integer32):
    """Custom type flWorkRoutingRipRouteRedistMatchExternal1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_FlWorkRoutingRipRouteRedistMatchExternal1_Type.__name__ = "Integer32"
_FlWorkRoutingRipRouteRedistMatchExternal1_Object = MibTableColumn
flWorkRoutingRipRouteRedistMatchExternal1 = _FlWorkRoutingRipRouteRedistMatchExternal1_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 6),
    _FlWorkRoutingRipRouteRedistMatchExternal1_Type()
)
flWorkRoutingRipRouteRedistMatchExternal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistMatchExternal1.setStatus("current")


class _FlWorkRoutingRipRouteRedistMatchExternal2_Type(Integer32):
    """Custom type flWorkRoutingRipRouteRedistMatchExternal2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_FlWorkRoutingRipRouteRedistMatchExternal2_Type.__name__ = "Integer32"
_FlWorkRoutingRipRouteRedistMatchExternal2_Object = MibTableColumn
flWorkRoutingRipRouteRedistMatchExternal2 = _FlWorkRoutingRipRouteRedistMatchExternal2_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 7),
    _FlWorkRoutingRipRouteRedistMatchExternal2_Type()
)
flWorkRoutingRipRouteRedistMatchExternal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistMatchExternal2.setStatus("current")


class _FlWorkRoutingRipRouteRedistMatchNSSAExternal1_Type(Integer32):
    """Custom type flWorkRoutingRipRouteRedistMatchNSSAExternal1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_FlWorkRoutingRipRouteRedistMatchNSSAExternal1_Type.__name__ = "Integer32"
_FlWorkRoutingRipRouteRedistMatchNSSAExternal1_Object = MibTableColumn
flWorkRoutingRipRouteRedistMatchNSSAExternal1 = _FlWorkRoutingRipRouteRedistMatchNSSAExternal1_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 8),
    _FlWorkRoutingRipRouteRedistMatchNSSAExternal1_Type()
)
flWorkRoutingRipRouteRedistMatchNSSAExternal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistMatchNSSAExternal1.setStatus("current")


class _FlWorkRoutingRipRouteRedistMatchNSSAExternal2_Type(Integer32):
    """Custom type flWorkRoutingRipRouteRedistMatchNSSAExternal2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("not-applicable", 3))
    )


_FlWorkRoutingRipRouteRedistMatchNSSAExternal2_Type.__name__ = "Integer32"
_FlWorkRoutingRipRouteRedistMatchNSSAExternal2_Object = MibTableColumn
flWorkRoutingRipRouteRedistMatchNSSAExternal2 = _FlWorkRoutingRipRouteRedistMatchNSSAExternal2_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 9),
    _FlWorkRoutingRipRouteRedistMatchNSSAExternal2_Type()
)
flWorkRoutingRipRouteRedistMatchNSSAExternal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistMatchNSSAExternal2.setStatus("current")


class _FlWorkRoutingRipRouteRedistDistList_Type(Unsigned32):
    """Custom type flWorkRoutingRipRouteRedistDistList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_FlWorkRoutingRipRouteRedistDistList_Type.__name__ = "Unsigned32"
_FlWorkRoutingRipRouteRedistDistList_Object = MibTableColumn
flWorkRoutingRipRouteRedistDistList = _FlWorkRoutingRipRouteRedistDistList_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 10),
    _FlWorkRoutingRipRouteRedistDistList_Type()
)
flWorkRoutingRipRouteRedistDistList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistDistList.setStatus("current")
_FlWorkRoutingRipRouteRedistDistListConfigured_Type = TruthValue
_FlWorkRoutingRipRouteRedistDistListConfigured_Object = MibTableColumn
flWorkRoutingRipRouteRedistDistListConfigured = _FlWorkRoutingRipRouteRedistDistListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 8, 1, 11),
    _FlWorkRoutingRipRouteRedistDistListConfigured_Type()
)
flWorkRoutingRipRouteRedistDistListConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingRipRouteRedistDistListConfigured.setStatus("current")
_FlWorkRoutingRip2IfConfTable_Object = MibTable
flWorkRoutingRip2IfConfTable = _FlWorkRoutingRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 9)
)
if mibBuilder.loadTexts:
    flWorkRoutingRip2IfConfTable.setStatus("current")
_FlWorkRoutingRip2IfConfEntry_Object = MibTableRow
flWorkRoutingRip2IfConfEntry = _FlWorkRoutingRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 9, 1)
)
if mibBuilder.loadTexts:
    flWorkRoutingRip2IfConfEntry.setStatus("current")


class _FlWorkRoutingRip2IfConfAuthKeyId_Type(Integer32):
    """Custom type flWorkRoutingRip2IfConfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkRoutingRip2IfConfAuthKeyId_Type.__name__ = "Integer32"
_FlWorkRoutingRip2IfConfAuthKeyId_Object = MibTableColumn
flWorkRoutingRip2IfConfAuthKeyId = _FlWorkRoutingRip2IfConfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 4, 9, 1, 1),
    _FlWorkRoutingRip2IfConfAuthKeyId_Type()
)
flWorkRoutingRip2IfConfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingRip2IfConfAuthKeyId.setStatus("current")
_FlWorkRoutingOspf_ObjectIdentity = ObjectIdentity
flWorkRoutingOspf = _FlWorkRoutingOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5)
)


class _FlWorkRoutingOspfDefaultMetric_Type(Integer32):
    """Custom type flWorkRoutingOspfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_FlWorkRoutingOspfDefaultMetric_Type.__name__ = "Integer32"
_FlWorkRoutingOspfDefaultMetric_Object = MibScalar
flWorkRoutingOspfDefaultMetric = _FlWorkRoutingOspfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 1),
    _FlWorkRoutingOspfDefaultMetric_Type()
)
flWorkRoutingOspfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfDefaultMetric.setStatus("current")
_FlWorkRoutingOspfDefaultMetricConfigured_Type = TruthValue
_FlWorkRoutingOspfDefaultMetricConfigured_Object = MibScalar
flWorkRoutingOspfDefaultMetricConfigured = _FlWorkRoutingOspfDefaultMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 2),
    _FlWorkRoutingOspfDefaultMetricConfigured_Type()
)
flWorkRoutingOspfDefaultMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfDefaultMetricConfigured.setStatus("current")


class _FlWorkRoutingOspfDefaultInfoOriginate_Type(TruthValue):
    """Custom type flWorkRoutingOspfDefaultInfoOriginate based on TruthValue"""
    defaultValue = 2


_FlWorkRoutingOspfDefaultInfoOriginate_Type.__name__ = "TruthValue"
_FlWorkRoutingOspfDefaultInfoOriginate_Object = MibScalar
flWorkRoutingOspfDefaultInfoOriginate = _FlWorkRoutingOspfDefaultInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 3),
    _FlWorkRoutingOspfDefaultInfoOriginate_Type()
)
flWorkRoutingOspfDefaultInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfDefaultInfoOriginate.setStatus("current")


class _FlWorkRoutingOspfDefaultInfoOriginateAlways_Type(TruthValue):
    """Custom type flWorkRoutingOspfDefaultInfoOriginateAlways based on TruthValue"""
    defaultValue = 2


_FlWorkRoutingOspfDefaultInfoOriginateAlways_Type.__name__ = "TruthValue"
_FlWorkRoutingOspfDefaultInfoOriginateAlways_Object = MibScalar
flWorkRoutingOspfDefaultInfoOriginateAlways = _FlWorkRoutingOspfDefaultInfoOriginateAlways_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 4),
    _FlWorkRoutingOspfDefaultInfoOriginateAlways_Type()
)
flWorkRoutingOspfDefaultInfoOriginateAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfDefaultInfoOriginateAlways.setStatus("current")


class _FlWorkRoutingOspfDefaultInfoOriginateMetric_Type(Integer32):
    """Custom type flWorkRoutingOspfDefaultInfoOriginateMetric based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_FlWorkRoutingOspfDefaultInfoOriginateMetric_Type.__name__ = "Integer32"
_FlWorkRoutingOspfDefaultInfoOriginateMetric_Object = MibScalar
flWorkRoutingOspfDefaultInfoOriginateMetric = _FlWorkRoutingOspfDefaultInfoOriginateMetric_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 5),
    _FlWorkRoutingOspfDefaultInfoOriginateMetric_Type()
)
flWorkRoutingOspfDefaultInfoOriginateMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfDefaultInfoOriginateMetric.setStatus("current")
_FlWorkRoutingOspfDefaultInfoOriginateMetricConfigured_Type = TruthValue
_FlWorkRoutingOspfDefaultInfoOriginateMetricConfigured_Object = MibScalar
flWorkRoutingOspfDefaultInfoOriginateMetricConfigured = _FlWorkRoutingOspfDefaultInfoOriginateMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 6),
    _FlWorkRoutingOspfDefaultInfoOriginateMetricConfigured_Type()
)
flWorkRoutingOspfDefaultInfoOriginateMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfDefaultInfoOriginateMetricConfigured.setStatus("current")


class _FlWorkRoutingOspfDefaultInfoOriginateMetricType_Type(Integer32):
    """Custom type flWorkRoutingOspfDefaultInfoOriginateMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalType1", 1),
          ("externalType2", 2))
    )


_FlWorkRoutingOspfDefaultInfoOriginateMetricType_Type.__name__ = "Integer32"
_FlWorkRoutingOspfDefaultInfoOriginateMetricType_Object = MibScalar
flWorkRoutingOspfDefaultInfoOriginateMetricType = _FlWorkRoutingOspfDefaultInfoOriginateMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 7),
    _FlWorkRoutingOspfDefaultInfoOriginateMetricType_Type()
)
flWorkRoutingOspfDefaultInfoOriginateMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfDefaultInfoOriginateMetricType.setStatus("current")
_FlWorkRoutingOspfRouteRedistTable_Object = MibTable
flWorkRoutingOspfRouteRedistTable = _FlWorkRoutingOspfRouteRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8)
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistTable.setStatus("current")
_FlWorkRoutingOspfRouteRedistEntry_Object = MibTableRow
flWorkRoutingOspfRouteRedistEntry = _FlWorkRoutingOspfRouteRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1)
)
flWorkRoutingOspfRouteRedistEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfRouteRedistSource"),
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistEntry.setStatus("current")


class _FlWorkRoutingOspfRouteRedistSource_Type(Integer32):
    """Custom type flWorkRoutingOspfRouteRedistSource based on Integer32"""
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
        *(("connected", 1),
          ("static", 2),
          ("rip", 3),
          ("bgp", 4))
    )


_FlWorkRoutingOspfRouteRedistSource_Type.__name__ = "Integer32"
_FlWorkRoutingOspfRouteRedistSource_Object = MibTableColumn
flWorkRoutingOspfRouteRedistSource = _FlWorkRoutingOspfRouteRedistSource_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1, 1),
    _FlWorkRoutingOspfRouteRedistSource_Type()
)
flWorkRoutingOspfRouteRedistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistSource.setStatus("current")


class _FlWorkRoutingOspfRouteRedistMode_Type(Integer32):
    """Custom type flWorkRoutingOspfRouteRedistMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingOspfRouteRedistMode_Type.__name__ = "Integer32"
_FlWorkRoutingOspfRouteRedistMode_Object = MibTableColumn
flWorkRoutingOspfRouteRedistMode = _FlWorkRoutingOspfRouteRedistMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1, 2),
    _FlWorkRoutingOspfRouteRedistMode_Type()
)
flWorkRoutingOspfRouteRedistMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistMode.setStatus("current")


class _FlWorkRoutingOspfRouteRedistMetric_Type(Integer32):
    """Custom type flWorkRoutingOspfRouteRedistMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_FlWorkRoutingOspfRouteRedistMetric_Type.__name__ = "Integer32"
_FlWorkRoutingOspfRouteRedistMetric_Object = MibTableColumn
flWorkRoutingOspfRouteRedistMetric = _FlWorkRoutingOspfRouteRedistMetric_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1, 3),
    _FlWorkRoutingOspfRouteRedistMetric_Type()
)
flWorkRoutingOspfRouteRedistMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistMetric.setStatus("current")
_FlWorkRoutingOspfRouteRedistMetricConfigured_Type = TruthValue
_FlWorkRoutingOspfRouteRedistMetricConfigured_Object = MibTableColumn
flWorkRoutingOspfRouteRedistMetricConfigured = _FlWorkRoutingOspfRouteRedistMetricConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1, 4),
    _FlWorkRoutingOspfRouteRedistMetricConfigured_Type()
)
flWorkRoutingOspfRouteRedistMetricConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistMetricConfigured.setStatus("current")


class _FlWorkRoutingOspfRouteRedistMetricType_Type(Integer32):
    """Custom type flWorkRoutingOspfRouteRedistMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalType1", 1),
          ("externalType2", 2))
    )


_FlWorkRoutingOspfRouteRedistMetricType_Type.__name__ = "Integer32"
_FlWorkRoutingOspfRouteRedistMetricType_Object = MibTableColumn
flWorkRoutingOspfRouteRedistMetricType = _FlWorkRoutingOspfRouteRedistMetricType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1, 5),
    _FlWorkRoutingOspfRouteRedistMetricType_Type()
)
flWorkRoutingOspfRouteRedistMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistMetricType.setStatus("current")


class _FlWorkRoutingOspfRouteRedistTag_Type(Unsigned32):
    """Custom type flWorkRoutingOspfRouteRedistTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FlWorkRoutingOspfRouteRedistTag_Type.__name__ = "Unsigned32"
_FlWorkRoutingOspfRouteRedistTag_Object = MibTableColumn
flWorkRoutingOspfRouteRedistTag = _FlWorkRoutingOspfRouteRedistTag_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1, 6),
    _FlWorkRoutingOspfRouteRedistTag_Type()
)
flWorkRoutingOspfRouteRedistTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistTag.setStatus("current")


class _FlWorkRoutingOspfRouteRedistSubnets_Type(TruthValue):
    """Custom type flWorkRoutingOspfRouteRedistSubnets based on TruthValue"""
    defaultValue = 2


_FlWorkRoutingOspfRouteRedistSubnets_Type.__name__ = "TruthValue"
_FlWorkRoutingOspfRouteRedistSubnets_Object = MibTableColumn
flWorkRoutingOspfRouteRedistSubnets = _FlWorkRoutingOspfRouteRedistSubnets_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1, 7),
    _FlWorkRoutingOspfRouteRedistSubnets_Type()
)
flWorkRoutingOspfRouteRedistSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistSubnets.setStatus("current")


class _FlWorkRoutingOspfRouteRedistDistList_Type(Unsigned32):
    """Custom type flWorkRoutingOspfRouteRedistDistList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_FlWorkRoutingOspfRouteRedistDistList_Type.__name__ = "Unsigned32"
_FlWorkRoutingOspfRouteRedistDistList_Object = MibTableColumn
flWorkRoutingOspfRouteRedistDistList = _FlWorkRoutingOspfRouteRedistDistList_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1, 8),
    _FlWorkRoutingOspfRouteRedistDistList_Type()
)
flWorkRoutingOspfRouteRedistDistList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistDistList.setStatus("current")
_FlWorkRoutingOspfRouteRedistDistListConfigured_Type = TruthValue
_FlWorkRoutingOspfRouteRedistDistListConfigured_Object = MibTableColumn
flWorkRoutingOspfRouteRedistDistListConfigured = _FlWorkRoutingOspfRouteRedistDistListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 8, 1, 9),
    _FlWorkRoutingOspfRouteRedistDistListConfigured_Type()
)
flWorkRoutingOspfRouteRedistDistListConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRouteRedistDistListConfigured.setStatus("current")
_FlWorkRoutingOspfIfTable_Object = MibTable
flWorkRoutingOspfIfTable = _FlWorkRoutingOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 9)
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfIfTable.setStatus("current")
_FlWorkRoutingOspfIfEntry_Object = MibTableRow
flWorkRoutingOspfIfEntry = _FlWorkRoutingOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 9, 1)
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfIfEntry.setStatus("current")


class _FlWorkRoutingOspfIfAuthKeyId_Type(Integer32):
    """Custom type flWorkRoutingOspfIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkRoutingOspfIfAuthKeyId_Type.__name__ = "Integer32"
_FlWorkRoutingOspfIfAuthKeyId_Object = MibTableColumn
flWorkRoutingOspfIfAuthKeyId = _FlWorkRoutingOspfIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 9, 1, 1),
    _FlWorkRoutingOspfIfAuthKeyId_Type()
)
flWorkRoutingOspfIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingOspfIfAuthKeyId.setStatus("current")


class _FlWorkRoutingOspfIfIpMtuIgnoreFlag_Type(Integer32):
    """Custom type flWorkRoutingOspfIfIpMtuIgnoreFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingOspfIfIpMtuIgnoreFlag_Type.__name__ = "Integer32"
_FlWorkRoutingOspfIfIpMtuIgnoreFlag_Object = MibTableColumn
flWorkRoutingOspfIfIpMtuIgnoreFlag = _FlWorkRoutingOspfIfIpMtuIgnoreFlag_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 9, 1, 2),
    _FlWorkRoutingOspfIfIpMtuIgnoreFlag_Type()
)
flWorkRoutingOspfIfIpMtuIgnoreFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfIfIpMtuIgnoreFlag.setStatus("current")


class _FlWorkRoutingOspfIfPassiveMode_Type(TruthValue):
    """Custom type flWorkRoutingOspfIfPassiveMode based on TruthValue"""
    defaultValue = 2


_FlWorkRoutingOspfIfPassiveMode_Type.__name__ = "TruthValue"
_FlWorkRoutingOspfIfPassiveMode_Object = MibTableColumn
flWorkRoutingOspfIfPassiveMode = _FlWorkRoutingOspfIfPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 9, 1, 3),
    _FlWorkRoutingOspfIfPassiveMode_Type()
)
flWorkRoutingOspfIfPassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfIfPassiveMode.setStatus("current")
_FlWorkRoutingOspfVirtIfTable_Object = MibTable
flWorkRoutingOspfVirtIfTable = _FlWorkRoutingOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 10)
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfVirtIfTable.setStatus("current")
_FlWorkRoutingOspfVirtIfEntry_Object = MibTableRow
flWorkRoutingOspfVirtIfEntry = _FlWorkRoutingOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 10, 1)
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfVirtIfEntry.setStatus("current")


class _FlWorkRoutingOspfVirtIfAuthKeyId_Type(Integer32):
    """Custom type flWorkRoutingOspfVirtIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlWorkRoutingOspfVirtIfAuthKeyId_Type.__name__ = "Integer32"
_FlWorkRoutingOspfVirtIfAuthKeyId_Object = MibTableColumn
flWorkRoutingOspfVirtIfAuthKeyId = _FlWorkRoutingOspfVirtIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 10, 1, 1),
    _FlWorkRoutingOspfVirtIfAuthKeyId_Type()
)
flWorkRoutingOspfVirtIfAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingOspfVirtIfAuthKeyId.setStatus("current")


class _FlWorkRoutingOspfRFC1583CompatibilityMode_Type(Integer32):
    """Custom type flWorkRoutingOspfRFC1583CompatibilityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FlWorkRoutingOspfRFC1583CompatibilityMode_Type.__name__ = "Integer32"
_FlWorkRoutingOspfRFC1583CompatibilityMode_Object = MibScalar
flWorkRoutingOspfRFC1583CompatibilityMode = _FlWorkRoutingOspfRFC1583CompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 11),
    _FlWorkRoutingOspfRFC1583CompatibilityMode_Type()
)
flWorkRoutingOspfRFC1583CompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfRFC1583CompatibilityMode.setStatus("current")


class _FlWorkRoutingOspfSpfDelayTime_Type(Integer32):
    """Custom type flWorkRoutingOspfSpfDelayTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlWorkRoutingOspfSpfDelayTime_Type.__name__ = "Integer32"
_FlWorkRoutingOspfSpfDelayTime_Object = MibScalar
flWorkRoutingOspfSpfDelayTime = _FlWorkRoutingOspfSpfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 12),
    _FlWorkRoutingOspfSpfDelayTime_Type()
)
flWorkRoutingOspfSpfDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfSpfDelayTime.setStatus("current")


class _FlWorkRoutingOspfSpfHoldTime_Type(Integer32):
    """Custom type flWorkRoutingOspfSpfHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlWorkRoutingOspfSpfHoldTime_Type.__name__ = "Integer32"
_FlWorkRoutingOspfSpfHoldTime_Object = MibScalar
flWorkRoutingOspfSpfHoldTime = _FlWorkRoutingOspfSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 13),
    _FlWorkRoutingOspfSpfHoldTime_Type()
)
flWorkRoutingOspfSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfSpfHoldTime.setStatus("current")


class _FlWorkRoutingOspfAutoCostRefBw_Type(Unsigned32):
    """Custom type flWorkRoutingOspfAutoCostRefBw based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967),
    )


_FlWorkRoutingOspfAutoCostRefBw_Type.__name__ = "Unsigned32"
_FlWorkRoutingOspfAutoCostRefBw_Object = MibScalar
flWorkRoutingOspfAutoCostRefBw = _FlWorkRoutingOspfAutoCostRefBw_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 14),
    _FlWorkRoutingOspfAutoCostRefBw_Type()
)
flWorkRoutingOspfAutoCostRefBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAutoCostRefBw.setStatus("current")
_FlWorkRoutingOspfOpaqueLsaSupport_Type = TruthValue
_FlWorkRoutingOspfOpaqueLsaSupport_Object = MibScalar
flWorkRoutingOspfOpaqueLsaSupport = _FlWorkRoutingOspfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 15),
    _FlWorkRoutingOspfOpaqueLsaSupport_Type()
)
flWorkRoutingOspfOpaqueLsaSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfOpaqueLsaSupport.setStatus("current")
_FlWorkRoutingOspfAreaOpaqueLsdbTable_Object = MibTable
flWorkRoutingOspfAreaOpaqueLsdbTable = _FlWorkRoutingOspfAreaOpaqueLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16)
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbTable.setStatus("current")
_FlWorkRoutingOspfAreaOpaqueLsdbEntry_Object = MibTableRow
flWorkRoutingOspfAreaOpaqueLsdbEntry = _FlWorkRoutingOspfAreaOpaqueLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16, 1)
)
flWorkRoutingOspfAreaOpaqueLsdbEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfAreaOpaqueLsdbAreaId"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfAreaOpaqueLsdbType"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfAreaOpaqueLsdbLsid"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfAreaOpaqueLsdbRouterId"),
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbEntry.setStatus("current")
_FlWorkRoutingOspfAreaOpaqueLsdbAreaId_Type = IpAddress
_FlWorkRoutingOspfAreaOpaqueLsdbAreaId_Object = MibTableColumn
flWorkRoutingOspfAreaOpaqueLsdbAreaId = _FlWorkRoutingOspfAreaOpaqueLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16, 1, 1),
    _FlWorkRoutingOspfAreaOpaqueLsdbAreaId_Type()
)
flWorkRoutingOspfAreaOpaqueLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbAreaId.setStatus("current")


class _FlWorkRoutingOspfAreaOpaqueLsdbType_Type(Integer32):
    """Custom type flWorkRoutingOspfAreaOpaqueLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("areaOpaqueLink", 10)
    )


_FlWorkRoutingOspfAreaOpaqueLsdbType_Type.__name__ = "Integer32"
_FlWorkRoutingOspfAreaOpaqueLsdbType_Object = MibTableColumn
flWorkRoutingOspfAreaOpaqueLsdbType = _FlWorkRoutingOspfAreaOpaqueLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16, 1, 2),
    _FlWorkRoutingOspfAreaOpaqueLsdbType_Type()
)
flWorkRoutingOspfAreaOpaqueLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbType.setStatus("current")
_FlWorkRoutingOspfAreaOpaqueLsdbLsid_Type = IpAddress
_FlWorkRoutingOspfAreaOpaqueLsdbLsid_Object = MibTableColumn
flWorkRoutingOspfAreaOpaqueLsdbLsid = _FlWorkRoutingOspfAreaOpaqueLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16, 1, 3),
    _FlWorkRoutingOspfAreaOpaqueLsdbLsid_Type()
)
flWorkRoutingOspfAreaOpaqueLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbLsid.setStatus("current")
_FlWorkRoutingOspfAreaOpaqueLsdbRouterId_Type = IpAddress
_FlWorkRoutingOspfAreaOpaqueLsdbRouterId_Object = MibTableColumn
flWorkRoutingOspfAreaOpaqueLsdbRouterId = _FlWorkRoutingOspfAreaOpaqueLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16, 1, 4),
    _FlWorkRoutingOspfAreaOpaqueLsdbRouterId_Type()
)
flWorkRoutingOspfAreaOpaqueLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbRouterId.setStatus("current")
_FlWorkRoutingOspfAreaOpaqueLsdbSequence_Type = Integer32
_FlWorkRoutingOspfAreaOpaqueLsdbSequence_Object = MibTableColumn
flWorkRoutingOspfAreaOpaqueLsdbSequence = _FlWorkRoutingOspfAreaOpaqueLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16, 1, 5),
    _FlWorkRoutingOspfAreaOpaqueLsdbSequence_Type()
)
flWorkRoutingOspfAreaOpaqueLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbSequence.setStatus("current")
_FlWorkRoutingOspfAreaOpaqueLsdbAge_Type = Integer32
_FlWorkRoutingOspfAreaOpaqueLsdbAge_Object = MibTableColumn
flWorkRoutingOspfAreaOpaqueLsdbAge = _FlWorkRoutingOspfAreaOpaqueLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16, 1, 6),
    _FlWorkRoutingOspfAreaOpaqueLsdbAge_Type()
)
flWorkRoutingOspfAreaOpaqueLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbAge.setUnits("seconds")
_FlWorkRoutingOspfAreaOpaqueLsdbChecksum_Type = Integer32
_FlWorkRoutingOspfAreaOpaqueLsdbChecksum_Object = MibTableColumn
flWorkRoutingOspfAreaOpaqueLsdbChecksum = _FlWorkRoutingOspfAreaOpaqueLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16, 1, 7),
    _FlWorkRoutingOspfAreaOpaqueLsdbChecksum_Type()
)
flWorkRoutingOspfAreaOpaqueLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbChecksum.setStatus("current")


class _FlWorkRoutingOspfAreaOpaqueLsdbAdvertisement_Type(OctetString):
    """Custom type flWorkRoutingOspfAreaOpaqueLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FlWorkRoutingOspfAreaOpaqueLsdbAdvertisement_Type.__name__ = "OctetString"
_FlWorkRoutingOspfAreaOpaqueLsdbAdvertisement_Object = MibTableColumn
flWorkRoutingOspfAreaOpaqueLsdbAdvertisement = _FlWorkRoutingOspfAreaOpaqueLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 16, 1, 8),
    _FlWorkRoutingOspfAreaOpaqueLsdbAdvertisement_Type()
)
flWorkRoutingOspfAreaOpaqueLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAreaOpaqueLsdbAdvertisement.setStatus("current")
_FlWorkRoutingOspfLocalLsdbTable_Object = MibTable
flWorkRoutingOspfLocalLsdbTable = _FlWorkRoutingOspfLocalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17)
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbTable.setStatus("current")
_FlWorkRoutingOspfLocalLsdbEntry_Object = MibTableRow
flWorkRoutingOspfLocalLsdbEntry = _FlWorkRoutingOspfLocalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1)
)
flWorkRoutingOspfLocalLsdbEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfLocalLsdbIpAddress"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfLocalLsdbAddressLessIf"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfLocalLsdbType"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfLocalLsdbLsid"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbEntry.setStatus("current")
_FlWorkRoutingOspfLocalLsdbIpAddress_Type = IpAddress
_FlWorkRoutingOspfLocalLsdbIpAddress_Object = MibTableColumn
flWorkRoutingOspfLocalLsdbIpAddress = _FlWorkRoutingOspfLocalLsdbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1, 1),
    _FlWorkRoutingOspfLocalLsdbIpAddress_Type()
)
flWorkRoutingOspfLocalLsdbIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbIpAddress.setStatus("current")
_FlWorkRoutingOspfLocalLsdbAddressLessIf_Type = InterfaceIndexOrZero
_FlWorkRoutingOspfLocalLsdbAddressLessIf_Object = MibTableColumn
flWorkRoutingOspfLocalLsdbAddressLessIf = _FlWorkRoutingOspfLocalLsdbAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1, 2),
    _FlWorkRoutingOspfLocalLsdbAddressLessIf_Type()
)
flWorkRoutingOspfLocalLsdbAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbAddressLessIf.setStatus("current")


class _FlWorkRoutingOspfLocalLsdbType_Type(Integer32):
    """Custom type flWorkRoutingOspfLocalLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("localOpaqueLink", 9)
    )


_FlWorkRoutingOspfLocalLsdbType_Type.__name__ = "Integer32"
_FlWorkRoutingOspfLocalLsdbType_Object = MibTableColumn
flWorkRoutingOspfLocalLsdbType = _FlWorkRoutingOspfLocalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1, 3),
    _FlWorkRoutingOspfLocalLsdbType_Type()
)
flWorkRoutingOspfLocalLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbType.setStatus("current")
_FlWorkRoutingOspfLocalLsdbLsid_Type = IpAddress
_FlWorkRoutingOspfLocalLsdbLsid_Object = MibTableColumn
flWorkRoutingOspfLocalLsdbLsid = _FlWorkRoutingOspfLocalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1, 4),
    _FlWorkRoutingOspfLocalLsdbLsid_Type()
)
flWorkRoutingOspfLocalLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbLsid.setStatus("current")
_FlWorkRoutingOspfLocalLsdbRouterId_Type = RouterID
_FlWorkRoutingOspfLocalLsdbRouterId_Object = MibTableColumn
flWorkRoutingOspfLocalLsdbRouterId = _FlWorkRoutingOspfLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1, 5),
    _FlWorkRoutingOspfLocalLsdbRouterId_Type()
)
flWorkRoutingOspfLocalLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbRouterId.setStatus("current")
_FlWorkRoutingOspfLocalLsdbSequence_Type = Integer32
_FlWorkRoutingOspfLocalLsdbSequence_Object = MibTableColumn
flWorkRoutingOspfLocalLsdbSequence = _FlWorkRoutingOspfLocalLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1, 6),
    _FlWorkRoutingOspfLocalLsdbSequence_Type()
)
flWorkRoutingOspfLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbSequence.setStatus("current")
_FlWorkRoutingOspfLocalLsdbAge_Type = Integer32
_FlWorkRoutingOspfLocalLsdbAge_Object = MibTableColumn
flWorkRoutingOspfLocalLsdbAge = _FlWorkRoutingOspfLocalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1, 7),
    _FlWorkRoutingOspfLocalLsdbAge_Type()
)
flWorkRoutingOspfLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbAge.setUnits("seconds")
_FlWorkRoutingOspfLocalLsdbChecksum_Type = Integer32
_FlWorkRoutingOspfLocalLsdbChecksum_Object = MibTableColumn
flWorkRoutingOspfLocalLsdbChecksum = _FlWorkRoutingOspfLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1, 8),
    _FlWorkRoutingOspfLocalLsdbChecksum_Type()
)
flWorkRoutingOspfLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbChecksum.setStatus("current")


class _FlWorkRoutingOspfLocalLsdbAdvertisement_Type(OctetString):
    """Custom type flWorkRoutingOspfLocalLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FlWorkRoutingOspfLocalLsdbAdvertisement_Type.__name__ = "OctetString"
_FlWorkRoutingOspfLocalLsdbAdvertisement_Object = MibTableColumn
flWorkRoutingOspfLocalLsdbAdvertisement = _FlWorkRoutingOspfLocalLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 17, 1, 9),
    _FlWorkRoutingOspfLocalLsdbAdvertisement_Type()
)
flWorkRoutingOspfLocalLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfLocalLsdbAdvertisement.setStatus("current")
_FlWorkRoutingOspfAsLsdbTable_Object = MibTable
flWorkRoutingOspfAsLsdbTable = _FlWorkRoutingOspfAsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 18)
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbTable.setStatus("current")
_FlWorkRoutingOspfAsLsdbEntry_Object = MibTableRow
flWorkRoutingOspfAsLsdbEntry = _FlWorkRoutingOspfAsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 18, 1)
)
flWorkRoutingOspfAsLsdbEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfAsLsdbType"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfAsLsdbLsid"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingOspfAsLsdbRouterId"),
)
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbEntry.setStatus("current")


class _FlWorkRoutingOspfAsLsdbType_Type(Integer32):
    """Custom type flWorkRoutingOspfAsLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            11
        )
    )
    namedValues = NamedValues(
        ("asOpaqueLink", 11)
    )


_FlWorkRoutingOspfAsLsdbType_Type.__name__ = "Integer32"
_FlWorkRoutingOspfAsLsdbType_Object = MibTableColumn
flWorkRoutingOspfAsLsdbType = _FlWorkRoutingOspfAsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 18, 1, 1),
    _FlWorkRoutingOspfAsLsdbType_Type()
)
flWorkRoutingOspfAsLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbType.setStatus("current")
_FlWorkRoutingOspfAsLsdbLsid_Type = IpAddress
_FlWorkRoutingOspfAsLsdbLsid_Object = MibTableColumn
flWorkRoutingOspfAsLsdbLsid = _FlWorkRoutingOspfAsLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 18, 1, 2),
    _FlWorkRoutingOspfAsLsdbLsid_Type()
)
flWorkRoutingOspfAsLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbLsid.setStatus("current")
_FlWorkRoutingOspfAsLsdbRouterId_Type = RouterID
_FlWorkRoutingOspfAsLsdbRouterId_Object = MibTableColumn
flWorkRoutingOspfAsLsdbRouterId = _FlWorkRoutingOspfAsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 18, 1, 3),
    _FlWorkRoutingOspfAsLsdbRouterId_Type()
)
flWorkRoutingOspfAsLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbRouterId.setStatus("current")
_FlWorkRoutingOspfAsLsdbSequence_Type = Integer32
_FlWorkRoutingOspfAsLsdbSequence_Object = MibTableColumn
flWorkRoutingOspfAsLsdbSequence = _FlWorkRoutingOspfAsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 18, 1, 4),
    _FlWorkRoutingOspfAsLsdbSequence_Type()
)
flWorkRoutingOspfAsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbSequence.setStatus("current")
_FlWorkRoutingOspfAsLsdbAge_Type = Integer32
_FlWorkRoutingOspfAsLsdbAge_Object = MibTableColumn
flWorkRoutingOspfAsLsdbAge = _FlWorkRoutingOspfAsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 18, 1, 5),
    _FlWorkRoutingOspfAsLsdbAge_Type()
)
flWorkRoutingOspfAsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbAge.setUnits("seconds")
_FlWorkRoutingOspfAsLsdbChecksum_Type = Integer32
_FlWorkRoutingOspfAsLsdbChecksum_Object = MibTableColumn
flWorkRoutingOspfAsLsdbChecksum = _FlWorkRoutingOspfAsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 18, 1, 6),
    _FlWorkRoutingOspfAsLsdbChecksum_Type()
)
flWorkRoutingOspfAsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbChecksum.setStatus("current")


class _FlWorkRoutingOspfAsLsdbAdvertisement_Type(OctetString):
    """Custom type flWorkRoutingOspfAsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FlWorkRoutingOspfAsLsdbAdvertisement_Type.__name__ = "OctetString"
_FlWorkRoutingOspfAsLsdbAdvertisement_Object = MibTableColumn
flWorkRoutingOspfAsLsdbAdvertisement = _FlWorkRoutingOspfAsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 18, 1, 7),
    _FlWorkRoutingOspfAsLsdbAdvertisement_Type()
)
flWorkRoutingOspfAsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingOspfAsLsdbAdvertisement.setStatus("current")


class _FlWorkRoutingOspfDefaultPassiveMode_Type(TruthValue):
    """Custom type flWorkRoutingOspfDefaultPassiveMode based on TruthValue"""
    defaultValue = 2


_FlWorkRoutingOspfDefaultPassiveMode_Type.__name__ = "TruthValue"
_FlWorkRoutingOspfDefaultPassiveMode_Object = MibScalar
flWorkRoutingOspfDefaultPassiveMode = _FlWorkRoutingOspfDefaultPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 5, 19),
    _FlWorkRoutingOspfDefaultPassiveMode_Type()
)
flWorkRoutingOspfDefaultPassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingOspfDefaultPassiveMode.setStatus("current")
_FlWorkRoutingLoopback_ObjectIdentity = ObjectIdentity
flWorkRoutingLoopback = _FlWorkRoutingLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 6)
)
_FlWorkRoutingLoopbackTable_Object = MibTable
flWorkRoutingLoopbackTable = _FlWorkRoutingLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 6, 1)
)
if mibBuilder.loadTexts:
    flWorkRoutingLoopbackTable.setStatus("current")
_FlWorkRoutingLoopbackEntry_Object = MibTableRow
flWorkRoutingLoopbackEntry = _FlWorkRoutingLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 6, 1, 1)
)
flWorkRoutingLoopbackEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingLoopbackID"),
)
if mibBuilder.loadTexts:
    flWorkRoutingLoopbackEntry.setStatus("current")


class _FlWorkRoutingLoopbackID_Type(Integer32):
    """Custom type flWorkRoutingLoopbackID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkRoutingLoopbackID_Type.__name__ = "Integer32"
_FlWorkRoutingLoopbackID_Object = MibTableColumn
flWorkRoutingLoopbackID = _FlWorkRoutingLoopbackID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 6, 1, 1, 1),
    _FlWorkRoutingLoopbackID_Type()
)
flWorkRoutingLoopbackID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flWorkRoutingLoopbackID.setStatus("current")
_FlWorkRoutingLoopbackIfIndex_Type = Integer32
_FlWorkRoutingLoopbackIfIndex_Object = MibTableColumn
flWorkRoutingLoopbackIfIndex = _FlWorkRoutingLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 6, 1, 1, 2),
    _FlWorkRoutingLoopbackIfIndex_Type()
)
flWorkRoutingLoopbackIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingLoopbackIfIndex.setStatus("current")
_FlWorkRoutingLoopbackIPAddress_Type = IpAddress
_FlWorkRoutingLoopbackIPAddress_Object = MibTableColumn
flWorkRoutingLoopbackIPAddress = _FlWorkRoutingLoopbackIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 6, 1, 1, 3),
    _FlWorkRoutingLoopbackIPAddress_Type()
)
flWorkRoutingLoopbackIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingLoopbackIPAddress.setStatus("current")
_FlWorkRoutingLoopbackIPSubnet_Type = IpAddress
_FlWorkRoutingLoopbackIPSubnet_Object = MibTableColumn
flWorkRoutingLoopbackIPSubnet = _FlWorkRoutingLoopbackIPSubnet_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 6, 1, 1, 4),
    _FlWorkRoutingLoopbackIPSubnet_Type()
)
flWorkRoutingLoopbackIPSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingLoopbackIPSubnet.setStatus("current")
_FlWorkRoutingLoopbackStatus_Type = RowStatus
_FlWorkRoutingLoopbackStatus_Object = MibTableColumn
flWorkRoutingLoopbackStatus = _FlWorkRoutingLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 6, 1, 1, 5),
    _FlWorkRoutingLoopbackStatus_Type()
)
flWorkRoutingLoopbackStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingLoopbackStatus.setStatus("current")
_FlWorkRoutingNAT_ObjectIdentity = ObjectIdentity
flWorkRoutingNAT = _FlWorkRoutingNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7)
)
_FlWorkRoutingNATIntfCtrl_ObjectIdentity = ObjectIdentity
flWorkRoutingNATIntfCtrl = _FlWorkRoutingNATIntfCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 1)
)
_FlWorkRoutingNATIntfCtrlTable_Object = MibTable
flWorkRoutingNATIntfCtrlTable = _FlWorkRoutingNATIntfCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 1, 1)
)
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfCtrlTable.setStatus("current")
_FlWorkRoutingNATIntfCtrlEntry_Object = MibTableRow
flWorkRoutingNATIntfCtrlEntry = _FlWorkRoutingNATIntfCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 1, 1, 1)
)
flWorkRoutingNATIntfCtrlEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingNATIntfCtrlIntfIndex"),
)
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfCtrlEntry.setStatus("current")


class _FlWorkRoutingNATIntfCtrlIntfIndex_Type(Integer32):
    """Custom type flWorkRoutingNATIntfCtrlIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FlWorkRoutingNATIntfCtrlIntfIndex_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfCtrlIntfIndex_Object = MibTableColumn
flWorkRoutingNATIntfCtrlIntfIndex = _FlWorkRoutingNATIntfCtrlIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 1, 1, 1, 1),
    _FlWorkRoutingNATIntfCtrlIntfIndex_Type()
)
flWorkRoutingNATIntfCtrlIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfCtrlIntfIndex.setStatus("current")


class _FlWorkRoutingNATIntfCtrlIntfMode_Type(Integer32):
    """Custom type flWorkRoutingNATIntfCtrlIntfMode based on Integer32"""
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
        *(("none", 0),
          ("oneToOne", 1),
          ("virtual", 2),
          ("masquerade", 3))
    )


_FlWorkRoutingNATIntfCtrlIntfMode_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfCtrlIntfMode_Object = MibTableColumn
flWorkRoutingNATIntfCtrlIntfMode = _FlWorkRoutingNATIntfCtrlIntfMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 1, 1, 1, 2),
    _FlWorkRoutingNATIntfCtrlIntfMode_Type()
)
flWorkRoutingNATIntfCtrlIntfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfCtrlIntfMode.setStatus("current")
_FlWorkRoutingNATIntfForwarding_ObjectIdentity = ObjectIdentity
flWorkRoutingNATIntfForwarding = _FlWorkRoutingNATIntfForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2)
)
_FlWorkRoutingNATIntfForwardingTable_Object = MibTable
flWorkRoutingNATIntfForwardingTable = _FlWorkRoutingNATIntfForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1)
)
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTable.setStatus("current")
_FlWorkRoutingNATIntfForwardingEntry_Object = MibTableRow
flWorkRoutingNATIntfForwardingEntry = _FlWorkRoutingNATIntfForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1)
)
flWorkRoutingNATIntfForwardingEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingNATIntfForwardingIntfIndex"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingNATIntfForwardingTableIndex"),
)
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingEntry.setStatus("current")


class _FlWorkRoutingNATIntfForwardingIntfIndex_Type(Integer32):
    """Custom type flWorkRoutingNATIntfForwardingIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FlWorkRoutingNATIntfForwardingIntfIndex_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfForwardingIntfIndex_Object = MibTableColumn
flWorkRoutingNATIntfForwardingIntfIndex = _FlWorkRoutingNATIntfForwardingIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 1),
    _FlWorkRoutingNATIntfForwardingIntfIndex_Type()
)
flWorkRoutingNATIntfForwardingIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingIntfIndex.setStatus("current")


class _FlWorkRoutingNATIntfForwardingTableIndex_Type(Integer32):
    """Custom type flWorkRoutingNATIntfForwardingTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_FlWorkRoutingNATIntfForwardingTableIndex_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfForwardingTableIndex_Object = MibTableColumn
flWorkRoutingNATIntfForwardingTableIndex = _FlWorkRoutingNATIntfForwardingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 2),
    _FlWorkRoutingNATIntfForwardingTableIndex_Type()
)
flWorkRoutingNATIntfForwardingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTableIndex.setStatus("current")


class _FlWorkRoutingNATIntfForwardingTableProtocol_Type(Integer32):
    """Custom type flWorkRoutingNATIntfForwardingTableProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("both", 3))
    )


_FlWorkRoutingNATIntfForwardingTableProtocol_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfForwardingTableProtocol_Object = MibTableColumn
flWorkRoutingNATIntfForwardingTableProtocol = _FlWorkRoutingNATIntfForwardingTableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 3),
    _FlWorkRoutingNATIntfForwardingTableProtocol_Type()
)
flWorkRoutingNATIntfForwardingTableProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTableProtocol.setStatus("current")


class _FlWorkRoutingNATIntfForwardingTableDirection_Type(Integer32):
    """Custom type flWorkRoutingNATIntfForwardingTableDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("destination", 2))
    )


_FlWorkRoutingNATIntfForwardingTableDirection_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfForwardingTableDirection_Object = MibTableColumn
flWorkRoutingNATIntfForwardingTableDirection = _FlWorkRoutingNATIntfForwardingTableDirection_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 4),
    _FlWorkRoutingNATIntfForwardingTableDirection_Type()
)
flWorkRoutingNATIntfForwardingTableDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTableDirection.setStatus("current")
_FlWorkRoutingNATIntfForwardingTableInboundAddr_Type = IpAddress
_FlWorkRoutingNATIntfForwardingTableInboundAddr_Object = MibTableColumn
flWorkRoutingNATIntfForwardingTableInboundAddr = _FlWorkRoutingNATIntfForwardingTableInboundAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 5),
    _FlWorkRoutingNATIntfForwardingTableInboundAddr_Type()
)
flWorkRoutingNATIntfForwardingTableInboundAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTableInboundAddr.setStatus("current")
_FlWorkRoutingNATIntfForwardingTableInboundPort_Type = Integer32
_FlWorkRoutingNATIntfForwardingTableInboundPort_Object = MibTableColumn
flWorkRoutingNATIntfForwardingTableInboundPort = _FlWorkRoutingNATIntfForwardingTableInboundPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 6),
    _FlWorkRoutingNATIntfForwardingTableInboundPort_Type()
)
flWorkRoutingNATIntfForwardingTableInboundPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTableInboundPort.setStatus("current")
_FlWorkRoutingNATIntfForwardingTableOutboundAddr_Type = IpAddress
_FlWorkRoutingNATIntfForwardingTableOutboundAddr_Object = MibTableColumn
flWorkRoutingNATIntfForwardingTableOutboundAddr = _FlWorkRoutingNATIntfForwardingTableOutboundAddr_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 7),
    _FlWorkRoutingNATIntfForwardingTableOutboundAddr_Type()
)
flWorkRoutingNATIntfForwardingTableOutboundAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTableOutboundAddr.setStatus("current")
_FlWorkRoutingNATIntfForwardingTableOutboundPort_Type = Integer32
_FlWorkRoutingNATIntfForwardingTableOutboundPort_Object = MibTableColumn
flWorkRoutingNATIntfForwardingTableOutboundPort = _FlWorkRoutingNATIntfForwardingTableOutboundPort_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 8),
    _FlWorkRoutingNATIntfForwardingTableOutboundPort_Type()
)
flWorkRoutingNATIntfForwardingTableOutboundPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTableOutboundPort.setStatus("current")


class _FlWorkRoutingNATIntfForwardingTableActive_Type(Integer32):
    """Custom type flWorkRoutingNATIntfForwardingTableActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkRoutingNATIntfForwardingTableActive_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfForwardingTableActive_Object = MibTableColumn
flWorkRoutingNATIntfForwardingTableActive = _FlWorkRoutingNATIntfForwardingTableActive_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 9),
    _FlWorkRoutingNATIntfForwardingTableActive_Type()
)
flWorkRoutingNATIntfForwardingTableActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTableActive.setStatus("current")
_FlWorkRoutingNATIntfForwardingTableStatus_Type = RowStatus
_FlWorkRoutingNATIntfForwardingTableStatus_Object = MibTableColumn
flWorkRoutingNATIntfForwardingTableStatus = _FlWorkRoutingNATIntfForwardingTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 2, 1, 1, 10),
    _FlWorkRoutingNATIntfForwardingTableStatus_Type()
)
flWorkRoutingNATIntfForwardingTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfForwardingTableStatus.setStatus("current")
_FlWorkRoutingNATIntf1to1_ObjectIdentity = ObjectIdentity
flWorkRoutingNATIntf1to1 = _FlWorkRoutingNATIntf1to1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3)
)
_FlWorkRoutingNATIntf1to1Table_Object = MibTable
flWorkRoutingNATIntf1to1Table = _FlWorkRoutingNATIntf1to1Table_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3, 1)
)
if mibBuilder.loadTexts:
    flWorkRoutingNATIntf1to1Table.setStatus("current")
_FlWorkRoutingNATIntf1to1Entry_Object = MibTableRow
flWorkRoutingNATIntf1to1Entry = _FlWorkRoutingNATIntf1to1Entry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3, 1, 1)
)
flWorkRoutingNATIntf1to1Entry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingNATIntf1to1IntfIndex"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingNATIntf1to1TableIndex"),
)
if mibBuilder.loadTexts:
    flWorkRoutingNATIntf1to1Entry.setStatus("current")


class _FlWorkRoutingNATIntf1to1IntfIndex_Type(Integer32):
    """Custom type flWorkRoutingNATIntf1to1IntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FlWorkRoutingNATIntf1to1IntfIndex_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntf1to1IntfIndex_Object = MibTableColumn
flWorkRoutingNATIntf1to1IntfIndex = _FlWorkRoutingNATIntf1to1IntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3, 1, 1, 1),
    _FlWorkRoutingNATIntf1to1IntfIndex_Type()
)
flWorkRoutingNATIntf1to1IntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntf1to1IntfIndex.setStatus("current")


class _FlWorkRoutingNATIntf1to1TableIndex_Type(Integer32):
    """Custom type flWorkRoutingNATIntf1to1TableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FlWorkRoutingNATIntf1to1TableIndex_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntf1to1TableIndex_Object = MibTableColumn
flWorkRoutingNATIntf1to1TableIndex = _FlWorkRoutingNATIntf1to1TableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3, 1, 1, 2),
    _FlWorkRoutingNATIntf1to1TableIndex_Type()
)
flWorkRoutingNATIntf1to1TableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntf1to1TableIndex.setStatus("current")
_FlWorkRoutingNATIntf1to1TableExternalNetwork_Type = IpAddress
_FlWorkRoutingNATIntf1to1TableExternalNetwork_Object = MibTableColumn
flWorkRoutingNATIntf1to1TableExternalNetwork = _FlWorkRoutingNATIntf1to1TableExternalNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3, 1, 1, 3),
    _FlWorkRoutingNATIntf1to1TableExternalNetwork_Type()
)
flWorkRoutingNATIntf1to1TableExternalNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntf1to1TableExternalNetwork.setStatus("current")
_FlWorkRoutingNATIntf1to1TableInternalNetwork_Type = IpAddress
_FlWorkRoutingNATIntf1to1TableInternalNetwork_Object = MibTableColumn
flWorkRoutingNATIntf1to1TableInternalNetwork = _FlWorkRoutingNATIntf1to1TableInternalNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3, 1, 1, 4),
    _FlWorkRoutingNATIntf1to1TableInternalNetwork_Type()
)
flWorkRoutingNATIntf1to1TableInternalNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntf1to1TableInternalNetwork.setStatus("current")


class _FlWorkRoutingNATIntf1to1TableRange_Type(Integer32):
    """Custom type flWorkRoutingNATIntf1to1TableRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FlWorkRoutingNATIntf1to1TableRange_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntf1to1TableRange_Object = MibTableColumn
flWorkRoutingNATIntf1to1TableRange = _FlWorkRoutingNATIntf1to1TableRange_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3, 1, 1, 5),
    _FlWorkRoutingNATIntf1to1TableRange_Type()
)
flWorkRoutingNATIntf1to1TableRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntf1to1TableRange.setStatus("current")


class _FlWorkRoutingNATIntf1to1TableActive_Type(Integer32):
    """Custom type flWorkRoutingNATIntf1to1TableActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWorkRoutingNATIntf1to1TableActive_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntf1to1TableActive_Object = MibTableColumn
flWorkRoutingNATIntf1to1TableActive = _FlWorkRoutingNATIntf1to1TableActive_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3, 1, 1, 6),
    _FlWorkRoutingNATIntf1to1TableActive_Type()
)
flWorkRoutingNATIntf1to1TableActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntf1to1TableActive.setStatus("current")
_FlWorkRoutingNATIntf1to1TableStatus_Type = RowStatus
_FlWorkRoutingNATIntf1to1TableStatus_Object = MibTableColumn
flWorkRoutingNATIntf1to1TableStatus = _FlWorkRoutingNATIntf1to1TableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 3, 1, 1, 7),
    _FlWorkRoutingNATIntf1to1TableStatus_Type()
)
flWorkRoutingNATIntf1to1TableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntf1to1TableStatus.setStatus("current")
_FlWorkRoutingNATIntfVirtual_ObjectIdentity = ObjectIdentity
flWorkRoutingNATIntfVirtual = _FlWorkRoutingNATIntfVirtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 4)
)
_FlWorkRoutingNATIntfVirtualTable_Object = MibTable
flWorkRoutingNATIntfVirtualTable = _FlWorkRoutingNATIntfVirtualTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 4, 1)
)
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfVirtualTable.setStatus("current")
_FlWorkRoutingNATIntfVirtualEntry_Object = MibTableRow
flWorkRoutingNATIntfVirtualEntry = _FlWorkRoutingNATIntfVirtualEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 4, 1, 1)
)
flWorkRoutingNATIntfVirtualEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingNATIntfVirtualIntfIndex"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkRoutingNATIntfVirtualTableIndex"),
)
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfVirtualEntry.setStatus("current")


class _FlWorkRoutingNATIntfVirtualIntfIndex_Type(Integer32):
    """Custom type flWorkRoutingNATIntfVirtualIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FlWorkRoutingNATIntfVirtualIntfIndex_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfVirtualIntfIndex_Object = MibTableColumn
flWorkRoutingNATIntfVirtualIntfIndex = _FlWorkRoutingNATIntfVirtualIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 4, 1, 1, 1),
    _FlWorkRoutingNATIntfVirtualIntfIndex_Type()
)
flWorkRoutingNATIntfVirtualIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfVirtualIntfIndex.setStatus("current")


class _FlWorkRoutingNATIntfVirtualTableIndex_Type(Integer32):
    """Custom type flWorkRoutingNATIntfVirtualTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FlWorkRoutingNATIntfVirtualTableIndex_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfVirtualTableIndex_Object = MibTableColumn
flWorkRoutingNATIntfVirtualTableIndex = _FlWorkRoutingNATIntfVirtualTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 4, 1, 1, 2),
    _FlWorkRoutingNATIntfVirtualTableIndex_Type()
)
flWorkRoutingNATIntfVirtualTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfVirtualTableIndex.setStatus("current")
_FlWorkRoutingNATIntfVirtualTableVirtualNetwork_Type = IpAddress
_FlWorkRoutingNATIntfVirtualTableVirtualNetwork_Object = MibTableColumn
flWorkRoutingNATIntfVirtualTableVirtualNetwork = _FlWorkRoutingNATIntfVirtualTableVirtualNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 4, 1, 1, 3),
    _FlWorkRoutingNATIntfVirtualTableVirtualNetwork_Type()
)
flWorkRoutingNATIntfVirtualTableVirtualNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfVirtualTableVirtualNetwork.setStatus("current")
_FlWorkRoutingNATIntfVirtualTableInternalNetwork_Type = IpAddress
_FlWorkRoutingNATIntfVirtualTableInternalNetwork_Object = MibTableColumn
flWorkRoutingNATIntfVirtualTableInternalNetwork = _FlWorkRoutingNATIntfVirtualTableInternalNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 4, 1, 1, 4),
    _FlWorkRoutingNATIntfVirtualTableInternalNetwork_Type()
)
flWorkRoutingNATIntfVirtualTableInternalNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfVirtualTableInternalNetwork.setStatus("current")


class _FlWorkRoutingNATIntfVirtualTableRange_Type(Integer32):
    """Custom type flWorkRoutingNATIntfVirtualTableRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FlWorkRoutingNATIntfVirtualTableRange_Type.__name__ = "Integer32"
_FlWorkRoutingNATIntfVirtualTableRange_Object = MibTableColumn
flWorkRoutingNATIntfVirtualTableRange = _FlWorkRoutingNATIntfVirtualTableRange_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 23, 7, 4, 1, 1, 5),
    _FlWorkRoutingNATIntfVirtualTableRange_Type()
)
flWorkRoutingNATIntfVirtualTableRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkRoutingNATIntfVirtualTableRange.setStatus("current")
_FlWorkCip_ObjectIdentity = ObjectIdentity
flWorkCip = _FlWorkCip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25)
)
_FlWorkCipInfo_ObjectIdentity = ObjectIdentity
flWorkCipInfo = _FlWorkCipInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1)
)
_FlWorkCipActiveIOConns_Type = Integer32
_FlWorkCipActiveIOConns_Object = MibScalar
flWorkCipActiveIOConns = _FlWorkCipActiveIOConns_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 1),
    _FlWorkCipActiveIOConns_Type()
)
flWorkCipActiveIOConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipActiveIOConns.setStatus("current")
_FlWorkCipActiveExpMsgConns_Type = Integer32
_FlWorkCipActiveExpMsgConns_Object = MibScalar
flWorkCipActiveExpMsgConns = _FlWorkCipActiveExpMsgConns_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 2),
    _FlWorkCipActiveExpMsgConns_Type()
)
flWorkCipActiveExpMsgConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipActiveExpMsgConns.setStatus("current")
_FlWorkCipActiveMcastGroups_Type = Integer32
_FlWorkCipActiveMcastGroups_Object = MibScalar
flWorkCipActiveMcastGroups = _FlWorkCipActiveMcastGroups_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 3),
    _FlWorkCipActiveMcastGroups_Type()
)
flWorkCipActiveMcastGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipActiveMcastGroups.setStatus("current")
_FlWorkCipOpenRequestsRcvd_Type = Integer32
_FlWorkCipOpenRequestsRcvd_Object = MibScalar
flWorkCipOpenRequestsRcvd = _FlWorkCipOpenRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 4),
    _FlWorkCipOpenRequestsRcvd_Type()
)
flWorkCipOpenRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipOpenRequestsRcvd.setStatus("current")
_FlWorkCipOpenResourceRejects_Type = Integer32
_FlWorkCipOpenResourceRejects_Object = MibScalar
flWorkCipOpenResourceRejects = _FlWorkCipOpenResourceRejects_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 5),
    _FlWorkCipOpenResourceRejects_Type()
)
flWorkCipOpenResourceRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipOpenResourceRejects.setStatus("current")
_FlWorkCipOpenFormatRejects_Type = Integer32
_FlWorkCipOpenFormatRejects_Object = MibScalar
flWorkCipOpenFormatRejects = _FlWorkCipOpenFormatRejects_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 6),
    _FlWorkCipOpenFormatRejects_Type()
)
flWorkCipOpenFormatRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipOpenFormatRejects.setStatus("current")
_FlWorkCipOpenOtherRejects_Type = Integer32
_FlWorkCipOpenOtherRejects_Object = MibScalar
flWorkCipOpenOtherRejects = _FlWorkCipOpenOtherRejects_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 7),
    _FlWorkCipOpenOtherRejects_Type()
)
flWorkCipOpenOtherRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipOpenOtherRejects.setStatus("current")
_FlWorkCipCloseRequests_Type = Integer32
_FlWorkCipCloseRequests_Object = MibScalar
flWorkCipCloseRequests = _FlWorkCipCloseRequests_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 8),
    _FlWorkCipCloseRequests_Type()
)
flWorkCipCloseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipCloseRequests.setStatus("current")
_FlWorkCipCloseFormatRejects_Type = Integer32
_FlWorkCipCloseFormatRejects_Object = MibScalar
flWorkCipCloseFormatRejects = _FlWorkCipCloseFormatRejects_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 9),
    _FlWorkCipCloseFormatRejects_Type()
)
flWorkCipCloseFormatRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipCloseFormatRejects.setStatus("current")
_FlWorkCipCloseOtherRejects_Type = Integer32
_FlWorkCipCloseOtherRejects_Object = MibScalar
flWorkCipCloseOtherRejects = _FlWorkCipCloseOtherRejects_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 10),
    _FlWorkCipCloseOtherRejects_Type()
)
flWorkCipCloseOtherRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipCloseOtherRejects.setStatus("current")
_FlWorkCipConnectionTimeouts_Type = Integer32
_FlWorkCipConnectionTimeouts_Object = MibScalar
flWorkCipConnectionTimeouts = _FlWorkCipConnectionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 11),
    _FlWorkCipConnectionTimeouts_Type()
)
flWorkCipConnectionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipConnectionTimeouts.setStatus("current")
_FlWorkCipNetworkStatus_Type = Integer32
_FlWorkCipNetworkStatus_Object = MibScalar
flWorkCipNetworkStatus = _FlWorkCipNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 12),
    _FlWorkCipNetworkStatus_Type()
)
flWorkCipNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipNetworkStatus.setStatus("current")
_FlWorkCipModuleStatus_Type = Integer32
_FlWorkCipModuleStatus_Object = MibScalar
flWorkCipModuleStatus = _FlWorkCipModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 13),
    _FlWorkCipModuleStatus_Type()
)
flWorkCipModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipModuleStatus.setStatus("current")


class _FlWorkCipClearStats_Type(Integer32):
    """Custom type flWorkCipClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 1),
          ("clear", 2))
    )


_FlWorkCipClearStats_Type.__name__ = "Integer32"
_FlWorkCipClearStats_Object = MibScalar
flWorkCipClearStats = _FlWorkCipClearStats_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 1, 14),
    _FlWorkCipClearStats_Type()
)
flWorkCipClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWorkCipClearStats.setStatus("current")
_FlWorkCipConnectionTable_Object = MibTable
flWorkCipConnectionTable = _FlWorkCipConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 2)
)
if mibBuilder.loadTexts:
    flWorkCipConnectionTable.setStatus("current")
_FlWorkCipConnectionEntry_Object = MibTableRow
flWorkCipConnectionEntry = _FlWorkCipConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 2, 1)
)
flWorkCipConnectionEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWorkCipConnectionID"),
)
if mibBuilder.loadTexts:
    flWorkCipConnectionEntry.setStatus("current")


class _FlWorkCipConnectionID_Type(Integer32):
    """Custom type flWorkCipConnectionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWorkCipConnectionID_Type.__name__ = "Integer32"
_FlWorkCipConnectionID_Object = MibTableColumn
flWorkCipConnectionID = _FlWorkCipConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 2, 1, 1),
    _FlWorkCipConnectionID_Type()
)
flWorkCipConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipConnectionID.setStatus("current")
_FlWorkCipConnectionOwnerIP_Type = IpAddress
_FlWorkCipConnectionOwnerIP_Object = MibTableColumn
flWorkCipConnectionOwnerIP = _FlWorkCipConnectionOwnerIP_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 2, 1, 2),
    _FlWorkCipConnectionOwnerIP_Type()
)
flWorkCipConnectionOwnerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipConnectionOwnerIP.setStatus("current")


class _FlWorkCipConnectionTransportClass_Type(Integer32):
    """Custom type flWorkCipConnectionTransportClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("class1", 1),
          ("class3", 3))
    )


_FlWorkCipConnectionTransportClass_Type.__name__ = "Integer32"
_FlWorkCipConnectionTransportClass_Object = MibTableColumn
flWorkCipConnectionTransportClass = _FlWorkCipConnectionTransportClass_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 25, 2, 1, 3),
    _FlWorkCipConnectionTransportClass_Type()
)
flWorkCipConnectionTransportClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWorkCipConnectionTransportClass.setStatus("current")
_FlWlan_ObjectIdentity = ObjectIdentity
flWlan = _FlWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27)
)
_FlWlanRadio_ObjectIdentity = ObjectIdentity
flWlanRadio = _FlWlanRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 1)
)
_FlWlanRadioHwTable_Object = MibTable
flWlanRadioHwTable = _FlWlanRadioHwTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 1, 1)
)
if mibBuilder.loadTexts:
    flWlanRadioHwTable.setStatus("current")
_FlWlanRadioHwEntry_Object = MibTableRow
flWlanRadioHwEntry = _FlWlanRadioHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 1, 1, 1)
)
flWlanRadioHwEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWlanRadioHwID"),
)
if mibBuilder.loadTexts:
    flWlanRadioHwEntry.setStatus("current")


class _FlWlanRadioHwID_Type(Integer32):
    """Custom type flWlanRadioHwID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWlanRadioHwID_Type.__name__ = "Integer32"
_FlWlanRadioHwID_Object = MibTableColumn
flWlanRadioHwID = _FlWlanRadioHwID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 1, 1, 1, 1),
    _FlWlanRadioHwID_Type()
)
flWlanRadioHwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanRadioHwID.setStatus("current")
_FlWlanRadioHwAntMask_Type = OctetString
_FlWlanRadioHwAntMask_Object = MibTableColumn
flWlanRadioHwAntMask = _FlWlanRadioHwAntMask_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 1, 1, 1, 2),
    _FlWlanRadioHwAntMask_Type()
)
flWlanRadioHwAntMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanRadioHwAntMask.setStatus("current")


class _FlWlanRadioHwAggMode_Type(Integer32):
    """Custom type flWlanRadioHwAggMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanRadioHwAggMode_Type.__name__ = "Integer32"
_FlWlanRadioHwAggMode_Object = MibTableColumn
flWlanRadioHwAggMode = _FlWlanRadioHwAggMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 1, 1, 1, 3),
    _FlWlanRadioHwAggMode_Type()
)
flWlanRadioHwAggMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanRadioHwAggMode.setStatus("current")
_FlWlanWifi_ObjectIdentity = ObjectIdentity
flWlanWifi = _FlWlanWifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2)
)
_FlWlanWifiVapTable_Object = MibTable
flWlanWifiVapTable = _FlWlanWifiVapTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1)
)
if mibBuilder.loadTexts:
    flWlanWifiVapTable.setStatus("current")
_FlWlanWifiVapEntry_Object = MibTableRow
flWlanWifiVapEntry = _FlWlanWifiVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1)
)
flWlanWifiVapEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWlanWifiVapID"),
)
if mibBuilder.loadTexts:
    flWlanWifiVapEntry.setStatus("current")


class _FlWlanWifiVapID_Type(Integer32):
    """Custom type flWlanWifiVapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWlanWifiVapID_Type.__name__ = "Integer32"
_FlWlanWifiVapID_Object = MibTableColumn
flWlanWifiVapID = _FlWlanWifiVapID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 1),
    _FlWlanWifiVapID_Type()
)
flWlanWifiVapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiVapID.setStatus("current")


class _FlWlanWifiVapFastEapolRetry_Type(Integer32):
    """Custom type flWlanWifiVapFastEapolRetry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanWifiVapFastEapolRetry_Type.__name__ = "Integer32"
_FlWlanWifiVapFastEapolRetry_Object = MibTableColumn
flWlanWifiVapFastEapolRetry = _FlWlanWifiVapFastEapolRetry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 2),
    _FlWlanWifiVapFastEapolRetry_Type()
)
flWlanWifiVapFastEapolRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapFastEapolRetry.setStatus("current")


class _FlWlanWifiVapHideSsid_Type(Integer32):
    """Custom type flWlanWifiVapHideSsid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanWifiVapHideSsid_Type.__name__ = "Integer32"
_FlWlanWifiVapHideSsid_Object = MibTableColumn
flWlanWifiVapHideSsid = _FlWlanWifiVapHideSsid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 3),
    _FlWlanWifiVapHideSsid_Type()
)
flWlanWifiVapHideSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapHideSsid.setStatus("current")


class _FlWlanWifiVapExcessiveRetries_Type(Integer32):
    """Custom type flWlanWifiVapExcessiveRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FlWlanWifiVapExcessiveRetries_Type.__name__ = "Integer32"
_FlWlanWifiVapExcessiveRetries_Object = MibTableColumn
flWlanWifiVapExcessiveRetries = _FlWlanWifiVapExcessiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 4),
    _FlWlanWifiVapExcessiveRetries_Type()
)
flWlanWifiVapExcessiveRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapExcessiveRetries.setStatus("current")


class _FlWlanWifiVapWdsBroadcast_Type(Integer32):
    """Custom type flWlanWifiVapWdsBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanWifiVapWdsBroadcast_Type.__name__ = "Integer32"
_FlWlanWifiVapWdsBroadcast_Object = MibTableColumn
flWlanWifiVapWdsBroadcast = _FlWlanWifiVapWdsBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 5),
    _FlWlanWifiVapWdsBroadcast_Type()
)
flWlanWifiVapWdsBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapWdsBroadcast.setStatus("current")


class _FlWlanWifiVapWdsAgingTime_Type(Integer32):
    """Custom type flWlanWifiVapWdsAgingTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967),
    )


_FlWlanWifiVapWdsAgingTime_Type.__name__ = "Integer32"
_FlWlanWifiVapWdsAgingTime_Object = MibTableColumn
flWlanWifiVapWdsAgingTime = _FlWlanWifiVapWdsAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 6),
    _FlWlanWifiVapWdsAgingTime_Type()
)
flWlanWifiVapWdsAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapWdsAgingTime.setStatus("current")


class _FlWlanWifiVapEnableState_Type(Integer32):
    """Custom type flWlanWifiVapEnableState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanWifiVapEnableState_Type.__name__ = "Integer32"
_FlWlanWifiVapEnableState_Object = MibTableColumn
flWlanWifiVapEnableState = _FlWlanWifiVapEnableState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 7),
    _FlWlanWifiVapEnableState_Type()
)
flWlanWifiVapEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapEnableState.setStatus("current")
_FlWlanWifiVapChScanlist_Type = DisplayString
_FlWlanWifiVapChScanlist_Object = MibTableColumn
flWlanWifiVapChScanlist = _FlWlanWifiVapChScanlist_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 8),
    _FlWlanWifiVapChScanlist_Type()
)
flWlanWifiVapChScanlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapChScanlist.setStatus("current")


class _FlWlanWifiVapMaxNumClients_Type(Integer32):
    """Custom type flWlanWifiVapMaxNumClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_FlWlanWifiVapMaxNumClients_Type.__name__ = "Integer32"
_FlWlanWifiVapMaxNumClients_Object = MibTableColumn
flWlanWifiVapMaxNumClients = _FlWlanWifiVapMaxNumClients_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 9),
    _FlWlanWifiVapMaxNumClients_Type()
)
flWlanWifiVapMaxNumClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapMaxNumClients.setStatus("current")


class _FlWlanWifiVapStartScanning_Type(Integer32):
    """Custom type flWlanWifiVapStartScanning based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanWifiVapStartScanning_Type.__name__ = "Integer32"
_FlWlanWifiVapStartScanning_Object = MibTableColumn
flWlanWifiVapStartScanning = _FlWlanWifiVapStartScanning_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 10),
    _FlWlanWifiVapStartScanning_Type()
)
flWlanWifiVapStartScanning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapStartScanning.setStatus("current")
_FlWlanWifiVapNetworkId_Type = Integer32
_FlWlanWifiVapNetworkId_Object = MibTableColumn
flWlanWifiVapNetworkId = _FlWlanWifiVapNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 11),
    _FlWlanWifiVapNetworkId_Type()
)
flWlanWifiVapNetworkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapNetworkId.setStatus("current")
_FlWlanWifiVapManRoaming_Type = DisplayString
_FlWlanWifiVapManRoaming_Object = MibTableColumn
flWlanWifiVapManRoaming = _FlWlanWifiVapManRoaming_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 12),
    _FlWlanWifiVapManRoaming_Type()
)
flWlanWifiVapManRoaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapManRoaming.setStatus("current")


class _FlWlanWifiVapBgScanIdle_Type(Integer32):
    """Custom type flWlanWifiVapBgScanIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_FlWlanWifiVapBgScanIdle_Type.__name__ = "Integer32"
_FlWlanWifiVapBgScanIdle_Object = MibTableColumn
flWlanWifiVapBgScanIdle = _FlWlanWifiVapBgScanIdle_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 13),
    _FlWlanWifiVapBgScanIdle_Type()
)
flWlanWifiVapBgScanIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapBgScanIdle.setStatus("current")


class _FlWlanWifiVapRssiThrshForceScan_Type(Integer32):
    """Custom type flWlanWifiVapRssiThrshForceScan based on Integer32"""
    defaultValue = -90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-94, -1),
    )


_FlWlanWifiVapRssiThrshForceScan_Type.__name__ = "Integer32"
_FlWlanWifiVapRssiThrshForceScan_Object = MibTableColumn
flWlanWifiVapRssiThrshForceScan = _FlWlanWifiVapRssiThrshForceScan_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 14),
    _FlWlanWifiVapRssiThrshForceScan_Type()
)
flWlanWifiVapRssiThrshForceScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapRssiThrshForceScan.setStatus("current")


class _FlWlanWifiVapRssiChangeRoam_Type(Integer32):
    """Custom type flWlanWifiVapRssiChangeRoam based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 94),
    )


_FlWlanWifiVapRssiChangeRoam_Type.__name__ = "Integer32"
_FlWlanWifiVapRssiChangeRoam_Object = MibTableColumn
flWlanWifiVapRssiChangeRoam = _FlWlanWifiVapRssiChangeRoam_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 15),
    _FlWlanWifiVapRssiChangeRoam_Type()
)
flWlanWifiVapRssiChangeRoam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapRssiChangeRoam.setStatus("current")


class _FlWlanWifiVapRssiChangeBgScan_Type(Integer32):
    """Custom type flWlanWifiVapRssiChangeBgScan based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 94),
    )


_FlWlanWifiVapRssiChangeBgScan_Type.__name__ = "Integer32"
_FlWlanWifiVapRssiChangeBgScan_Object = MibTableColumn
flWlanWifiVapRssiChangeBgScan = _FlWlanWifiVapRssiChangeBgScan_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 16),
    _FlWlanWifiVapRssiChangeBgScan_Type()
)
flWlanWifiVapRssiChangeBgScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapRssiChangeBgScan.setStatus("current")


class _FlWlanWifiVapRssiThrshBgScan_Type(Integer32):
    """Custom type flWlanWifiVapRssiThrshBgScan based on Integer32"""
    defaultValue = -60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-94, -1),
    )


_FlWlanWifiVapRssiThrshBgScan_Type.__name__ = "Integer32"
_FlWlanWifiVapRssiThrshBgScan_Object = MibTableColumn
flWlanWifiVapRssiThrshBgScan = _FlWlanWifiVapRssiThrshBgScan_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 17),
    _FlWlanWifiVapRssiThrshBgScan_Type()
)
flWlanWifiVapRssiThrshBgScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapRssiThrshBgScan.setStatus("current")
_FlWlanWifiVapScbManMac_Type = DisplayString
_FlWlanWifiVapScbManMac_Object = MibTableColumn
flWlanWifiVapScbManMac = _FlWlanWifiVapScbManMac_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 18),
    _FlWlanWifiVapScbManMac_Type()
)
flWlanWifiVapScbManMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapScbManMac.setStatus("current")


class _FlWlanWifiVapScbMode_Type(Integer32):
    """Custom type flWlanWifiVapScbMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_FlWlanWifiVapScbMode_Type.__name__ = "Integer32"
_FlWlanWifiVapScbMode_Object = MibTableColumn
flWlanWifiVapScbMode = _FlWlanWifiVapScbMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 19),
    _FlWlanWifiVapScbMode_Type()
)
flWlanWifiVapScbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapScbMode.setStatus("current")


class _FlWlanWifiVapFragThreshold_Type(Integer32):
    """Custom type flWlanWifiVapFragThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FlWlanWifiVapFragThreshold_Type.__name__ = "Integer32"
_FlWlanWifiVapFragThreshold_Object = MibTableColumn
flWlanWifiVapFragThreshold = _FlWlanWifiVapFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 20),
    _FlWlanWifiVapFragThreshold_Type()
)
flWlanWifiVapFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapFragThreshold.setStatus("current")


class _FlWlanWifiVapTxPowerRadiated_Type(Integer32):
    """Custom type flWlanWifiVapTxPowerRadiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_FlWlanWifiVapTxPowerRadiated_Type.__name__ = "Integer32"
_FlWlanWifiVapTxPowerRadiated_Object = MibTableColumn
flWlanWifiVapTxPowerRadiated = _FlWlanWifiVapTxPowerRadiated_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 21),
    _FlWlanWifiVapTxPowerRadiated_Type()
)
flWlanWifiVapTxPowerRadiated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapTxPowerRadiated.setStatus("current")
_FlWlanWifiVapCurrentTxPowerRadiated_Type = Integer32
_FlWlanWifiVapCurrentTxPowerRadiated_Object = MibTableColumn
flWlanWifiVapCurrentTxPowerRadiated = _FlWlanWifiVapCurrentTxPowerRadiated_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 22),
    _FlWlanWifiVapCurrentTxPowerRadiated_Type()
)
flWlanWifiVapCurrentTxPowerRadiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiVapCurrentTxPowerRadiated.setStatus("current")


class _FlWlanWifiVapChBandwidth_Type(Integer32):
    """Custom type flWlanWifiVapChBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f20MHz", 1),
          ("f40MHz", 2))
    )


_FlWlanWifiVapChBandwidth_Type.__name__ = "Integer32"
_FlWlanWifiVapChBandwidth_Object = MibTableColumn
flWlanWifiVapChBandwidth = _FlWlanWifiVapChBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 23),
    _FlWlanWifiVapChBandwidth_Type()
)
flWlanWifiVapChBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapChBandwidth.setStatus("current")


class _FlWlanWifiVapWlanCh_Type(Integer32):
    """Custom type flWlanWifiVapWlanCh based on Integer32"""
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
              14,
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("channel-1", 1),
          ("channel-2", 2),
          ("channel-3", 3),
          ("channel-4", 4),
          ("channel-5", 5),
          ("channel-6", 6),
          ("channel-7", 7),
          ("channel-8", 8),
          ("channel-9", 9),
          ("channel-10", 10),
          ("channel-11", 11),
          ("channel-12", 12),
          ("channel-13", 13),
          ("channel-14", 14),
          ("channel-36", 36),
          ("channel-40", 40),
          ("channel-44", 44),
          ("channel-48", 48),
          ("channel-52", 52),
          ("channel-56", 56),
          ("channel-60", 60),
          ("channel-64", 64),
          ("channel-132", 132),
          ("channel-136", 136),
          ("channel-140", 140),
          ("channel-149", 149),
          ("channel-153", 153),
          ("channel-157", 157),
          ("channel-161", 161),
          ("channel-165", 165),
          ("indoor8-auto", 200),
          ("indoor16-auto", 201),
          ("outdoor", 202),
          ("auto", 203))
    )


_FlWlanWifiVapWlanCh_Type.__name__ = "Integer32"
_FlWlanWifiVapWlanCh_Object = MibTableColumn
flWlanWifiVapWlanCh = _FlWlanWifiVapWlanCh_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 24),
    _FlWlanWifiVapWlanCh_Type()
)
flWlanWifiVapWlanCh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapWlanCh.setStatus("current")


class _FlWlanWifiVap80211Mode_Type(Integer32):
    """Custom type flWlanWifiVap80211Mode based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("bg", 3),
          ("an", 4),
          ("gn", 5))
    )


_FlWlanWifiVap80211Mode_Type.__name__ = "Integer32"
_FlWlanWifiVap80211Mode_Object = MibTableColumn
flWlanWifiVap80211Mode = _FlWlanWifiVap80211Mode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 25),
    _FlWlanWifiVap80211Mode_Type()
)
flWlanWifiVap80211Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVap80211Mode.setStatus("current")
_FlWlanWifiVapHwID_Type = Integer32
_FlWlanWifiVapHwID_Object = MibTableColumn
flWlanWifiVapHwID = _FlWlanWifiVapHwID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 26),
    _FlWlanWifiVapHwID_Type()
)
flWlanWifiVapHwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiVapHwID.setStatus("current")


class _FlWlanWifiVapOpMode_Type(Integer32):
    """Custom type flWlanWifiVapOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("scb", 2),
          ("mcb", 3),
          ("ftb", 4),
          ("monitor", 5),
          ("mesh", 6),
          ("natc", 8))
    )


_FlWlanWifiVapOpMode_Type.__name__ = "Integer32"
_FlWlanWifiVapOpMode_Object = MibTableColumn
flWlanWifiVapOpMode = _FlWlanWifiVapOpMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 27),
    _FlWlanWifiVapOpMode_Type()
)
flWlanWifiVapOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapOpMode.setStatus("current")


class _FlWlanWifiVapStatus_Type(Integer32):
    """Custom type flWlanWifiVapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("scanning", 1))
    )


_FlWlanWifiVapStatus_Type.__name__ = "Integer32"
_FlWlanWifiVapStatus_Object = MibTableColumn
flWlanWifiVapStatus = _FlWlanWifiVapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 28),
    _FlWlanWifiVapStatus_Type()
)
flWlanWifiVapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiVapStatus.setStatus("current")


class _FlWlanWifiVapActiveProfile_Type(Integer32):
    """Custom type flWlanWifiVapActiveProfile based on Integer32"""
    defaultValue = 1


_FlWlanWifiVapActiveProfile_Type.__name__ = "Integer32"
_FlWlanWifiVapActiveProfile_Object = MibTableColumn
flWlanWifiVapActiveProfile = _FlWlanWifiVapActiveProfile_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 29),
    _FlWlanWifiVapActiveProfile_Type()
)
flWlanWifiVapActiveProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiVapActiveProfile.setStatus("current")
_FlWlanWifiVapRowStatus_Type = RowStatus
_FlWlanWifiVapRowStatus_Object = MibTableColumn
flWlanWifiVapRowStatus = _FlWlanWifiVapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 1, 1, 30),
    _FlWlanWifiVapRowStatus_Type()
)
flWlanWifiVapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flWlanWifiVapRowStatus.setStatus("current")
_FlWlanWifiVapProfileTable_Object = MibTable
flWlanWifiVapProfileTable = _FlWlanWifiVapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2)
)
if mibBuilder.loadTexts:
    flWlanWifiVapProfileTable.setStatus("current")
_FlWlanWifiVapProfileEntry_Object = MibTableRow
flWlanWifiVapProfileEntry = _FlWlanWifiVapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1)
)
flWlanWifiVapProfileEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWlanWifiVapProfileVapID"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWlanWifiVapProfileID"),
)
if mibBuilder.loadTexts:
    flWlanWifiVapProfileEntry.setStatus("current")


class _FlWlanWifiVapProfileVapID_Type(Integer32):
    """Custom type flWlanWifiVapProfileVapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWlanWifiVapProfileVapID_Type.__name__ = "Integer32"
_FlWlanWifiVapProfileVapID_Object = MibTableColumn
flWlanWifiVapProfileVapID = _FlWlanWifiVapProfileVapID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 1),
    _FlWlanWifiVapProfileVapID_Type()
)
flWlanWifiVapProfileVapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileVapID.setStatus("current")


class _FlWlanWifiVapProfileID_Type(Integer32):
    """Custom type flWlanWifiVapProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWlanWifiVapProfileID_Type.__name__ = "Integer32"
_FlWlanWifiVapProfileID_Object = MibTableColumn
flWlanWifiVapProfileID = _FlWlanWifiVapProfileID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 2),
    _FlWlanWifiVapProfileID_Type()
)
flWlanWifiVapProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileID.setStatus("current")


class _FlWlanWifiVapProfileEapClientcertPsKey_Type(OctetString):
    """Custom type flWlanWifiVapProfileEapClientcertPsKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 128),
    )


_FlWlanWifiVapProfileEapClientcertPsKey_Type.__name__ = "OctetString"
_FlWlanWifiVapProfileEapClientcertPsKey_Object = MibTableColumn
flWlanWifiVapProfileEapClientcertPsKey = _FlWlanWifiVapProfileEapClientcertPsKey_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 3),
    _FlWlanWifiVapProfileEapClientcertPsKey_Type()
)
flWlanWifiVapProfileEapClientcertPsKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileEapClientcertPsKey.setStatus("current")


class _FlWlanWifiVapProfileEapUserPw_Type(OctetString):
    """Custom type flWlanWifiVapProfileEapUserPw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 128),
    )


_FlWlanWifiVapProfileEapUserPw_Type.__name__ = "OctetString"
_FlWlanWifiVapProfileEapUserPw_Object = MibTableColumn
flWlanWifiVapProfileEapUserPw = _FlWlanWifiVapProfileEapUserPw_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 4),
    _FlWlanWifiVapProfileEapUserPw_Type()
)
flWlanWifiVapProfileEapUserPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileEapUserPw.setStatus("current")
_FlWlanWifiVapProfileEapIdentity_Type = DisplayString
_FlWlanWifiVapProfileEapIdentity_Object = MibTableColumn
flWlanWifiVapProfileEapIdentity = _FlWlanWifiVapProfileEapIdentity_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 5),
    _FlWlanWifiVapProfileEapIdentity_Type()
)
flWlanWifiVapProfileEapIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileEapIdentity.setStatus("current")


class _FlWlanWifiVapProfileEapPhase2Auth_Type(Integer32):
    """Custom type flWlanWifiVapProfileEapPhase2Auth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mschapv2", 1),
          ("md5", 2))
    )


_FlWlanWifiVapProfileEapPhase2Auth_Type.__name__ = "Integer32"
_FlWlanWifiVapProfileEapPhase2Auth_Object = MibTableColumn
flWlanWifiVapProfileEapPhase2Auth = _FlWlanWifiVapProfileEapPhase2Auth_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 6),
    _FlWlanWifiVapProfileEapPhase2Auth_Type()
)
flWlanWifiVapProfileEapPhase2Auth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileEapPhase2Auth.setStatus("current")


class _FlWlanWifiVapProfileEapPairwiseMode_Type(Integer32):
    """Custom type flWlanWifiVapProfileEapPairwiseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("tkip", 2))
    )


_FlWlanWifiVapProfileEapPairwiseMode_Type.__name__ = "Integer32"
_FlWlanWifiVapProfileEapPairwiseMode_Object = MibTableColumn
flWlanWifiVapProfileEapPairwiseMode = _FlWlanWifiVapProfileEapPairwiseMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 7),
    _FlWlanWifiVapProfileEapPairwiseMode_Type()
)
flWlanWifiVapProfileEapPairwiseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileEapPairwiseMode.setStatus("current")


class _FlWlanWifiVapProfileEapMode_Type(Integer32):
    """Custom type flWlanWifiVapProfileEapMode based on Integer32"""
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
        *(("disable", 0),
          ("peap", 1),
          ("ttls", 2),
          ("tls", 3))
    )


_FlWlanWifiVapProfileEapMode_Type.__name__ = "Integer32"
_FlWlanWifiVapProfileEapMode_Object = MibTableColumn
flWlanWifiVapProfileEapMode = _FlWlanWifiVapProfileEapMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 8),
    _FlWlanWifiVapProfileEapMode_Type()
)
flWlanWifiVapProfileEapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileEapMode.setStatus("current")


class _FlWlanWifiVapProfilePsKey_Type(OctetString):
    """Custom type flWlanWifiVapProfilePsKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 128),
    )


_FlWlanWifiVapProfilePsKey_Type.__name__ = "OctetString"
_FlWlanWifiVapProfilePsKey_Object = MibTableColumn
flWlanWifiVapProfilePsKey = _FlWlanWifiVapProfilePsKey_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 9),
    _FlWlanWifiVapProfilePsKey_Type()
)
flWlanWifiVapProfilePsKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfilePsKey.setStatus("current")


class _FlWlanWifiVapProfileEnc_Type(Integer32):
    """Custom type flWlanWifiVapProfileEnc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("tkip-aes", 3))
    )


_FlWlanWifiVapProfileEnc_Type.__name__ = "Integer32"
_FlWlanWifiVapProfileEnc_Object = MibTableColumn
flWlanWifiVapProfileEnc = _FlWlanWifiVapProfileEnc_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 10),
    _FlWlanWifiVapProfileEnc_Type()
)
flWlanWifiVapProfileEnc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileEnc.setStatus("current")


class _FlWlanWifiVapProfileAuth_Type(Integer32):
    """Custom type flWlanWifiVapProfileAuth based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wpa-psk", 1),
          ("wep64", 2),
          ("wep128", 3),
          ("wpa2-psk", 4),
          ("wpa2-eap", 5),
          ("wpa-wpa2-psk", 6),
          ("ft-psk", 7),
          ("ft-eap", 8))
    )


_FlWlanWifiVapProfileAuth_Type.__name__ = "Integer32"
_FlWlanWifiVapProfileAuth_Object = MibTableColumn
flWlanWifiVapProfileAuth = _FlWlanWifiVapProfileAuth_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 11),
    _FlWlanWifiVapProfileAuth_Type()
)
flWlanWifiVapProfileAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileAuth.setStatus("current")
_FlWlanWifiVapProfileSsid_Type = DisplayString
_FlWlanWifiVapProfileSsid_Object = MibTableColumn
flWlanWifiVapProfileSsid = _FlWlanWifiVapProfileSsid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 2, 1, 12),
    _FlWlanWifiVapProfileSsid_Type()
)
flWlanWifiVapProfileSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanWifiVapProfileSsid.setStatus("current")
_FlWlanWifiScanResultsTable_Object = MibTable
flWlanWifiScanResultsTable = _FlWlanWifiScanResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3)
)
if mibBuilder.loadTexts:
    flWlanWifiScanResultsTable.setStatus("current")
_FlWlanWifiScanResultsEntry_Object = MibTableRow
flWlanWifiScanResultsEntry = _FlWlanWifiScanResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1)
)
flWlanWifiScanResultsEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWlanWifiScanResultsVapID"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWlanWifiScanResultsID"),
)
if mibBuilder.loadTexts:
    flWlanWifiScanResultsEntry.setStatus("current")


class _FlWlanWifiScanResultsVapID_Type(Integer32):
    """Custom type flWlanWifiScanResultsVapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWlanWifiScanResultsVapID_Type.__name__ = "Integer32"
_FlWlanWifiScanResultsVapID_Object = MibTableColumn
flWlanWifiScanResultsVapID = _FlWlanWifiScanResultsVapID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1, 1),
    _FlWlanWifiScanResultsVapID_Type()
)
flWlanWifiScanResultsVapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiScanResultsVapID.setStatus("current")


class _FlWlanWifiScanResultsID_Type(Integer32):
    """Custom type flWlanWifiScanResultsID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWlanWifiScanResultsID_Type.__name__ = "Integer32"
_FlWlanWifiScanResultsID_Object = MibTableColumn
flWlanWifiScanResultsID = _FlWlanWifiScanResultsID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1, 2),
    _FlWlanWifiScanResultsID_Type()
)
flWlanWifiScanResultsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiScanResultsID.setStatus("current")
_FlWlanWifiScanResultsEssid_Type = DisplayString
_FlWlanWifiScanResultsEssid_Object = MibTableColumn
flWlanWifiScanResultsEssid = _FlWlanWifiScanResultsEssid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1, 3),
    _FlWlanWifiScanResultsEssid_Type()
)
flWlanWifiScanResultsEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiScanResultsEssid.setStatus("current")
_FlWlanWifiScanResultsBssid_Type = DisplayString
_FlWlanWifiScanResultsBssid_Object = MibTableColumn
flWlanWifiScanResultsBssid = _FlWlanWifiScanResultsBssid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1, 4),
    _FlWlanWifiScanResultsBssid_Type()
)
flWlanWifiScanResultsBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiScanResultsBssid.setStatus("current")
_FlWlanWifiScanResultsCh_Type = Integer32
_FlWlanWifiScanResultsCh_Object = MibTableColumn
flWlanWifiScanResultsCh = _FlWlanWifiScanResultsCh_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1, 5),
    _FlWlanWifiScanResultsCh_Type()
)
flWlanWifiScanResultsCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiScanResultsCh.setStatus("current")
_FlWlanWifiScanResultsSignal_Type = Integer32
_FlWlanWifiScanResultsSignal_Object = MibTableColumn
flWlanWifiScanResultsSignal = _FlWlanWifiScanResultsSignal_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1, 6),
    _FlWlanWifiScanResultsSignal_Type()
)
flWlanWifiScanResultsSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiScanResultsSignal.setStatus("current")
_FlWlanWifiScanResultsSecurity_Type = DisplayString
_FlWlanWifiScanResultsSecurity_Object = MibTableColumn
flWlanWifiScanResultsSecurity = _FlWlanWifiScanResultsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1, 7),
    _FlWlanWifiScanResultsSecurity_Type()
)
flWlanWifiScanResultsSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiScanResultsSecurity.setStatus("current")


class _FlWlanWifiScanResultsEnc_Type(Integer32):
    """Custom type flWlanWifiScanResultsEnc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tkip", 1),
          ("aes", 2))
    )


_FlWlanWifiScanResultsEnc_Type.__name__ = "Integer32"
_FlWlanWifiScanResultsEnc_Object = MibTableColumn
flWlanWifiScanResultsEnc = _FlWlanWifiScanResultsEnc_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1, 8),
    _FlWlanWifiScanResultsEnc_Type()
)
flWlanWifiScanResultsEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiScanResultsEnc.setStatus("current")
_FlWlanWifiScanResultsMode_Type = DisplayString
_FlWlanWifiScanResultsMode_Object = MibTableColumn
flWlanWifiScanResultsMode = _FlWlanWifiScanResultsMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 3, 1, 9),
    _FlWlanWifiScanResultsMode_Type()
)
flWlanWifiScanResultsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiScanResultsMode.setStatus("current")
_FlWlanWifiConnectionTable_Object = MibTable
flWlanWifiConnectionTable = _FlWlanWifiConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4)
)
if mibBuilder.loadTexts:
    flWlanWifiConnectionTable.setStatus("current")
_FlWlanWifiConnectionEntry_Object = MibTableRow
flWlanWifiConnectionEntry = _FlWlanWifiConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1)
)
flWlanWifiConnectionEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWlanWifiConnectionVapID"),
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWlanWifiConnectionID"),
)
if mibBuilder.loadTexts:
    flWlanWifiConnectionEntry.setStatus("current")


class _FlWlanWifiConnectionVapID_Type(Integer32):
    """Custom type flWlanWifiConnectionVapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWlanWifiConnectionVapID_Type.__name__ = "Integer32"
_FlWlanWifiConnectionVapID_Object = MibTableColumn
flWlanWifiConnectionVapID = _FlWlanWifiConnectionVapID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1, 1),
    _FlWlanWifiConnectionVapID_Type()
)
flWlanWifiConnectionVapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiConnectionVapID.setStatus("current")


class _FlWlanWifiConnectionID_Type(Integer32):
    """Custom type flWlanWifiConnectionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWlanWifiConnectionID_Type.__name__ = "Integer32"
_FlWlanWifiConnectionID_Object = MibTableColumn
flWlanWifiConnectionID = _FlWlanWifiConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1, 2),
    _FlWlanWifiConnectionID_Type()
)
flWlanWifiConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiConnectionID.setStatus("current")


class _FlWlanWifiConnectionOpMode_Type(Integer32):
    """Custom type flWlanWifiConnectionOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("scb", 2),
          ("mcb", 3),
          ("ftb", 4),
          ("monitor", 5),
          ("mesh", 6),
          ("natc", 8))
    )


_FlWlanWifiConnectionOpMode_Type.__name__ = "Integer32"
_FlWlanWifiConnectionOpMode_Object = MibTableColumn
flWlanWifiConnectionOpMode = _FlWlanWifiConnectionOpMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1, 3),
    _FlWlanWifiConnectionOpMode_Type()
)
flWlanWifiConnectionOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiConnectionOpMode.setStatus("current")
_FlWlanWifiConnectionSsid_Type = DisplayString
_FlWlanWifiConnectionSsid_Object = MibTableColumn
flWlanWifiConnectionSsid = _FlWlanWifiConnectionSsid_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1, 4),
    _FlWlanWifiConnectionSsid_Type()
)
flWlanWifiConnectionSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiConnectionSsid.setStatus("current")
_FlWlanWifiConnectionMac_Type = DisplayString
_FlWlanWifiConnectionMac_Object = MibTableColumn
flWlanWifiConnectionMac = _FlWlanWifiConnectionMac_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1, 5),
    _FlWlanWifiConnectionMac_Type()
)
flWlanWifiConnectionMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiConnectionMac.setStatus("current")
_FlWlanWifiConnectionRssi_Type = Integer32
_FlWlanWifiConnectionRssi_Object = MibTableColumn
flWlanWifiConnectionRssi = _FlWlanWifiConnectionRssi_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1, 6),
    _FlWlanWifiConnectionRssi_Type()
)
flWlanWifiConnectionRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiConnectionRssi.setStatus("current")
_FlWlanWifiConnectionBitRate_Type = Integer32
_FlWlanWifiConnectionBitRate_Object = MibTableColumn
flWlanWifiConnectionBitRate = _FlWlanWifiConnectionBitRate_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1, 7),
    _FlWlanWifiConnectionBitRate_Type()
)
flWlanWifiConnectionBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiConnectionBitRate.setStatus("current")
_FlWlanWifiConnectionFreq_Type = DisplayString
_FlWlanWifiConnectionFreq_Object = MibTableColumn
flWlanWifiConnectionFreq = _FlWlanWifiConnectionFreq_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1, 8),
    _FlWlanWifiConnectionFreq_Type()
)
flWlanWifiConnectionFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiConnectionFreq.setStatus("current")


class _FlWlanWifiConnectionCh_Type(Integer32):
    """Custom type flWlanWifiConnectionCh based on Integer32"""
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
              14,
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("channel-1", 1),
          ("channel-2", 2),
          ("channel-3", 3),
          ("channel-4", 4),
          ("channel-5", 5),
          ("channel-6", 6),
          ("channel-7", 7),
          ("channel-8", 8),
          ("channel-9", 9),
          ("channel-10", 10),
          ("channel-11", 11),
          ("channel-12", 12),
          ("channel-13", 13),
          ("channel-14", 14),
          ("channel-36", 36),
          ("channel-40", 40),
          ("channel-44", 44),
          ("channel-48", 48),
          ("channel-52", 52),
          ("channel-56", 56),
          ("channel-60", 60),
          ("channel-64", 64),
          ("channel-132", 132),
          ("channel-136", 136),
          ("channel-140", 140),
          ("channel-149", 149),
          ("channel-153", 153),
          ("channel-157", 157),
          ("channel-161", 161),
          ("channel-165", 165),
          ("indoor8-auto", 200),
          ("indoor16-auto", 201),
          ("outdoor", 202),
          ("auto", 203))
    )


_FlWlanWifiConnectionCh_Type.__name__ = "Integer32"
_FlWlanWifiConnectionCh_Object = MibTableColumn
flWlanWifiConnectionCh = _FlWlanWifiConnectionCh_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 2, 4, 1, 9),
    _FlWlanWifiConnectionCh_Type()
)
flWlanWifiConnectionCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanWifiConnectionCh.setStatus("current")


class _FlWlanApplySettings_Type(Integer32):
    """Custom type flWlanApplySettings based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanApplySettings_Type.__name__ = "Integer32"
_FlWlanApplySettings_Object = MibScalar
flWlanApplySettings = _FlWlanApplySettings_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 3),
    _FlWlanApplySettings_Type()
)
flWlanApplySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanApplySettings.setStatus("current")


class _FlWlanSettingsApplyState_Type(Integer32):
    """Custom type flWlanSettingsApplyState based on Integer32"""
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
        *(("ok", 0),
          ("newSettingsNeedToBeApplied", 1),
          ("inProgress", 2),
          ("error", 3))
    )


_FlWlanSettingsApplyState_Type.__name__ = "Integer32"
_FlWlanSettingsApplyState_Object = MibScalar
flWlanSettingsApplyState = _FlWlanSettingsApplyState_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 4),
    _FlWlanSettingsApplyState_Type()
)
flWlanSettingsApplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanSettingsApplyState.setStatus("current")


class _FlWlanManagementAccess_Type(Integer32):
    """Custom type flWlanManagementAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanManagementAccess_Type.__name__ = "Integer32"
_FlWlanManagementAccess_Object = MibScalar
flWlanManagementAccess = _FlWlanManagementAccess_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 5),
    _FlWlanManagementAccess_Type()
)
flWlanManagementAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanManagementAccess.setStatus("current")


class _FlWlanPtcpLldpFilter_Type(Integer32):
    """Custom type flWlanPtcpLldpFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanPtcpLldpFilter_Type.__name__ = "Integer32"
_FlWlanPtcpLldpFilter_Object = MibScalar
flWlanPtcpLldpFilter = _FlWlanPtcpLldpFilter_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 6),
    _FlWlanPtcpLldpFilter_Type()
)
flWlanPtcpLldpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanPtcpLldpFilter.setStatus("current")
_FlWlanCountry_Type = DisplayString
_FlWlanCountry_Object = MibScalar
flWlanCountry = _FlWlanCountry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 7),
    _FlWlanCountry_Type()
)
flWlanCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanCountry.setStatus("current")
_FlWlanCountryTable_Object = MibTable
flWlanCountryTable = _FlWlanCountryTable_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 8)
)
if mibBuilder.loadTexts:
    flWlanCountryTable.setStatus("current")
_FlWlanCountryEntry_Object = MibTableRow
flWlanCountryEntry = _FlWlanCountryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 8, 1)
)
flWlanCountryEntry.setIndexNames(
    (0, "FL-MGD-INFRASTRUCT-MIB", "flWlanCountryID"),
)
if mibBuilder.loadTexts:
    flWlanCountryEntry.setStatus("current")


class _FlWlanCountryID_Type(Integer32):
    """Custom type flWlanCountryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlWlanCountryID_Type.__name__ = "Integer32"
_FlWlanCountryID_Object = MibTableColumn
flWlanCountryID = _FlWlanCountryID_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 8, 1, 1),
    _FlWlanCountryID_Type()
)
flWlanCountryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanCountryID.setStatus("current")
_FlWlanCountryName_Type = DisplayString
_FlWlanCountryName_Object = MibTableColumn
flWlanCountryName = _FlWlanCountryName_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 8, 1, 2),
    _FlWlanCountryName_Type()
)
flWlanCountryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flWlanCountryName.setStatus("current")


class _FlWlanOutdoorMode_Type(Integer32):
    """Custom type flWlanOutdoorMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanOutdoorMode_Type.__name__ = "Integer32"
_FlWlanOutdoorMode_Object = MibScalar
flWlanOutdoorMode = _FlWlanOutdoorMode_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 9),
    _FlWlanOutdoorMode_Type()
)
flWlanOutdoorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanOutdoorMode.setStatus("current")


class _FlWlanGlobalActivation_Type(Integer32):
    """Custom type flWlanGlobalActivation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanGlobalActivation_Type.__name__ = "Integer32"
_FlWlanGlobalActivation_Object = MibScalar
flWlanGlobalActivation = _FlWlanGlobalActivation_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 10),
    _FlWlanGlobalActivation_Type()
)
flWlanGlobalActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanGlobalActivation.setStatus("current")


class _FlWlanCyclicRssiTracking_Type(Integer32):
    """Custom type flWlanCyclicRssiTracking based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlWlanCyclicRssiTracking_Type.__name__ = "Integer32"
_FlWlanCyclicRssiTracking_Object = MibScalar
flWlanCyclicRssiTracking = _FlWlanCyclicRssiTracking_Object(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 27, 11),
    _FlWlanCyclicRssiTracking_Type()
)
flWlanCyclicRssiTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flWlanCyclicRssiTracking.setStatus("current")
dot1qStaticMulticastEntry.registerAugmentions(
    ("FL-MGD-INFRASTRUCT-MIB",
     "flSwitchIgmpSnoopEntry")
)
flSwitchIgmpSnoopEntry.setIndexNames(*dot1qStaticMulticastEntry.getIndexNames())
rip2IfConfEntry.registerAugmentions(
    ("FL-MGD-INFRASTRUCT-MIB",
     "flWorkRoutingRip2IfConfEntry")
)
flWorkRoutingRip2IfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("FL-MGD-INFRASTRUCT-MIB",
     "flWorkRoutingOspfIfEntry")
)
flWorkRoutingOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("FL-MGD-INFRASTRUCT-MIB",
     "flWorkRoutingOspfVirtIfEntry")
)
flWorkRoutingOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects

trapPasswdAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 1)
)
trapPasswdAccess.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlPasswdSuccess")
)
if mibBuilder.loadTexts:
    trapPasswdAccess.setStatus(
        "current"
    )

trapFWHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 2)
)
trapFWHealth.setObjects(
      *(("FL-MGD-INFRASTRUCT-MIB", "flWorkFWInfoOperStatus"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWInfoHealthText"))
)
if mibBuilder.loadTexts:
    trapFWHealth.setStatus(
        "current"
    )

trapFWConf = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 3)
)
trapFWConf.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlConfStatus")
)
if mibBuilder.loadTexts:
    trapFWConf.setStatus(
        "current"
    )

trapPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 4)
)
trapPowerSupply.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkBasicPowerStat")
)
if mibBuilder.loadTexts:
    trapPowerSupply.setStatus(
        "current"
    )

trapSecurityPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 5)
)
trapSecurityPort.setObjects(
      *(("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlSecurityPortIndex"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlSecurityPortLastMacAddr"))
)
if mibBuilder.loadTexts:
    trapSecurityPort.setStatus(
        "current"
    )

trapRstpRingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 6)
)
trapRstpRingFailure.setObjects(
      *(("FL-MGD-INFRASTRUCT-MIB", "flSwitchRSTPRingRootPort"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkNetIfParamPhyAddress"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkNetIfParamIpAddress"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkBasicName"))
)
if mibBuilder.loadTexts:
    trapRstpRingFailure.setStatus(
        "current"
    )

trapPofScrjPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 7)
)
trapPofScrjPort.setObjects(
      *(("FL-MGD-INFRASTRUCT-MIB", "flWorkNetPortPofScrjIfIndex"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkNetPortPofScrjIfStatus"))
)
if mibBuilder.loadTexts:
    trapPofScrjPort.setStatus(
        "current"
    )

trapPoEPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 8)
)
trapPoEPort.setObjects(
      *(("FL-MGD-INFRASTRUCT-MIB", "flWorkNetPortPoEIndex"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkNetPortPoEFaultStatus"))
)
if mibBuilder.loadTexts:
    trapPoEPort.setStatus(
        "current"
    )

trapMrpStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 9)
)
trapMrpStatusChange.setObjects(
      *(("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlMRPInfoDomainIdx"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlMRPInfoDomainName"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlMRPInfoDomainState"))
)
if mibBuilder.loadTexts:
    trapMrpStatusChange.setStatus(
        "current"
    )

trapTemperatureManagement = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 10)
)
if mibBuilder.loadTexts:
    trapTemperatureManagement.setStatus(
        "current"
    )

trapDigitalInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 11)
)
trapDigitalInput.setObjects(
      *(("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDigitalInputIndex"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDigitalInputStatus"))
)
if mibBuilder.loadTexts:
    trapDigitalInput.setStatus(
        "current"
    )

trapSDcardPluggedin = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 12)
)
trapSDcardPluggedin.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlConfPluggableStatus")
)
if mibBuilder.loadTexts:
    trapSDcardPluggedin.setStatus(
        "current"
    )

trapSDcardPluggedout = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 13)
)
if mibBuilder.loadTexts:
    trapSDcardPluggedout.setStatus(
        "current"
    )

trapConfSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 16)
)
trapConfSaved.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlConfStatus")
)
if mibBuilder.loadTexts:
    trapConfSaved.setStatus(
        "current"
    )

trapIPconflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 18)
)
trapIPconflict.setObjects(
      *(("FL-MGD-INFRASTRUCT-MIB", "flWorkNetACDStatus"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkNetACDIP"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkNetACDMAC"))
)
if mibBuilder.loadTexts:
    trapIPconflict.setStatus(
        "current"
    )

trapDLRRingChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 19)
)
trapDLRRingChange.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDLRRingStatus")
)
if mibBuilder.loadTexts:
    trapDLRRingChange.setStatus(
        "current"
    )

trapPowerSupplyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 20)
)
if mibBuilder.loadTexts:
    trapPowerSupplyLow.setStatus(
        "current"
    )

trapConfigDiff = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 21)
)
trapConfigDiff.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlConfPluggableCompareStatus")
)
if mibBuilder.loadTexts:
    trapConfigDiff.setStatus(
        "current"
    )

trapCrcOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 25)
)
trapCrcOk.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex")
)
if mibBuilder.loadTexts:
    trapCrcOk.setStatus(
        "current"
    )

trapCrcWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 26)
)
trapCrcWarning.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex")
)
if mibBuilder.loadTexts:
    trapCrcWarning.setStatus(
        "current"
    )

trapCrcCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 27)
)
trapCrcCritical.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex")
)
if mibBuilder.loadTexts:
    trapCrcCritical.setStatus(
        "current"
    )

trapCrcPeakIncreased = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 28)
)
trapCrcPeakIncreased.setObjects(
      *(("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex"),
        ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak"))
)
if mibBuilder.loadTexts:
    trapCrcPeakIncreased.setStatus(
        "current"
    )

trapEventTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 29)
)
if mibBuilder.loadTexts:
    trapEventTableOverflow.setStatus(
        "current"
    )

trapUserConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 30)
)
trapUserConfigChanged.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWInfoEventDescription")
)
if mibBuilder.loadTexts:
    trapUserConfigChanged.setStatus(
        "current"
    )

trapConfigParamChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 31)
)
trapConfigParamChanged.setObjects(
    ("FL-MGD-INFRASTRUCT-MIB", "flWorkFWInfoEventDescription")
)
if mibBuilder.loadTexts:
    trapConfigParamChanged.setStatus(
        "current"
    )

trapManagerConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 4346, 11, 11, 3, 0, 99)
)
if mibBuilder.loadTexts:
    trapManagerConnection.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FL-MGD-INFRASTRUCT-MIB",
    **{"EnabledDisabledStatus": EnabledDisabledStatus,
       "OpModeType": OpModeType,
       "EtypeValue": EtypeValue,
       "phoenixContact": phoenixContact,
       "pxcModules": pxcModules,
       "flMgdInfrastructureMibModule": flMgdInfrastructureMibModule,
       "pxcGlobal": pxcGlobal,
       "pxcBasic": pxcBasic,
       "pxcBasicName": pxcBasicName,
       "pxcBasicDescr": pxcBasicDescr,
       "pxcBasicURL": pxcBasicURL,
       "pxcFactoryLine": pxcFactoryLine,
       "flGlobal": flGlobal,
       "flBasic": flBasic,
       "flBasicName": flBasicName,
       "flBasicDescr": flBasicDescr,
       "flBasicURL": flBasicURL,
       "flBasicCompCapacity": flBasicCompCapacity,
       "flComponents": flComponents,
       "flComponentsTable": flComponentsTable,
       "flComponentsEntry": flComponentsEntry,
       "flComponentsIndex": flComponentsIndex,
       "flComponentsName": flComponentsName,
       "flComponentsDescr": flComponentsDescr,
       "flComponentsURL": flComponentsURL,
       "flComponentsOrderNumber": flComponentsOrderNumber,
       "flWorkDevice": flWorkDevice,
       "flWorkBasic": flWorkBasic,
       "flWorkBasicName": flWorkBasicName,
       "flWorkBasicDescr": flWorkBasicDescr,
       "flWorkBasicURL": flWorkBasicURL,
       "flWorkBasicSerialNumber": flWorkBasicSerialNumber,
       "flWorkBasicHWRevision": flWorkBasicHWRevision,
       "flWorkBasicPowerStat": flWorkBasicPowerStat,
       "flWorkBasicSystemBusRevision": flWorkBasicSystemBusRevision,
       "flWorkBasicCompMaxCapacity": flWorkBasicCompMaxCapacity,
       "flWorkBasicCompCapacity": flWorkBasicCompCapacity,
       "flWorkBasicLogicRevision": flWorkBasicLogicRevision,
       "flWorkBasicPlatformID": flWorkBasicPlatformID,
       "flWorkBasicFwGeneration": flWorkBasicFwGeneration,
       "flWorkBasicCfGeneration": flWorkBasicCfGeneration,
       "flWorkBasicPortTable": flWorkBasicPortTable,
       "flWorkBasicPortEntry": flWorkBasicPortEntry,
       "flWorkBasicPortIdx": flWorkBasicPortIdx,
       "flWorkBasicPortService": flWorkBasicPortService,
       "flWorkBasicPortProtocol": flWorkBasicPortProtocol,
       "flWorkBasicPortTransport": flWorkBasicPortTransport,
       "flWorkBasicPort": flWorkBasicPort,
       "flWorkComponents": flWorkComponents,
       "flWorkComponentsTable": flWorkComponentsTable,
       "flWorkComponentsEntry": flWorkComponentsEntry,
       "flWorkComponentsIndex": flWorkComponentsIndex,
       "flWorkComponentsOID": flWorkComponentsOID,
       "flWorkComponentsURL": flWorkComponentsURL,
       "flWorkComponentsDevSign": flWorkComponentsDevSign,
       "flWorkTraps": flWorkTraps,
       "flWorkTrapsDelemeter": flWorkTrapsDelemeter,
       "trapPasswdAccess": trapPasswdAccess,
       "trapFWHealth": trapFWHealth,
       "trapFWConf": trapFWConf,
       "trapPowerSupply": trapPowerSupply,
       "trapSecurityPort": trapSecurityPort,
       "trapRstpRingFailure": trapRstpRingFailure,
       "trapPofScrjPort": trapPofScrjPort,
       "trapPoEPort": trapPoEPort,
       "trapMrpStatusChange": trapMrpStatusChange,
       "trapTemperatureManagement": trapTemperatureManagement,
       "trapDigitalInput": trapDigitalInput,
       "trapSDcardPluggedin": trapSDcardPluggedin,
       "trapSDcardPluggedout": trapSDcardPluggedout,
       "trapConfSaved": trapConfSaved,
       "trapIPconflict": trapIPconflict,
       "trapDLRRingChange": trapDLRRingChange,
       "trapPowerSupplyLow": trapPowerSupplyLow,
       "trapConfigDiff": trapConfigDiff,
       "trapCrcOk": trapCrcOk,
       "trapCrcWarning": trapCrcWarning,
       "trapCrcCritical": trapCrcCritical,
       "trapCrcPeakIncreased": trapCrcPeakIncreased,
       "trapEventTableOverflow": trapEventTableOverflow,
       "trapUserConfigChanged": trapUserConfigChanged,
       "trapConfigParamChanged": trapConfigParamChanged,
       "trapManagerConnection": trapManagerConnection,
       "flWorkNet": flWorkNet,
       "flWorkNetIfParameter": flWorkNetIfParameter,
       "flWorkNetIfParamPhyAddress": flWorkNetIfParamPhyAddress,
       "flWorkNetIfParamIpAddress": flWorkNetIfParamIpAddress,
       "flWorkNetIfParamSubnetmask": flWorkNetIfParamSubnetmask,
       "flWorkNetIfParamGwIpAddress": flWorkNetIfParamGwIpAddress,
       "flWorkNetIfParamStatus": flWorkNetIfParamStatus,
       "flWorkNetIfParamSave": flWorkNetIfParamSave,
       "flWorkNetIfParamAssignment": flWorkNetIfParamAssignment,
       "flWorkNetIfParamManagementVlanId": flWorkNetIfParamManagementVlanId,
       "flWorkNetIfParamConflictDetection": flWorkNetIfParamConflictDetection,
       "flWorkNetIfParamDnsServerTable": flWorkNetIfParamDnsServerTable,
       "flWorkNetIfParamDnsServerEntry": flWorkNetIfParamDnsServerEntry,
       "flWorkNetIfParamDnsServerIndex": flWorkNetIfParamDnsServerIndex,
       "flWorkNetIfParamDnsServerIPAddr": flWorkNetIfParamDnsServerIPAddr,
       "flWorkNetPort": flWorkNetPort,
       "flWorkNetPortCapacity": flWorkNetPortCapacity,
       "flWorkNetPortTable": flWorkNetPortTable,
       "flWorkNetPortEntry": flWorkNetPortEntry,
       "flWorkNetPortIndex": flWorkNetPortIndex,
       "flWorkNetPortLinkState": flWorkNetPortLinkState,
       "flWorkNetPortSpeed": flWorkNetPortSpeed,
       "flWorkNetPortDuplexMode": flWorkNetPortDuplexMode,
       "flWorkNetPortNegotiation": flWorkNetPortNegotiation,
       "flWorkNetPortName": flWorkNetPortName,
       "flWorkNetPortEnable": flWorkNetPortEnable,
       "flWorkNetPortLinkMonitoring": flWorkNetPortLinkMonitoring,
       "flWorkNetPortModus": flWorkNetPortModus,
       "flWorkNetPortSTPEnable": flWorkNetPortSTPEnable,
       "flWorkNetPortIfIndex": flWorkNetPortIfIndex,
       "flWorkNetPortLLWHPort": flWorkNetPortLLWHPort,
       "flWorkNetPortType": flWorkNetPortType,
       "flWorkNetPortModuleName": flWorkNetPortModuleName,
       "flWorkNetPortInterfaceName": flWorkNetPortInterfaceName,
       "flWorkNetPortPriorityLevel": flWorkNetPortPriorityLevel,
       "flWorkNetPortPofTransmittingPower": flWorkNetPortPofTransmittingPower,
       "flWorkNetPortStpMode": flWorkNetPortStpMode,
       "flWorkNetPortFlowControl": flWorkNetPortFlowControl,
       "flWorkNetPortMaxFrameSize": flWorkNetPortMaxFrameSize,
       "flWorkNetPortJumboFrame": flWorkNetPortJumboFrame,
       "flWorkNetPortCableLength": flWorkNetPortCableLength,
       "flWorkNetPortPHYcompatibility": flWorkNetPortPHYcompatibility,
       "flWorkNetPortPoETable": flWorkNetPortPoETable,
       "flWorkNetPortPoEEntry": flWorkNetPortPoEEntry,
       "flWorkNetPortPoEIndex": flWorkNetPortPoEIndex,
       "flWorkNetPortPoEPowerEnable": flWorkNetPortPoEPowerEnable,
       "flWorkNetPortPoECurrentLimitation": flWorkNetPortPoECurrentLimitation,
       "flWorkNetPortPoEDeviceClass": flWorkNetPortPoEDeviceClass,
       "flWorkNetPortPoEOutputCurrent": flWorkNetPortPoEOutputCurrent,
       "flWorkNetPortPoEOutputVoltage": flWorkNetPortPoEOutputVoltage,
       "flWorkNetPortPoEFaultStatus": flWorkNetPortPoEFaultStatus,
       "flWorkNetPortPoeFaultMonitoring": flWorkNetPortPoeFaultMonitoring,
       "flWorkNetPortPofScrjIfTable": flWorkNetPortPofScrjIfTable,
       "flWorkNetPortPofScrjIfEntry": flWorkNetPortPofScrjIfEntry,
       "flWorkNetPortPofScrjIfIndex": flWorkNetPortPofScrjIfIndex,
       "flWorkNetPortPofScrjIfStatus": flWorkNetPortPofScrjIfStatus,
       "flWorkNetPortPofScrjIfSupplyVoltage": flWorkNetPortPofScrjIfSupplyVoltage,
       "flWorkNetPortPofScrjIfTxPower": flWorkNetPortPofScrjIfTxPower,
       "flWorkNetPortPofScrjIfRxPower": flWorkNetPortPofScrjIfRxPower,
       "flWorkNetPortPofScrjIfSystemReserve": flWorkNetPortPofScrjIfSystemReserve,
       "flWorkNetPortPofScrjIfRxPowerHighAlarm": flWorkNetPortPofScrjIfRxPowerHighAlarm,
       "flWorkNetPortPofScrjIfRxPowerLowAlarm": flWorkNetPortPofScrjIfRxPowerLowAlarm,
       "flWorkNetPortPofScrjIfRxPowerHighWarning": flWorkNetPortPofScrjIfRxPowerHighWarning,
       "flWorkNetPortPofScrjIfRxPowerLowWarning": flWorkNetPortPofScrjIfRxPowerLowWarning,
       "flWorkNetPortPofScrjIfManufacturer": flWorkNetPortPofScrjIfManufacturer,
       "flWorkNetPortPofScrjIfManufactOui": flWorkNetPortPofScrjIfManufactOui,
       "flWorkNetPortPofScrjIfRevision": flWorkNetPortPofScrjIfRevision,
       "flWorkNetPortPofScrjIfWavelength": flWorkNetPortPofScrjIfWavelength,
       "flWorkNetPortPofScrjIfTransceiverOptions": flWorkNetPortPofScrjIfTransceiverOptions,
       "flWorkNetPortPofScrjIfSerialNumber": flWorkNetPortPofScrjIfSerialNumber,
       "flWorkNetPortPofScrjIfDatecodeAndLot": flWorkNetPortPofScrjIfDatecodeAndLot,
       "flWorkNetPortPofScrjIfAlarmContactEnable": flWorkNetPortPofScrjIfAlarmContactEnable,
       "flWorkNetSFPModuleTable": flWorkNetSFPModuleTable,
       "flWorkNetSFPModuleEntry": flWorkNetSFPModuleEntry,
       "flWorkNetSFPModuleIndex": flWorkNetSFPModuleIndex,
       "flWorkNetSFPModuleType": flWorkNetSFPModuleType,
       "flWorkNetSFPModuleMedia": flWorkNetSFPModuleMedia,
       "flWorkNetSFPModuleVendor": flWorkNetSFPModuleVendor,
       "flWorkNetSFPModulePartNo": flWorkNetSFPModulePartNo,
       "flWorkNetSFPModuleSerialNo": flWorkNetSFPModuleSerialNo,
       "flWorkNetSFPModuleRev": flWorkNetSFPModuleRev,
       "flWorkNetSFPModuleLinkLength": flWorkNetSFPModuleLinkLength,
       "flWorkNetSFPModuleBitrate": flWorkNetSFPModuleBitrate,
       "flWorkNetSFPModuleTransceiverCode": flWorkNetSFPModuleTransceiverCode,
       "flWorkNetSFPModuleEncoding": flWorkNetSFPModuleEncoding,
       "flWorkNetSFPPortTxPower": flWorkNetSFPPortTxPower,
       "flWorkNetSFPPortRxPower": flWorkNetSFPPortRxPower,
       "flWorkNetIfList": flWorkNetIfList,
       "flWorkNetIfTable": flWorkNetIfTable,
       "flWorkNetIfEntry": flWorkNetIfEntry,
       "flWorkNetIfPhyAddress": flWorkNetIfPhyAddress,
       "flWorkNetIfIpAddress": flWorkNetIfIpAddress,
       "flWorkNetIfSubnetmask": flWorkNetIfSubnetmask,
       "flWorkNetIfGwIpAddress": flWorkNetIfGwIpAddress,
       "flWorkNetIfStatus": flWorkNetIfStatus,
       "flWorkNetIfSave": flWorkNetIfSave,
       "flWorkNetIfAssignment": flWorkNetIfAssignment,
       "flWorkNetIfManagementVlanId": flWorkNetIfManagementVlanId,
       "flWorkNetACD": flWorkNetACD,
       "flWorkNetACDStatus": flWorkNetACDStatus,
       "flWorkNetACDIP": flWorkNetACDIP,
       "flWorkNetACDMAC": flWorkNetACDMAC,
       "flWorkFirmware": flWorkFirmware,
       "flWorkFWInfo": flWorkFWInfo,
       "flWorkFWInfoVersion": flWorkFWInfoVersion,
       "flWorkFWInfoState": flWorkFWInfoState,
       "flWorkFWInfoDate": flWorkFWInfoDate,
       "flWorkFWInfoTime": flWorkFWInfoTime,
       "flWorkFWInfoCopyright": flWorkFWInfoCopyright,
       "flWorkFWInfoBootVersion": flWorkFWInfoBootVersion,
       "flWorkFWInfoBootState": flWorkFWInfoBootState,
       "flWorkFWInfoBootDate": flWorkFWInfoBootDate,
       "flWorkFWInfoBootTime": flWorkFWInfoBootTime,
       "flWorkFWInfoOperStatus": flWorkFWInfoOperStatus,
       "flWorkFWInfoHealthText": flWorkFWInfoHealthText,
       "flWorkFWInfoDisplay": flWorkFWInfoDisplay,
       "flWorkFWInfoEvent": flWorkFWInfoEvent,
       "flWorkFWInfoEventTable": flWorkFWInfoEventTable,
       "flWorkFWInfoEventEntry": flWorkFWInfoEventEntry,
       "flWorkFWInfoEventIndex": flWorkFWInfoEventIndex,
       "flWorkFWInfoEventCode": flWorkFWInfoEventCode,
       "flWorkFWInfoEventDescription": flWorkFWInfoEventDescription,
       "flWorkFWInfoEventSystemUpTime": flWorkFWInfoEventSystemUpTime,
       "flWorkFWInfoEventSntpTime": flWorkFWInfoEventSntpTime,
       "flWorkFWInfoEventSntpDate": flWorkFWInfoEventSntpDate,
       "flWorkFWInfoEventSntpSeconds": flWorkFWInfoEventSntpSeconds,
       "flWorkFWInfoEventSntpFractionalSeconds": flWorkFWInfoEventSntpFractionalSeconds,
       "flWorkFWInfoEventTableClear": flWorkFWInfoEventTableClear,
       "flWorkFWCtrl": flWorkFWCtrl,
       "flWorkFWCtrlBasic": flWorkFWCtrlBasic,
       "flWorkFWCtrlReset": flWorkFWCtrlReset,
       "flWorkFWCtrlTrapDestCapacity": flWorkFWCtrlTrapDestCapacity,
       "flWorkFWCtrlWatchdog": flWorkFWCtrlWatchdog,
       "flWorkFWCtrlHTTP": flWorkFWCtrlHTTP,
       "flWorkFWCtrlTelnet": flWorkFWCtrlTelnet,
       "flWorkFWCtrlWebPageRefresh": flWorkFWCtrlWebPageRefresh,
       "flWorkFWCtrlSNMP": flWorkFWCtrlSNMP,
       "flWorkFWCtrlOperatingMode": flWorkFWCtrlOperatingMode,
       "flWorkFWCtrlIfCounters": flWorkFWCtrlIfCounters,
       "flWorkFWCtrlHTTPSecure": flWorkFWCtrlHTTPSecure,
       "flWorkFWCtrlSSH": flWorkFWCtrlSSH,
       "flWorkFWCtrlSNMPv3": flWorkFWCtrlSNMPv3,
       "flWorkFwCtrlCpuOverloadStopForwarding": flWorkFwCtrlCpuOverloadStopForwarding,
       "flWorkFWCtrlDisplayRights": flWorkFWCtrlDisplayRights,
       "flWorkFWCtrlDisplayContrast": flWorkFWCtrlDisplayContrast,
       "flWorkFWCtrlCLIIPSock": flWorkFWCtrlCLIIPSock,
       "flWorkFWCtrlLEDsOff": flWorkFWCtrlLEDsOff,
       "flWorkFWCtrlWebServerMode": flWorkFWCtrlWebServerMode,
       "flWorkFWCtrlSnmpAgentMode": flWorkFWCtrlSnmpAgentMode,
       "flWorkFWCtrlCliServiceMode": flWorkFWCtrlCliServiceMode,
       "flWorkFWCtrlPersistentEventLoggingMode": flWorkFWCtrlPersistentEventLoggingMode,
       "flWorkFWCtrlSmartModeGblEnable": flWorkFWCtrlSmartModeGblEnable,
       "flWorkFWCtrlHostnameResolutionEnable": flWorkFWCtrlHostnameResolutionEnable,
       "flWorkFWCtrlHostname": flWorkFWCtrlHostname,
       "flWorkFWCtrlSdCardGblEnable": flWorkFWCtrlSdCardGblEnable,
       "flWorkFWCtrlWebLoginRequired": flWorkFWCtrlWebLoginRequired,
       "flWorkFWCtrlTopologyBasedIpPort": flWorkFWCtrlTopologyBasedIpPort,
       "flWorkFWCtrlTopologyBasedIpState": flWorkFWCtrlTopologyBasedIpState,
       "flWorkFWCtrlTrapDest": flWorkFWCtrlTrapDest,
       "flWorkFWCtrlTrapDestTable": flWorkFWCtrlTrapDestTable,
       "flWorkFWCtrlTrapDestEntry": flWorkFWCtrlTrapDestEntry,
       "flWorkFWCtrlTrapDestIndex": flWorkFWCtrlTrapDestIndex,
       "flWorkFWCtrlTrapDestIPAddr": flWorkFWCtrlTrapDestIPAddr,
       "flWorkFWCtrlTrapDestName": flWorkFWCtrlTrapDestName,
       "flWorkFWCtrlTrapDestCapacityMax": flWorkFWCtrlTrapDestCapacityMax,
       "flWorkFWCtrlTrapDestEnable": flWorkFWCtrlTrapDestEnable,
       "flWorkFWCtrlTrapLink": flWorkFWCtrlTrapLink,
       "flWorkFWCtrlTrapConnectionTest": flWorkFWCtrlTrapConnectionTest,
       "flWorkFWCtrlTrapEnableTable": flWorkFWCtrlTrapEnableTable,
       "flWorkFWCtrlTrapEnableEntry": flWorkFWCtrlTrapEnableEntry,
       "flWorkFWCtrlTrapEnableIndex": flWorkFWCtrlTrapEnableIndex,
       "flWorkFWCtrlTrapEnableOid": flWorkFWCtrlTrapEnableOid,
       "flWorkFWCtrlTrapEnableName": flWorkFWCtrlTrapEnableName,
       "flWorkFWCtrlTrapEnableStatus": flWorkFWCtrlTrapEnableStatus,
       "flWorkFWCtrlPasswd": flWorkFWCtrlPasswd,
       "flWorkFWCtrlPasswdSet": flWorkFWCtrlPasswdSet,
       "flWorkFWCtrlPasswdSuccess": flWorkFWCtrlPasswdSuccess,
       "flWorkFWCtrlLoginExpire": flWorkFWCtrlLoginExpire,
       "flWorkFWCtrlUpdate": flWorkFWCtrlUpdate,
       "flWorkFWCtrlTftpIPAddr": flWorkFWCtrlTftpIPAddr,
       "flWorkFWCtrlTftpFile": flWorkFWCtrlTftpFile,
       "flWorkFWCtrlUpdateStatus": flWorkFWCtrlUpdateStatus,
       "flWorkFWCtrlUpdateExecute": flWorkFWCtrlUpdateExecute,
       "flWorkFWCtrlRunningUpdate": flWorkFWCtrlRunningUpdate,
       "flWorkFWCtrlAutoUpdate": flWorkFWCtrlAutoUpdate,
       "flWorkFWCtrlTftpImage": flWorkFWCtrlTftpImage,
       "flWorkFWCtrlConf": flWorkFWCtrlConf,
       "flWorkFWCtrlConfStatus": flWorkFWCtrlConfStatus,
       "flWorkFWCtrlConfSave": flWorkFWCtrlConfSave,
       "flWorkFWCtrlDefaultUponDelivery": flWorkFWCtrlDefaultUponDelivery,
       "flWorkFWCtrlConfName": flWorkFWCtrlConfName,
       "flWorkFWCtrlConfSource": flWorkFWCtrlConfSource,
       "flWorkFWCtrlLoginSessions": flWorkFWCtrlLoginSessions,
       "flWorkFWCtrlPasswords": flWorkFWCtrlPasswords,
       "flWorkFWCtrlSwitchStats": flWorkFWCtrlSwitchStats,
       "flWorkFWCtrlTrapLog": flWorkFWCtrlTrapLog,
       "flWorkFWConfig": flWorkFWConfig,
       "flWorkFWConfigTftpIPAddr": flWorkFWConfigTftpIPAddr,
       "flWorkFWConfigTftpFile": flWorkFWConfigTftpFile,
       "flWorkFWConfigStatus": flWorkFWConfigStatus,
       "flWorkFWConfigExecute": flWorkFWConfigExecute,
       "flWorkFWRunningConfig": flWorkFWRunningConfig,
       "flWorkFWCtrlConfigPluggable": flWorkFWCtrlConfigPluggable,
       "flWorkFWCtrlConfPluggableStatus": flWorkFWCtrlConfPluggableStatus,
       "flWorkFWCtrlConfPluggableClear": flWorkFWCtrlConfPluggableClear,
       "flWorkFWCtrlConfPluggableCompare": flWorkFWCtrlConfPluggableCompare,
       "flWorkFWCtrlConfPluggableCompareStatus": flWorkFWCtrlConfPluggableCompareStatus,
       "flWorkFWCtrlConfigMemInfo": flWorkFWCtrlConfigMemInfo,
       "flWorkFWCtrlConfigMemConfName": flWorkFWCtrlConfigMemConfName,
       "flWorkFWCtrlConfigMemFwVersion": flWorkFWCtrlConfigMemFwVersion,
       "flWorkFWCtrlConfigMemIpAddress": flWorkFWCtrlConfigMemIpAddress,
       "flWorkFWCtrlConfigMemMrmFunctionality": flWorkFWCtrlConfigMemMrmFunctionality,
       "flWorkFWCtrlConfigMemSerialNumber": flWorkFWCtrlConfigMemSerialNumber,
       "flWorkFWCtrlConfigMemManufacturingId": flWorkFWCtrlConfigMemManufacturingId,
       "flWorkFWCtrlConfigMemType": flWorkFWCtrlConfigMemType,
       "flWorkFWCtrlConfigMemL3License": flWorkFWCtrlConfigMemL3License,
       "flWorkFWCtrlSerial": flWorkFWCtrlSerial,
       "flWorkFWCtrlSerialBaud": flWorkFWCtrlSerialBaud,
       "flWorkFWCtrlSerialDataBits": flWorkFWCtrlSerialDataBits,
       "flWorkFWCtrlSerialStopBits": flWorkFWCtrlSerialStopBits,
       "flWorkFWCtrlSerialParity": flWorkFWCtrlSerialParity,
       "flWorkFWCtrlSerialFlowControl": flWorkFWCtrlSerialFlowControl,
       "flWorkFWCtrlSerialTimeout": flWorkFWCtrlSerialTimeout,
       "flWorkFWCtrlAlarmContact": flWorkFWCtrlAlarmContact,
       "flWorkFWCtrlAlarmContactEvents": flWorkFWCtrlAlarmContactEvents,
       "flWorkFWCtrlAlarmContactEventPowerSupply": flWorkFWCtrlAlarmContactEventPowerSupply,
       "flWorkFWCtrlAlarmContactEventLinkState": flWorkFWCtrlAlarmContactEventLinkState,
       "flWorkFWCtrlAlarmContactEventSecurityPortBlocked": flWorkFWCtrlAlarmContactEventSecurityPortBlocked,
       "flWorkFWCtrlAlarmContactEventPoeFaultDetected": flWorkFWCtrlAlarmContactEventPoeFaultDetected,
       "flWorkFWCtrlAlarmContactEventMrpRingFailure": flWorkFWCtrlAlarmContactEventMrpRingFailure,
       "flWorkFWCtrlAlarmContactEventConfigMemFail": flWorkFWCtrlAlarmContactEventConfigMemFail,
       "flWorkFWCtrlAlarmContactEventPoFScrjTransCritical": flWorkFWCtrlAlarmContactEventPoFScrjTransCritical,
       "flWorkFWCtrlAlarmContactEventDlrRingFailure": flWorkFWCtrlAlarmContactEventDlrRingFailure,
       "flWorkFWCtrlAlarmContactEnable": flWorkFWCtrlAlarmContactEnable,
       "flWorkFWCtrlAlarmContactStatus": flWorkFWCtrlAlarmContactStatus,
       "flWorkFWCtrlAlarmContactReason": flWorkFWCtrlAlarmContactReason,
       "flWorkFWCtrlAlarmContact2Events": flWorkFWCtrlAlarmContact2Events,
       "flWorkFWCtrlAlarmContact2EventPowerSupply": flWorkFWCtrlAlarmContact2EventPowerSupply,
       "flWorkFWCtrlAlarmContact2EventLinkState": flWorkFWCtrlAlarmContact2EventLinkState,
       "flWorkFWCtrlAlarmContact2EventSecurityPortBlocked": flWorkFWCtrlAlarmContact2EventSecurityPortBlocked,
       "flWorkFWCtrlAlarmContact2EventPoeFaultDetected": flWorkFWCtrlAlarmContact2EventPoeFaultDetected,
       "flWorkFWCtrlAlarmContact2EventMrpRingFailure": flWorkFWCtrlAlarmContact2EventMrpRingFailure,
       "flWorkFWCtrlAlarmContact2EventConfigMemFail": flWorkFWCtrlAlarmContact2EventConfigMemFail,
       "flWorkFWCtrlAlarmContact2EventPoFScrjTransCritical": flWorkFWCtrlAlarmContact2EventPoFScrjTransCritical,
       "flWorkFWCtrlAlarmContact2EventDlrRingFailure": flWorkFWCtrlAlarmContact2EventDlrRingFailure,
       "flWorkFWCtrlAlarmContact2Enable": flWorkFWCtrlAlarmContact2Enable,
       "flWorkFWCtrlAlarmContact2Status": flWorkFWCtrlAlarmContact2Status,
       "flWorkFWCtrlAlarmContact2Reason": flWorkFWCtrlAlarmContact2Reason,
       "flWorkFWCtrlSecurity": flWorkFWCtrlSecurity,
       "flWorkFWCtrlSecurityAccess": flWorkFWCtrlSecurityAccess,
       "flWorkFWCtrlSecurityAccessTable": flWorkFWCtrlSecurityAccessTable,
       "flWorkFWCtrlSecurityAccessEntry": flWorkFWCtrlSecurityAccessEntry,
       "flWorkFWCtrlSecurityAccessIndex": flWorkFWCtrlSecurityAccessIndex,
       "flWorkFWCtrlSecurityAccessAddr": flWorkFWCtrlSecurityAccessAddr,
       "flWorkFWCtrlSecurityAccessDescr": flWorkFWCtrlSecurityAccessDescr,
       "flWorkFWCtrlSecurityAccessRight": flWorkFWCtrlSecurityAccessRight,
       "flWorkFWCtrlSecurityAccessTableCapacityMax": flWorkFWCtrlSecurityAccessTableCapacityMax,
       "flWorkFWCtrlSecurityAccessEnable": flWorkFWCtrlSecurityAccessEnable,
       "flWorkFWCtrlSecurityPort": flWorkFWCtrlSecurityPort,
       "flWorkFWCtrlSecurityPortTable": flWorkFWCtrlSecurityPortTable,
       "flWorkFWCtrlSecurityPortEntry": flWorkFWCtrlSecurityPortEntry,
       "flWorkFWCtrlSecurityPortIndex": flWorkFWCtrlSecurityPortIndex,
       "flWorkFWCtrlSecurityPortLastMacAddr": flWorkFWCtrlSecurityPortLastMacAddr,
       "flWorkFWCtrlSecurityPortMode": flWorkFWCtrlSecurityPortMode,
       "flWorkFWCtrlSecurityPortState": flWorkFWCtrlSecurityPortState,
       "flWorkFWCtrlSecurityPortIllegalAddrCounter": flWorkFWCtrlSecurityPortIllegalAddrCounter,
       "flWorkFWCtrlSecurityPortMacTable": flWorkFWCtrlSecurityPortMacTable,
       "flWorkFWCtrlSecurityPortMacEntry": flWorkFWCtrlSecurityPortMacEntry,
       "flWorkFWCtrlSecurityPortMacIndex": flWorkFWCtrlSecurityPortMacIndex,
       "flWorkFWCtrlSecurityPortMacAddr": flWorkFWCtrlSecurityPortMacAddr,
       "flWorkFWCtrlSecurityPortMacDescr": flWorkFWCtrlSecurityPortMacDescr,
       "flWorkFWCtrlSecurityPortMacVlanID": flWorkFWCtrlSecurityPortMacVlanID,
       "flWorkFWCtrlSecurityPortMacDelete": flWorkFWCtrlSecurityPortMacDelete,
       "flWorkFWCtrlSecurityPortTableCapacityMax": flWorkFWCtrlSecurityPortTableCapacityMax,
       "flWorkFWCtrlSecurityPortMacTableCapacityMax": flWorkFWCtrlSecurityPortMacTableCapacityMax,
       "flWorkFWCtrlSecurityPortEnable": flWorkFWCtrlSecurityPortEnable,
       "flWorkFWCtrlSecurityPortIllegalAddrCounterClear": flWorkFWCtrlSecurityPortIllegalAddrCounterClear,
       "flWorkFWCtrlSecurityPortIpFilterTable": flWorkFWCtrlSecurityPortIpFilterTable,
       "flWorkFWCtrlSecurityPortIpFilterEntry": flWorkFWCtrlSecurityPortIpFilterEntry,
       "flWorkFWCtrlSecurityPortIpFilterIndex": flWorkFWCtrlSecurityPortIpFilterIndex,
       "flWorkFWCtrlSecurityPortIpFilterAddr": flWorkFWCtrlSecurityPortIpFilterAddr,
       "flWorkFWCtrlSecurityPortIpFilterDescr": flWorkFWCtrlSecurityPortIpFilterDescr,
       "flWorkFWCtrlSecurityPortIpFilterPort": flWorkFWCtrlSecurityPortIpFilterPort,
       "flWorkFWCtrlSecurityPortIpFilterTableCapacityMax": flWorkFWCtrlSecurityPortIpFilterTableCapacityMax,
       "flWorkFWCtrlSecurityMAConMultiplePorts": flWorkFWCtrlSecurityMAConMultiplePorts,
       "flWorkFWCtrlSecurityDot1x": flWorkFWCtrlSecurityDot1x,
       "flWorkFWCtrlSecurityDot1xPortTable": flWorkFWCtrlSecurityDot1xPortTable,
       "flWorkFWCtrlSecurityDot1xPortEntry": flWorkFWCtrlSecurityDot1xPortEntry,
       "flWorkFWCtrlSecurityDot1xGuestVlanId": flWorkFWCtrlSecurityDot1xGuestVlanId,
       "flWorkFWCtrlSecurityDot1xAssignTimeout": flWorkFWCtrlSecurityDot1xAssignTimeout,
       "flWorkFWCtrlSecurityDot1xVlanAssign": flWorkFWCtrlSecurityDot1xVlanAssign,
       "flWorkFWCtrlSecurityRadiusAuthServTable": flWorkFWCtrlSecurityRadiusAuthServTable,
       "flWorkFWCtrlSecurityRadiusAuthServEntry": flWorkFWCtrlSecurityRadiusAuthServEntry,
       "flWorkFWCtrlSecurityRadiusServIndex": flWorkFWCtrlSecurityRadiusServIndex,
       "flWorkFWCtrlSecurityRadiusServAddress": flWorkFWCtrlSecurityRadiusServAddress,
       "flWorkFWCtrlSecurityRadiusServPort": flWorkFWCtrlSecurityRadiusServPort,
       "flWorkFWCtrlSecurityRadiusServSharedSecret": flWorkFWCtrlSecurityRadiusServSharedSecret,
       "flWorkFWCtrlSecurityRadiusServName": flWorkFWCtrlSecurityRadiusServName,
       "flWorkFWCtrlProfinet": flWorkFWCtrlProfinet,
       "flWorkFWCtrlProfinetAlarm": flWorkFWCtrlProfinetAlarm,
       "flWorkFWCtrlProfinetAlarmPortTable": flWorkFWCtrlProfinetAlarmPortTable,
       "flWorkFWCtrlProfinetAlarmPortEntry": flWorkFWCtrlProfinetAlarmPortEntry,
       "flWorkFWCtrlProfinetAlarmPortIndex": flWorkFWCtrlProfinetAlarmPortIndex,
       "flWorkFWCtrlProfinetAlarmPortLinkMonitoring": flWorkFWCtrlProfinetAlarmPortLinkMonitoring,
       "flWorkFWCtrlProfinetAlarmPortPofScrjDiag": flWorkFWCtrlProfinetAlarmPortPofScrjDiag,
       "flWorkFWCtrlProfinetAlarmPortSFPMissing": flWorkFWCtrlProfinetAlarmPortSFPMissing,
       "flWorkFWCtrlProfinetAlarmPowerSupply": flWorkFWCtrlProfinetAlarmPowerSupply,
       "flWorkFWCtrlProfinetAlarmModuleRemove": flWorkFWCtrlProfinetAlarmModuleRemove,
       "flWorkFWCtrlProfinetAlarmPlugableMemory": flWorkFWCtrlProfinetAlarmPlugableMemory,
       "flWorkFWCtrlProfinetAlarmMRPRingFailure": flWorkFWCtrlProfinetAlarmMRPRingFailure,
       "flWorkFWCtrlProfinetStatus": flWorkFWCtrlProfinetStatus,
       "flWorkFWCtrlProfinetStatusActiveARs": flWorkFWCtrlProfinetStatusActiveARs,
       "flWorkFWCtrlProfinetStatusConReqCount": flWorkFWCtrlProfinetStatusConReqCount,
       "flWorkFWCtrlProfinetStatusDiagStatus": flWorkFWCtrlProfinetStatusDiagStatus,
       "flWorkFWCtrlProfinetBoundarySettings": flWorkFWCtrlProfinetBoundarySettings,
       "flWorkFWCtrlProfinetBoundarySettingsTable": flWorkFWCtrlProfinetBoundarySettingsTable,
       "flWorkFWCtrlProfinetBoundarySettingsEntry": flWorkFWCtrlProfinetBoundarySettingsEntry,
       "flWorkFWCtrlProfinetBoundarySettingsPortIndex": flWorkFWCtrlProfinetBoundarySettingsPortIndex,
       "flWorkFWCtrlProfinetBoundarySettingsDcpIdentify": flWorkFWCtrlProfinetBoundarySettingsDcpIdentify,
       "flWorkFWCtrlProfinetBoundarySettingsDcpHello": flWorkFWCtrlProfinetBoundarySettingsDcpHello,
       "flWorkFWCtrlProfinetBoundarySettingsLLDP": flWorkFWCtrlProfinetBoundarySettingsLLDP,
       "flWorkFWCtrlMRP": flWorkFWCtrlMRP,
       "flWorkFWCtrlMRPConfig": flWorkFWCtrlMRPConfig,
       "flWorkFWCtrlMRPConfigDomainTable": flWorkFWCtrlMRPConfigDomainTable,
       "flWorkFWCtrlMRPConfigDomainEntry": flWorkFWCtrlMRPConfigDomainEntry,
       "flWorkFWCtrlMRPConfigDomainIdx": flWorkFWCtrlMRPConfigDomainIdx,
       "flWorkFWCtrlMRPConfigDomainUdid": flWorkFWCtrlMRPConfigDomainUdid,
       "flWorkFWCtrlMRPConfigDomainName": flWorkFWCtrlMRPConfigDomainName,
       "flWorkFWCtrlMRPConfigDomainRole": flWorkFWCtrlMRPConfigDomainRole,
       "flWorkFWCtrlMRPConfigDomainManagerPriority": flWorkFWCtrlMRPConfigDomainManagerPriority,
       "flWorkFWCtrlMRPConfigDomainVlanID": flWorkFWCtrlMRPConfigDomainVlanID,
       "flWorkFWCtrlMRPConfigDomainRingPort1": flWorkFWCtrlMRPConfigDomainRingPort1,
       "flWorkFWCtrlMRPConfigDomainRingPort2": flWorkFWCtrlMRPConfigDomainRingPort2,
       "flWorkFWCtrlMRPConfigDomainResetRoundTripDelays": flWorkFWCtrlMRPConfigDomainResetRoundTripDelays,
       "flWorkFWCtrlMRPInfo": flWorkFWCtrlMRPInfo,
       "flWorkFWCtrlMRPInfoDomainTable": flWorkFWCtrlMRPInfoDomainTable,
       "flWorkFWCtrlMRPInfoDomainEntry": flWorkFWCtrlMRPInfoDomainEntry,
       "flWorkFWCtrlMRPInfoDomainIdx": flWorkFWCtrlMRPInfoDomainIdx,
       "flWorkFWCtrlMRPInfoDomainUuid": flWorkFWCtrlMRPInfoDomainUuid,
       "flWorkFWCtrlMRPInfoDomainName": flWorkFWCtrlMRPInfoDomainName,
       "flWorkFWCtrlMRPInfoDomainAdminRole": flWorkFWCtrlMRPInfoDomainAdminRole,
       "flWorkFWCtrlMRPInfoDomainOperRole": flWorkFWCtrlMRPInfoDomainOperRole,
       "flWorkFWCtrlMRPInfoDomainManagerPriority": flWorkFWCtrlMRPInfoDomainManagerPriority,
       "flWorkFWCtrlMRPInfoDomainRingPort1": flWorkFWCtrlMRPInfoDomainRingPort1,
       "flWorkFWCtrlMRPInfoDomainRingPort1State": flWorkFWCtrlMRPInfoDomainRingPort1State,
       "flWorkFWCtrlMRPInfoDomainRingPort2": flWorkFWCtrlMRPInfoDomainRingPort2,
       "flWorkFWCtrlMRPInfoDomainRingPort2State": flWorkFWCtrlMRPInfoDomainRingPort2State,
       "flWorkFWCtrlMRPInfoDomainState": flWorkFWCtrlMRPInfoDomainState,
       "flWorkFWCtrlMRPInfoDomainError": flWorkFWCtrlMRPInfoDomainError,
       "flWorkFWCtrlMRPInfoDomainRingOpenCount": flWorkFWCtrlMRPInfoDomainRingOpenCount,
       "flWorkFWCtrlMRPInfoDomainLastRingOpenChange": flWorkFWCtrlMRPInfoDomainLastRingOpenChange,
       "flWorkFWCtrlMRPInfoDomainRoundTripDelayMax": flWorkFWCtrlMRPInfoDomainRoundTripDelayMax,
       "flWorkFWCtrlMRPInfoDomainRoundTripDelayMin": flWorkFWCtrlMRPInfoDomainRoundTripDelayMin,
       "flWorkFWCtrlMRPInfoDeviceBlockingSupport": flWorkFWCtrlMRPInfoDeviceBlockingSupport,
       "flWorkFWCtrlTemp": flWorkFWCtrlTemp,
       "flWorkFWCtrlActualDeviceTemperature": flWorkFWCtrlActualDeviceTemperature,
       "flWorkFWCtrlMinOperTemperature": flWorkFWCtrlMinOperTemperature,
       "flWorkFWCtrlMaxOperTemperature": flWorkFWCtrlMaxOperTemperature,
       "flWorkFWCtrlUserTempWarningThreshold": flWorkFWCtrlUserTempWarningThreshold,
       "flWorkFWCtrlTempShutdownPrevention": flWorkFWCtrlTempShutdownPrevention,
       "flWorkFWCtrlTelnetGroup": flWorkFWCtrlTelnetGroup,
       "flWorkFWCtrlTelnetLoginTimeout": flWorkFWCtrlTelnetLoginTimeout,
       "flWorkFWCtrlTelnetMaxSessions": flWorkFWCtrlTelnetMaxSessions,
       "flWorkFWCtrlTelnetAllowNewMode": flWorkFWCtrlTelnetAllowNewMode,
       "flWorkFWCtrlImage": flWorkFWCtrlImage,
       "flWorkFWCtrlImage1": flWorkFWCtrlImage1,
       "flWorkFWCtrlImage2": flWorkFWCtrlImage2,
       "flWorkFWCtrlActiveImage": flWorkFWCtrlActiveImage,
       "flWorkFWCtrlNextActiveImage": flWorkFWCtrlNextActiveImage,
       "flWorkFWCtrlUserConfigGroup": flWorkFWCtrlUserConfigGroup,
       "flWorkFWCtrlUserConfigCreate": flWorkFWCtrlUserConfigCreate,
       "flWorkFWCtrlUserConfigTable": flWorkFWCtrlUserConfigTable,
       "flWorkFWCtrlUserConfigEntry": flWorkFWCtrlUserConfigEntry,
       "flWorkFWCtrlUserIndex": flWorkFWCtrlUserIndex,
       "flWorkFWCtrlUserName": flWorkFWCtrlUserName,
       "flWorkFWCtrlUserPassword": flWorkFWCtrlUserPassword,
       "flWorkFWCtrlUserAccessMode": flWorkFWCtrlUserAccessMode,
       "flWorkFWCtrlUserStatus": flWorkFWCtrlUserStatus,
       "flWorkFWCtrlUserAuthenticationType": flWorkFWCtrlUserAuthenticationType,
       "flWorkFWCtrlUserEncryptionType": flWorkFWCtrlUserEncryptionType,
       "flWorkFWCtrlUserEncryptionPassword": flWorkFWCtrlUserEncryptionPassword,
       "flWorkFWCtrlUserLockoutStatus": flWorkFWCtrlUserLockoutStatus,
       "flWorkFWCtrlUserPasswordExpireTime": flWorkFWCtrlUserPasswordExpireTime,
       "flWorkFWCtrlDigitalInput": flWorkFWCtrlDigitalInput,
       "flWorkFWCtrlDigitalInputTable": flWorkFWCtrlDigitalInputTable,
       "flWorkFWCtrlDigitalInputEntry": flWorkFWCtrlDigitalInputEntry,
       "flWorkFWCtrlDigitalInputIndex": flWorkFWCtrlDigitalInputIndex,
       "flWorkFWCtrlDigitalInputStatus": flWorkFWCtrlDigitalInputStatus,
       "flWorkFWCtrlDigitalInputEvents": flWorkFWCtrlDigitalInputEvents,
       "flWorkFWCtrlEnergy": flWorkFWCtrlEnergy,
       "flWorkFWCtrlEnergyTest": flWorkFWCtrlEnergyTest,
       "flWorkEnergyPortTable": flWorkEnergyPortTable,
       "flWorkEnergyPortEntry": flWorkEnergyPortEntry,
       "flWorkEnergyPortIndex": flWorkEnergyPortIndex,
       "flWorkEnergyPortModus": flWorkEnergyPortModus,
       "flWorkFWCtrlDigitalOutput": flWorkFWCtrlDigitalOutput,
       "flWorkFWCtrlDigitalOutputTable": flWorkFWCtrlDigitalOutputTable,
       "flWorkFWCtrlDigitalOutputEntry": flWorkFWCtrlDigitalOutputEntry,
       "flWorkFWCtrlDigitalOutputIndex": flWorkFWCtrlDigitalOutputIndex,
       "flWorkFWCtrlDigitalOutputStatus": flWorkFWCtrlDigitalOutputStatus,
       "flWorkFWCtrlDigitalOutputEnable": flWorkFWCtrlDigitalOutputEnable,
       "flWorkFWCtrlDigitalOutputEventDigitalInState": flWorkFWCtrlDigitalOutputEventDigitalInState,
       "flWorkFWCtrlDigitalOutputEventWlanState": flWorkFWCtrlDigitalOutputEventWlanState,
       "flWorkFWCtrlDigitalOutputEventWlanConnection": flWorkFWCtrlDigitalOutputEventWlanConnection,
       "flWorkFWCtrlDLR": flWorkFWCtrlDLR,
       "flWorkFWCtrlDLRDomainTable": flWorkFWCtrlDLRDomainTable,
       "flWorkFWCtrlDLRDomainEntry": flWorkFWCtrlDLRDomainEntry,
       "flWorkFWCtrlDLRDomainIdx": flWorkFWCtrlDLRDomainIdx,
       "flWorkFWCtrlDLRMode": flWorkFWCtrlDLRMode,
       "flWorkFWCtrlDLRPort1": flWorkFWCtrlDLRPort1,
       "flWorkFWCtrlDLRPort2": flWorkFWCtrlDLRPort2,
       "flWorkFWCtrlDLRBeaconInterval": flWorkFWCtrlDLRBeaconInterval,
       "flWorkFWCtrlDLRBeaconTimeout": flWorkFWCtrlDLRBeaconTimeout,
       "flWorkFWCtrlDLRSupervisorPrecedence": flWorkFWCtrlDLRSupervisorPrecedence,
       "flWorkFWCtrlDLRVlanId": flWorkFWCtrlDLRVlanId,
       "flWorkFWCtrlDLRRingStatus": flWorkFWCtrlDLRRingStatus,
       "flWorkFWCtrlDLRDeviceStatus": flWorkFWCtrlDLRDeviceStatus,
       "flWorkFWCtrlDLRRingFaultCounter": flWorkFWCtrlDLRRingFaultCounter,
       "flWorkFWCtrlDLRRingFaultCntClear": flWorkFWCtrlDLRRingFaultCntClear,
       "flWorkFWCtrlDLRActiveSupervisorIP": flWorkFWCtrlDLRActiveSupervisorIP,
       "flWorkFWCtrlDLRActiveSupervisorMAC": flWorkFWCtrlDLRActiveSupervisorMAC,
       "flWorkFWCtrlDLRLastNodePort1IP": flWorkFWCtrlDLRLastNodePort1IP,
       "flWorkFWCtrlDLRLastNodePort1MAC": flWorkFWCtrlDLRLastNodePort1MAC,
       "flWorkFWCtrlDLRLastNodePort2IP": flWorkFWCtrlDLRLastNodePort2IP,
       "flWorkFWCtrlDLRLastNodePort2MAC": flWorkFWCtrlDLRLastNodePort2MAC,
       "flWorkFWCtrlDLRRapidFaultClear": flWorkFWCtrlDLRRapidFaultClear,
       "flWorkFWCtrlDLRActivePrecedence": flWorkFWCtrlDLRActivePrecedence,
       "flWorkFWCtrlDLRVerifyFaultLocation": flWorkFWCtrlDLRVerifyFaultLocation,
       "flWorkFWCtrlDLRRestartSignOn": flWorkFWCtrlDLRRestartSignOn,
       "flWorkFWCtrlDLRNodeTable": flWorkFWCtrlDLRNodeTable,
       "flWorkFWCtrlDLRNodeEntry": flWorkFWCtrlDLRNodeEntry,
       "flWorkFWCtrlDLRNodeIdx": flWorkFWCtrlDLRNodeIdx,
       "flWorkFWCtrlDLRNodeIP": flWorkFWCtrlDLRNodeIP,
       "flWorkFWCtrlDLRNodeMAC": flWorkFWCtrlDLRNodeMAC,
       "flWorkFWCtrlFileTransfer": flWorkFWCtrlFileTransfer,
       "flWorkFWCtrlFileTransferTftpIPAddr": flWorkFWCtrlFileTransferTftpIPAddr,
       "flWorkFWCtrlFileTransferTftpVapID": flWorkFWCtrlFileTransferTftpVapID,
       "flWorkFWCtrlFileTransferTftpProfileID": flWorkFWCtrlFileTransferTftpProfileID,
       "flWorkFWCtrlFileTransferTftpFileType": flWorkFWCtrlFileTransferTftpFileType,
       "flWorkFWCtrlFileTransferTftpFile": flWorkFWCtrlFileTransferTftpFile,
       "flWorkFWCtrlFileTransferStatus": flWorkFWCtrlFileTransferStatus,
       "flWorkFWCtrlFileTransferExecute": flWorkFWCtrlFileTransferExecute,
       "flWorkFWCtrlDiag": flWorkFWCtrlDiag,
       "flWorkFWCtrlDiagSurveillance": flWorkFWCtrlDiagSurveillance,
       "flWorkFWCtrlDiagSurveillanceCrcMonitoringTable": flWorkFWCtrlDiagSurveillanceCrcMonitoringTable,
       "flWorkFWCtrlDiagSurveillanceCrcMonitoringEntry": flWorkFWCtrlDiagSurveillanceCrcMonitoringEntry,
       "flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex": flWorkFWCtrlDiagSurveillanceCrcMonitoringPortIndex,
       "flWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak": flWorkFWCtrlDiagSurveillanceCrcMonitoringProportionPeak,
       "flWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus": flWorkFWCtrlDiagSurveillanceCrcMonitoringPortStatus,
       "flWorkFWCtrlDiagSurveillanceCrcMonitoringWarningThreshold": flWorkFWCtrlDiagSurveillanceCrcMonitoringWarningThreshold,
       "flWorkFWCtrlDiagSurveillanceCrcMonitoringCriticalThreshold": flWorkFWCtrlDiagSurveillanceCrcMonitoringCriticalThreshold,
       "flWorkFWCtrlDiagSurveillanceResetCrcValues": flWorkFWCtrlDiagSurveillanceResetCrcValues,
       "flWorkFWCtrlDiagSnapshot": flWorkFWCtrlDiagSnapshot,
       "flWorkFWCtrlDiagSnapshotTrigger": flWorkFWCtrlDiagSnapshotTrigger,
       "flWorkFWCtrlDiagSnapshotStatus": flWorkFWCtrlDiagSnapshotStatus,
       "flWorkFWCtrlDiagSnapshotTimeStamp": flWorkFWCtrlDiagSnapshotTimeStamp,
       "flWorkFWCtrlDiagSyslog": flWorkFWCtrlDiagSyslog,
       "flWorkFWCtrlDiagSyslogEnable": flWorkFWCtrlDiagSyslogEnable,
       "flWorkFWCtrlDiagSyslogServTable": flWorkFWCtrlDiagSyslogServTable,
       "flWorkFWCtrlDiagSyslogServEntry": flWorkFWCtrlDiagSyslogServEntry,
       "flWorkFWCtrlDiagSyslogServIndex": flWorkFWCtrlDiagSyslogServIndex,
       "flWorkFWCtrlDiagSyslogServIP": flWorkFWCtrlDiagSyslogServIP,
       "flWorkFWCtrlDiagSyslogServPort": flWorkFWCtrlDiagSyslogServPort,
       "flWorkFWCtrlDiagSyslogServName": flWorkFWCtrlDiagSyslogServName,
       "flWorkFWCtrlDiagSyslogTestMsg": flWorkFWCtrlDiagSyslogTestMsg,
       "flWorkFWCtrlDiagSyslogMsgGroupTable": flWorkFWCtrlDiagSyslogMsgGroupTable,
       "flWorkFWCtrlDiagSyslogMsgGroupEntry": flWorkFWCtrlDiagSyslogMsgGroupEntry,
       "flWorkFWCtrlDiagSyslogMsgGroupIndex": flWorkFWCtrlDiagSyslogMsgGroupIndex,
       "flWorkFWCtrlDiagSyslogMsgGroupName": flWorkFWCtrlDiagSyslogMsgGroupName,
       "flWorkFWCtrlDiagSyslogMsgGroupState": flWorkFWCtrlDiagSyslogMsgGroupState,
       "flSwitch": flSwitch,
       "flSwitchCtrl": flSwitchCtrl,
       "flSwitchCtrlSpanTree": flSwitchCtrlSpanTree,
       "flSwitchCtrlRedundancy": flSwitchCtrlRedundancy,
       "flSwitchCtrlMulticast": flSwitchCtrlMulticast,
       "flSwitchCtrlVlan": flSwitchCtrlVlan,
       "flSwitchCtrlVlanTagMode": flSwitchCtrlVlanTagMode,
       "flSwitchCtrlVlanTagStatus": flSwitchCtrlVlanTagStatus,
       "flSwitchCtrlLldp": flSwitchCtrlLldp,
       "flSwitchCtrlRSTPLargeTreeSupport": flSwitchCtrlRSTPLargeTreeSupport,
       "flSwitchCtrlMacHashMode": flSwitchCtrlMacHashMode,
       "flSwitchCtrlDhcpRelayAgentUi": flSwitchCtrlDhcpRelayAgentUi,
       "flSwitchCtrlMacTableErase": flSwitchCtrlMacTableErase,
       "flSwitchCtrlRmonHistory": flSwitchCtrlRmonHistory,
       "flSwitchCtrlLldpFlooding": flSwitchCtrlLldpFlooding,
       "flSwitchCtrlQosProfile": flSwitchCtrlQosProfile,
       "flSwitchPortMirr": flSwitchPortMirr,
       "flSwitchPortMirrDestinationPort": flSwitchPortMirrDestinationPort,
       "flSwitchPortMirrSourcePort": flSwitchPortMirrSourcePort,
       "flSwitchPortMirrStatus": flSwitchPortMirrStatus,
       "flSwitchPortMirrIngressSourcePort": flSwitchPortMirrIngressSourcePort,
       "flSwitchPortMirrEgressSourcePort": flSwitchPortMirrEgressSourcePort,
       "flSwitchIgmp": flSwitchIgmp,
       "flSwitchIgmpSnoop": flSwitchIgmpSnoop,
       "flSwitchIgmpSnoopEnable": flSwitchIgmpSnoopEnable,
       "flSwitchIgmpSnoopAging": flSwitchIgmpSnoopAging,
       "flSwitchIgmpSnoopTable": flSwitchIgmpSnoopTable,
       "flSwitchIgmpSnoopEntry": flSwitchIgmpSnoopEntry,
       "flSwitchIgmpSnoopEgressPorts": flSwitchIgmpSnoopEgressPorts,
       "flSwitchIgmpSnoopExtended": flSwitchIgmpSnoopExtended,
       "flSwitchBlockUnknownMulticastAtQuerier": flSwitchBlockUnknownMulticastAtQuerier,
       "flSwitchForwardUnknownMulticastToQuerier": flSwitchForwardUnknownMulticastToQuerier,
       "flSwitchIGMPAutoQueryPort": flSwitchIGMPAutoQueryPort,
       "flSwitchIGMPAutoQueryPortsClear": flSwitchIGMPAutoQueryPortsClear,
       "flSwitchIGMPStaticQueryPorts": flSwitchIGMPStaticQueryPorts,
       "flSwitchIgmpQuery": flSwitchIgmpQuery,
       "flSwitchIgmpQueryTable": flSwitchIgmpQueryTable,
       "flSwitchIgmpQueryEntry": flSwitchIgmpQueryEntry,
       "flSwitchIgmpQueryPorts": flSwitchIgmpQueryPorts,
       "flSwitchIgmpQueryEnable": flSwitchIgmpQueryEnable,
       "flSwitchIgmpQueryInterval": flSwitchIgmpQueryInterval,
       "flSwitchIgmpQueryActiveIP": flSwitchIgmpQueryActiveIP,
       "flSwitchIgmpTablesErase": flSwitchIgmpTablesErase,
       "flSwitchRedundancy": flSwitchRedundancy,
       "flSwitchCtrlRSTPFastRingDetection": flSwitchCtrlRSTPFastRingDetection,
       "flSwitchRSTPRingTable": flSwitchRSTPRingTable,
       "flSwitchRSTPRingEntry": flSwitchRSTPRingEntry,
       "flSwitchRSTPRingIndex": flSwitchRSTPRingIndex,
       "flSwitchRSTPRingMAC": flSwitchRSTPRingMAC,
       "flSwitchRSTPRingBlockPort": flSwitchRSTPRingBlockPort,
       "flSwitchRSTPRingRootPort": flSwitchRSTPRingRootPort,
       "flSwitchRSTPRingDesPort": flSwitchRSTPRingDesPort,
       "flSwitchRSTPRingStatus": flSwitchRSTPRingStatus,
       "flSwitchRSTPRingFailedPort": flSwitchRSTPRingFailedPort,
       "flSwitchRSTPextPortTable": flSwitchRSTPextPortTable,
       "flSwitchRSTPextPortEntry": flSwitchRSTPextPortEntry,
       "flSwitchRSTPextPortNum": flSwitchRSTPextPortNum,
       "flSwitchRSTPextAutoEdge": flSwitchRSTPextAutoEdge,
       "flSwitchRSTPextBPDUFlood": flSwitchRSTPextBPDUFlood,
       "flSwitchRelayAgentDhcp": flSwitchRelayAgentDhcp,
       "flSwitchRelayAgentDhcpCtrl": flSwitchRelayAgentDhcpCtrl,
       "flSwitchRelayAgentDhcpIpAddress": flSwitchRelayAgentDhcpIpAddress,
       "flSwitchRelayAgentDhcpStatus": flSwitchRelayAgentDhcpStatus,
       "flSwitchRelayAgentDhcpRIdType": flSwitchRelayAgentDhcpRIdType,
       "flSwitchRelayAgentDhcpPortTable": flSwitchRelayAgentDhcpPortTable,
       "flSwitchRelayAgentDhcpPortEntry": flSwitchRelayAgentDhcpPortEntry,
       "flSwitchRelayAgentDhcpPortCtrlIndex": flSwitchRelayAgentDhcpPortCtrlIndex,
       "flSwitchRelayAgentDhcpPortCtrlOperation": flSwitchRelayAgentDhcpPortCtrlOperation,
       "flSwitchRateCtrl": flSwitchRateCtrl,
       "flSwitchRateCtrlBroadcast": flSwitchRateCtrlBroadcast,
       "flSwitchRateCtrlMulticast": flSwitchRateCtrlMulticast,
       "flSwitchRateCtrlBitrate": flSwitchRateCtrlBitrate,
       "flSwitchDot3FlowControlMode": flSwitchDot3FlowControlMode,
       "flSwitchBroadcastControlMode": flSwitchBroadcastControlMode,
       "flSwitchBroadcastControlThreshold": flSwitchBroadcastControlThreshold,
       "flSwitchMulticastControlMode": flSwitchMulticastControlMode,
       "flSwitchMulticastControlThreshold": flSwitchMulticastControlThreshold,
       "flSwitchUnicastControlMode": flSwitchUnicastControlMode,
       "flSwitchUnicastControlThreshold": flSwitchUnicastControlThreshold,
       "flSwitchStormCtrlTable": flSwitchStormCtrlTable,
       "flSwitchStormCtrlEntry": flSwitchStormCtrlEntry,
       "flSwitchStormCtrlPortNum": flSwitchStormCtrlPortNum,
       "flSwitchStormCtrlBroadcast": flSwitchStormCtrlBroadcast,
       "flSwitchStormCtrlMulticast": flSwitchStormCtrlMulticast,
       "flSwitchStormCtrlUnicast": flSwitchStormCtrlUnicast,
       "flSwitchStormCtrlThreshold": flSwitchStormCtrlThreshold,
       "flSwitchStormCtrlThresholdUnicast": flSwitchStormCtrlThresholdUnicast,
       "flSwitchStormCtrlThresholdBroadcast": flSwitchStormCtrlThresholdBroadcast,
       "flSwitchStormCtrlThresholdMulticast": flSwitchStormCtrlThresholdMulticast,
       "flSwitchStormCtrlBandwidthUnicast": flSwitchStormCtrlBandwidthUnicast,
       "flSwitchStormCtrlBandwidthBroadcast": flSwitchStormCtrlBandwidthBroadcast,
       "flSwitchStormCtrlBandwidthMulticast": flSwitchStormCtrlBandwidthMulticast,
       "flSwitchStormCtrlFrameLimitUnicast": flSwitchStormCtrlFrameLimitUnicast,
       "flSwitchStormCtrlFrameLimitBroadcast": flSwitchStormCtrlFrameLimitBroadcast,
       "flSwitchStormCtrlFrameLimitMulticast": flSwitchStormCtrlFrameLimitMulticast,
       "flSwitchTrafficShaping": flSwitchTrafficShaping,
       "flSwitchTrafficShapingTable": flSwitchTrafficShapingTable,
       "flSwitchTrafficShapingEntry": flSwitchTrafficShapingEntry,
       "flSwitchTrafficShapingIntfIndex": flSwitchTrafficShapingIntfIndex,
       "flSwitchTrafficShapingIntfRate": flSwitchTrafficShapingIntfRate,
       "flSwitchLagConfig": flSwitchLagConfig,
       "flSwitchLagCreate": flSwitchLagCreate,
       "flSwitchLagSummaryTable": flSwitchLagSummaryTable,
       "flSwitchLagSummaryEntry": flSwitchLagSummaryEntry,
       "flSwitchLagIndex": flSwitchLagIndex,
       "flSwitchLagName": flSwitchLagName,
       "flSwitchLagLinkTrap": flSwitchLagLinkTrap,
       "flSwitchLagAdminMode": flSwitchLagAdminMode,
       "flSwitchLagStpMode": flSwitchLagStpMode,
       "flSwitchLagAddPort": flSwitchLagAddPort,
       "flSwitchLagDeletePort": flSwitchLagDeletePort,
       "flSwitchLagStatus": flSwitchLagStatus,
       "flSwitchLagType": flSwitchLagType,
       "flSwitchLagStaticCapability": flSwitchLagStaticCapability,
       "flSwitchLagHashOption": flSwitchLagHashOption,
       "flSwitchLagMaxFrameSize": flSwitchLagMaxFrameSize,
       "flSwitchLagJumboFrame": flSwitchLagJumboFrame,
       "flSwitchLagLinkStatus": flSwitchLagLinkStatus,
       "flSwitchLagMode": flSwitchLagMode,
       "flSwitchLagConfigTable": flSwitchLagConfigTable,
       "flSwitchLagConfigEntry": flSwitchLagConfigEntry,
       "flSwitchLagConfigIndex": flSwitchLagConfigIndex,
       "flSwitchLagConfigIfIndex": flSwitchLagConfigIfIndex,
       "flSwitchLagConfigPortSpeed": flSwitchLagConfigPortSpeed,
       "flSwitchLagConfigPortStatus": flSwitchLagConfigPortStatus,
       "flSwitchLagGlobalHashOption": flSwitchLagGlobalHashOption,
       "flSwitchDhcpServerConfig": flSwitchDhcpServerConfig,
       "flSwitchDhcpServerCtrl": flSwitchDhcpServerCtrl,
       "flSwitchDhcpServerStartAddress": flSwitchDhcpServerStartAddress,
       "flSwitchDhcpServerEndAddress": flSwitchDhcpServerEndAddress,
       "flSwitchDhcpServerSubnetmask": flSwitchDhcpServerSubnetmask,
       "flSwitchDhcpServerGatewayAddress": flSwitchDhcpServerGatewayAddress,
       "flSwitchDhcpServerDnsAddress": flSwitchDhcpServerDnsAddress,
       "flSwitchDhcpServerLeaseTime": flSwitchDhcpServerLeaseTime,
       "flSwitchDhcpServerStatus": flSwitchDhcpServerStatus,
       "flSwitchDhcpServerApply": flSwitchDhcpServerApply,
       "flSwitchDhcpServerAddressPoolSize": flSwitchDhcpServerAddressPoolSize,
       "flSwitchDhcpServerAcceptBootp": flSwitchDhcpServerAcceptBootp,
       "flSwitchDhcpServerRunning": flSwitchDhcpServerRunning,
       "flSwitchDhcpPortLocalService": flSwitchDhcpPortLocalService,
       "flSwitchDhcpPortLocalTable": flSwitchDhcpPortLocalTable,
       "flSwitchDhcpPortLocalEntry": flSwitchDhcpPortLocalEntry,
       "flSwitchDhcpPortLocalIndex": flSwitchDhcpPortLocalIndex,
       "flSwitchDhcpPortLocalOperation": flSwitchDhcpPortLocalOperation,
       "flSwitchDhcpPortLocalLeaseIP": flSwitchDhcpPortLocalLeaseIP,
       "flSwitchDhcpPortLocalNetmask": flSwitchDhcpPortLocalNetmask,
       "flSwitchDhcpPortLocalGateway": flSwitchDhcpPortLocalGateway,
       "flSwitchDhcpPortLocalDns": flSwitchDhcpPortLocalDns,
       "flSwitchDhcpPortLocalClear": flSwitchDhcpPortLocalClear,
       "flSwitchDhcpCurrentLeases": flSwitchDhcpCurrentLeases,
       "flSwitchDhcpCurrentLeaseTable": flSwitchDhcpCurrentLeaseTable,
       "flSwitchDhcpCurrentLeaseEntry": flSwitchDhcpCurrentLeaseEntry,
       "flSwitchDhcpCurrentLeaseIP": flSwitchDhcpCurrentLeaseIP,
       "flSwitchDhcpCurrentLeaseClientID": flSwitchDhcpCurrentLeaseClientID,
       "flSwitchDhcpCurrentLeaseSystemUpTime": flSwitchDhcpCurrentLeaseSystemUpTime,
       "flSwitchDhcpCurrentLeaseTime": flSwitchDhcpCurrentLeaseTime,
       "flSwitchDhcpCurrentLeaseDate": flSwitchDhcpCurrentLeaseDate,
       "flSwitchDhcpCurrentLeaseSeconds": flSwitchDhcpCurrentLeaseSeconds,
       "flSwitchDhcpCurrentLeaseStatus": flSwitchDhcpCurrentLeaseStatus,
       "flSwitchDhcpCurrentLeaseLocalPort": flSwitchDhcpCurrentLeaseLocalPort,
       "flSwitchDhcpCurrentLeasesRelease": flSwitchDhcpCurrentLeasesRelease,
       "flSwitchDhcpStaticBinding": flSwitchDhcpStaticBinding,
       "flSwitchDhcpStaticBindingTable": flSwitchDhcpStaticBindingTable,
       "flSwitchDhcpStaticBindingEntry": flSwitchDhcpStaticBindingEntry,
       "flSwitchDhcpStaticBindingIP": flSwitchDhcpStaticBindingIP,
       "flSwitchDhcpStaticBindingClientID": flSwitchDhcpStaticBindingClientID,
       "flSwitchDhcpStaticBindingClear": flSwitchDhcpStaticBindingClear,
       "flSwitchDhcpPortServerService": flSwitchDhcpPortServerService,
       "flSwitchDhcpPortServerTable": flSwitchDhcpPortServerTable,
       "flSwitchDhcpPortServerEntry": flSwitchDhcpPortServerEntry,
       "flSwitchDhcpPortServerIndex": flSwitchDhcpPortServerIndex,
       "flSwitchDhcpPortServerOperation": flSwitchDhcpPortServerOperation,
       "flSwitchDhcpPortServerStartAddress": flSwitchDhcpPortServerStartAddress,
       "flSwitchDhcpPortServerAddressPoolSize": flSwitchDhcpPortServerAddressPoolSize,
       "flSwitchDhcpPortServerSubnetmask": flSwitchDhcpPortServerSubnetmask,
       "flSwitchDhcpPortServerGatewayAddress": flSwitchDhcpPortServerGatewayAddress,
       "flSwitchDhcpPortServerDnsAddress": flSwitchDhcpPortServerDnsAddress,
       "flSwitchDhcpPortServerLeaseTime": flSwitchDhcpPortServerLeaseTime,
       "flSwitchDiffServConfig": flSwitchDiffServConfig,
       "flSwitchDiffServEnable": flSwitchDiffServEnable,
       "flSwitchDiffServConfigTable": flSwitchDiffServConfigTable,
       "flSwitchDiffServConfigEntry": flSwitchDiffServConfigEntry,
       "flSwitchDiffServCSIndex": flSwitchDiffServCSIndex,
       "flSwitchDiffServCSName": flSwitchDiffServCSName,
       "flSwitchDiffServCriType": flSwitchDiffServCriType,
       "flSwitchDiffServCriEtypeValue": flSwitchDiffServCriEtypeValue,
       "flSwitchDiffServCriEtypeValueCustom": flSwitchDiffServCriEtypeValueCustom,
       "flSwitchDiffServCriIpTosBits": flSwitchDiffServCriIpTosBits,
       "flSwitchDiffServCriIpTosMask": flSwitchDiffServCriIpTosMask,
       "flSwitchDiffServCriIpPrecedence": flSwitchDiffServCriIpPrecedence,
       "flSwitchDiffServServiceType": flSwitchDiffServServiceType,
       "flSwitchDiffServServiceAssignQueueID": flSwitchDiffServServiceAssignQueueID,
       "flSwitchDiffServIncludedPorts": flSwitchDiffServIncludedPorts,
       "flSwitchDiffServRowStatus": flSwitchDiffServRowStatus,
       "flWorkSecGateway": flWorkSecGateway,
       "flWorkSecurityCtrl": flWorkSecurityCtrl,
       "flWorkSecurityCtrlClientAuth": flWorkSecurityCtrlClientAuth,
       "flWorkSecurityCtrlGenSecurityContext": flWorkSecurityCtrlGenSecurityContext,
       "flWorkTimeSynch": flWorkTimeSynch,
       "flWorkTimeSynchSntp": flWorkTimeSynchSntp,
       "flWorkTimeSynchSntpEnable": flWorkTimeSynchSntpEnable,
       "flWorkTimeSynchSntpMode": flWorkTimeSynchSntpMode,
       "flWorkTimeSynchSntpPollInterval": flWorkTimeSynchSntpPollInterval,
       "flWorkTimeSynchSntpServerIpAddress": flWorkTimeSynchSntpServerIpAddress,
       "flWorkTimeSynchSntpBackupServerIpAddress": flWorkTimeSynchSntpBackupServerIpAddress,
       "flWorkTimeSynchSntpBroadcastIpAddress": flWorkTimeSynchSntpBroadcastIpAddress,
       "flWorkTimeSynchSntpStratum": flWorkTimeSynchSntpStratum,
       "flWorkTimeSynchSntpTime": flWorkTimeSynchSntpTime,
       "flWorkTimeSynchSntpDate": flWorkTimeSynchSntpDate,
       "flWorkTimeSynchSntpSeconds": flWorkTimeSynchSntpSeconds,
       "flWorkTimeSynchSntpFractionalSeconds": flWorkTimeSynchSntpFractionalSeconds,
       "flWorkTimeSynchSntpUtcOffset": flWorkTimeSynchSntpUtcOffset,
       "flWorkTimeSynchSntpServerDesc": flWorkTimeSynchSntpServerDesc,
       "flWorkTimeSynchSntpBackupServerDesc": flWorkTimeSynchSntpBackupServerDesc,
       "flWorkTimeSynchSntpServerName": flWorkTimeSynchSntpServerName,
       "flWorkTimeSynchSntpBackupServerName": flWorkTimeSynchSntpBackupServerName,
       "flWorkTimeSynchRTC": flWorkTimeSynchRTC,
       "flWorkTimeSynchRTCDateTime": flWorkTimeSynchRTCDateTime,
       "flWorkTimeSynchRTCSeconds": flWorkTimeSynchRTCSeconds,
       "flWorkTimeSynchPTP": flWorkTimeSynchPTP,
       "flWorkTimeSynchPTPPortTable": flWorkTimeSynchPTPPortTable,
       "flWorkTimeSynchPTPPortEntry": flWorkTimeSynchPTPPortEntry,
       "flWorkTimeSynchPTPPortIndex": flWorkTimeSynchPTPPortIndex,
       "flWorkTimeSynchPTPPortAdminStatus": flWorkTimeSynchPTPPortAdminStatus,
       "flWorkWlan": flWorkWlan,
       "flWorkWlanOpMode": flWorkWlanOpMode,
       "flWorkWlanSetOnlyMode": flWorkWlanSetOnlyMode,
       "flWorkWlanCountry": flWorkWlanCountry,
       "flWorkWlanIf1": flWorkWlanIf1,
       "flWorkWlanIf1Parameter": flWorkWlanIf1Parameter,
       "flWorkWlanIf1ParamState": flWorkWlanIf1ParamState,
       "flWorkWlanIf1ParamOpMode": flWorkWlanIf1ParamOpMode,
       "flWorkWlanIf1ParamSSID": flWorkWlanIf1ParamSSID,
       "flWorkWlanIf1ParamMode": flWorkWlanIf1ParamMode,
       "flWorkWlanIf1ParamChannel": flWorkWlanIf1ParamChannel,
       "flWorkWlanIf1ParamOutdoor": flWorkWlanIf1ParamOutdoor,
       "flWorkWlanIf1AntennaOutput": flWorkWlanIf1AntennaOutput,
       "flWorkWlanIf1OutputPower": flWorkWlanIf1OutputPower,
       "flWorkWlanIf1STBC": flWorkWlanIf1STBC,
       "flWorkWlanIf1Fragmentation": flWorkWlanIf1Fragmentation,
       "flWorkWlanIf1RtsCts": flWorkWlanIf1RtsCts,
       "flWorkWlanIf1LongDistance": flWorkWlanIf1LongDistance,
       "flWorkWlanIf1ScbMacAddress": flWorkWlanIf1ScbMacAddress,
       "flWorkWlanIf1ScbManMacMode": flWorkWlanIf1ScbManMacMode,
       "flWorkWlanIf1IAPP": flWorkWlanIf1IAPP,
       "flWorkWlanIf1MachineAdmin": flWorkWlanIf1MachineAdmin,
       "flWorkWlanIf1MachineAdminSSID": flWorkWlanIf1MachineAdminSSID,
       "flWorkWlanIf1MachineAdminPsk": flWorkWlanIf1MachineAdminPsk,
       "flWorkWlanIf1MachineAdminIp": flWorkWlanIf1MachineAdminIp,
       "flWorkWlanIf1Security": flWorkWlanIf1Security,
       "flWorkWlanIf1SecMode": flWorkWlanIf1SecMode,
       "flWorkWlanIf1SecWpaEncryptionAlgorithm": flWorkWlanIf1SecWpaEncryptionAlgorithm,
       "flWorkWlanIf1SecWpaPsk": flWorkWlanIf1SecWpaPsk,
       "flWorkWlanIf1SecWepAuthType": flWorkWlanIf1SecWepAuthType,
       "flWorkWlanIf1SecWepKeyEncoding": flWorkWlanIf1SecWepKeyEncoding,
       "flWorkWlanIf1SecWepKey": flWorkWlanIf1SecWepKey,
       "flWorkWlanIf1FastRoaming": flWorkWlanIf1FastRoaming,
       "flWorkWlanIf1FastRoamingTable": flWorkWlanIf1FastRoamingTable,
       "flWorkWlanIf1FastRoamingEntry": flWorkWlanIf1FastRoamingEntry,
       "flWorkWlanIf1FastRoamingEntryIdx": flWorkWlanIf1FastRoamingEntryIdx,
       "flWorkWlanIf1FastRoamingEntryThreshold": flWorkWlanIf1FastRoamingEntryThreshold,
       "flWorkWlanIf1FastRoamingEntryChannel": flWorkWlanIf1FastRoamingEntryChannel,
       "flWorkWlanIf1FastRoamingEntryAddress": flWorkWlanIf1FastRoamingEntryAddress,
       "flWorkWlanIf1FastRoamingEnabled": flWorkWlanIf1FastRoamingEnabled,
       "flWorkWlanIf1FastRoamToAP": flWorkWlanIf1FastRoamToAP,
       "flWorkWlanIf1Mcast": flWorkWlanIf1Mcast,
       "flWorkWlanIf1McastEnhance": flWorkWlanIf1McastEnhance,
       "flWorkWlanIf1McastDrop": flWorkWlanIf1McastDrop,
       "flWorkWlanIf1McastAutoAdd": flWorkWlanIf1McastAutoAdd,
       "flWorkWlanIf1McastAdvSnooping": flWorkWlanIf1McastAdvSnooping,
       "flWorkWlanIf1McastTable": flWorkWlanIf1McastTable,
       "flWorkWlanIf1McastEntry": flWorkWlanIf1McastEntry,
       "flWorkWlanIf1McastTableEntryIdx": flWorkWlanIf1McastTableEntryIdx,
       "flWorkWlanIf1McastTableEntryGroup": flWorkWlanIf1McastTableEntryGroup,
       "flWorkWlanIf1McastTableEntryMember": flWorkWlanIf1McastTableEntryMember,
       "flWorkWlanIf1McastTableEntrySta": flWorkWlanIf1McastTableEntrySta,
       "flWorkWlanIf1McastDenyConfig": flWorkWlanIf1McastDenyConfig,
       "flWorkWlanIf1McastDenyCreate": flWorkWlanIf1McastDenyCreate,
       "flWorkWlanIf1McastDenyTable": flWorkWlanIf1McastDenyTable,
       "flWorkWlanIf1McastDenyEntry": flWorkWlanIf1McastDenyEntry,
       "flWorkWlanIf1McastDenyTableEntryIdx": flWorkWlanIf1McastDenyTableEntryIdx,
       "flWorkWlanIf1McastDenyTableEntryGroup": flWorkWlanIf1McastDenyTableEntryGroup,
       "flWorkWlanIf1McastDenyTableEntryStatus": flWorkWlanIf1McastDenyTableEntryStatus,
       "flWorkWlanIf1StationsTable": flWorkWlanIf1StationsTable,
       "flWorkWlanIf1StationsEntry": flWorkWlanIf1StationsEntry,
       "flWorkWlanIf1StationEntryIdx": flWorkWlanIf1StationEntryIdx,
       "flWorkWlanIf1StationEntrySNR": flWorkWlanIf1StationEntrySNR,
       "flWorkWlanIf1StationEntryRate": flWorkWlanIf1StationEntryRate,
       "flWorkWlanIf1StationEntryPower": flWorkWlanIf1StationEntryPower,
       "flWorkWlanIf1StationEntryAddress": flWorkWlanIf1StationEntryAddress,
       "flWorkWlanIf1VisibleAccessPointTable": flWorkWlanIf1VisibleAccessPointTable,
       "flWorkWlanIf1VisibleAccessPointEntry": flWorkWlanIf1VisibleAccessPointEntry,
       "flWorkWlanIf1VisibleAccessPointEntryIdx": flWorkWlanIf1VisibleAccessPointEntryIdx,
       "flWorkWlanIf1VisibleAccessPointEntrySNR": flWorkWlanIf1VisibleAccessPointEntrySNR,
       "flWorkWlanIf1VisibleAccessPointEntryChannel": flWorkWlanIf1VisibleAccessPointEntryChannel,
       "flWorkWlanIf1VisibleAccessPointEntryPower": flWorkWlanIf1VisibleAccessPointEntryPower,
       "flWorkWlanIf1VisibleAccessPointEntrySSID": flWorkWlanIf1VisibleAccessPointEntrySSID,
       "flWorkWlanIf1VisibleAccessPointEntrySecurity": flWorkWlanIf1VisibleAccessPointEntrySecurity,
       "flWorkWlanIf1VisibleAccessPointEntryAddress": flWorkWlanIf1VisibleAccessPointEntryAddress,
       "flWorkWlanIf1VisibleAccessPointEntryConnected": flWorkWlanIf1VisibleAccessPointEntryConnected,
       "flWorkWlanIf1VisibleAccessPointEntryRSSI": flWorkWlanIf1VisibleAccessPointEntryRSSI,
       "flWorkWlanIf1VisibleAccessPointEntryNoise": flWorkWlanIf1VisibleAccessPointEntryNoise,
       "flWorkWlanIf2": flWorkWlanIf2,
       "flWorkWlanIf2Parameter": flWorkWlanIf2Parameter,
       "flWorkWlanIf2ParamState": flWorkWlanIf2ParamState,
       "flWorkWlanIf2ParamOpMode": flWorkWlanIf2ParamOpMode,
       "flWorkWlanIf2ParamSSID": flWorkWlanIf2ParamSSID,
       "flWorkWlanIf2ParamMode": flWorkWlanIf2ParamMode,
       "flWorkWlanIf2ParamChannel": flWorkWlanIf2ParamChannel,
       "flWorkWlanIf2ParamOutdoor": flWorkWlanIf2ParamOutdoor,
       "flWorkWlanIf2AntennaOutput": flWorkWlanIf2AntennaOutput,
       "flWorkWlanIf2OutputPower": flWorkWlanIf2OutputPower,
       "flWorkWlanIf2STBC": flWorkWlanIf2STBC,
       "flWorkWlanIf2Fragmentation": flWorkWlanIf2Fragmentation,
       "flWorkWlanIf2RtsCts": flWorkWlanIf2RtsCts,
       "flWorkWlanIf2LongDistance": flWorkWlanIf2LongDistance,
       "flWorkWlanIf2ScbMacAddress": flWorkWlanIf2ScbMacAddress,
       "flWorkWlanIf2ScbManMacMode": flWorkWlanIf2ScbManMacMode,
       "flWorkWlanIf2IAPP": flWorkWlanIf2IAPP,
       "flWorkWlanIf2MachineAdmin": flWorkWlanIf2MachineAdmin,
       "flWorkWlanIf2MachineAdminSSID": flWorkWlanIf2MachineAdminSSID,
       "flWorkWlanIf2MachineAdminPsk": flWorkWlanIf2MachineAdminPsk,
       "flWorkWlanIf2MachineAdminIp": flWorkWlanIf2MachineAdminIp,
       "flWorkWlanIf2Security": flWorkWlanIf2Security,
       "flWorkWlanIf2SecMode": flWorkWlanIf2SecMode,
       "flWorkWlanIf2SecWpaEncryptionAlgorithm": flWorkWlanIf2SecWpaEncryptionAlgorithm,
       "flWorkWlanIf2SecWpaPsk": flWorkWlanIf2SecWpaPsk,
       "flWorkWlanIf2SecWepAuthType": flWorkWlanIf2SecWepAuthType,
       "flWorkWlanIf2SecWepKeyEncoding": flWorkWlanIf2SecWepKeyEncoding,
       "flWorkWlanIf2SecWepKey": flWorkWlanIf2SecWepKey,
       "flWorkWlanMacFilter": flWorkWlanMacFilter,
       "flWorkWlanMacFilterTable": flWorkWlanMacFilterTable,
       "flWorkWlanMacFilterEntry": flWorkWlanMacFilterEntry,
       "flWorkWlanMacEntryIdx": flWorkWlanMacEntryIdx,
       "flWorkWlanMacEntryInterfaceName": flWorkWlanMacEntryInterfaceName,
       "flWorkWlanMacEntryAction": flWorkWlanMacEntryAction,
       "flWorkWlanMacEntryAddress": flWorkWlanMacEntryAddress,
       "flWorkWlanMacPolicyIf1": flWorkWlanMacPolicyIf1,
       "flWorkWlanMacPolicyIf2": flWorkWlanMacPolicyIf2,
       "flWorkWlanMacFilterSyslog": flWorkWlanMacFilterSyslog,
       "flWorkRouting": flWorkRouting,
       "flWorkRoutingIp": flWorkRoutingIp,
       "flWorkRoutingIpRoutingMode": flWorkRoutingIpRoutingMode,
       "flWorkRoutingIpInterfaceTable": flWorkRoutingIpInterfaceTable,
       "flWorkRoutingIpInterfaceEntry": flWorkRoutingIpInterfaceEntry,
       "flWorkRoutingIpInterfaceIfIndex": flWorkRoutingIpInterfaceIfIndex,
       "flWorkRoutingIpInterfaceIpAddress": flWorkRoutingIpInterfaceIpAddress,
       "flWorkRoutingIpInterfaceNetMask": flWorkRoutingIpInterfaceNetMask,
       "flWorkRoutingIpInterfaceClearIp": flWorkRoutingIpInterfaceClearIp,
       "flWorkRoutingIpInterfaceRoutingMode": flWorkRoutingIpInterfaceRoutingMode,
       "flWorkRoutingIpInterfaceProxyARPMode": flWorkRoutingIpInterfaceProxyARPMode,
       "flWorkRoutingIpInterfaceMtuValue": flWorkRoutingIpInterfaceMtuValue,
       "flWorkRoutingIpInterfaceBandwidth": flWorkRoutingIpInterfaceBandwidth,
       "flWorkRoutingIpInterfaceUnnumberedIfIndex": flWorkRoutingIpInterfaceUnnumberedIfIndex,
       "flWorkRoutingIpInterfaceIcmpUnreachables": flWorkRoutingIpInterfaceIcmpUnreachables,
       "flWorkRoutingIpInterfaceIcmpRedirects": flWorkRoutingIpInterfaceIcmpRedirects,
       "flWorkRoutingIpInterfaceManagementAccess": flWorkRoutingIpInterfaceManagementAccess,
       "flWorkRoutingIpInterfaceAssignMode": flWorkRoutingIpInterfaceAssignMode,
       "flWorkRoutingIpInterfaceMapIdx2IfTable": flWorkRoutingIpInterfaceMapIdx2IfTable,
       "flWorkRoutingIpRouterDiscoveryTable": flWorkRoutingIpRouterDiscoveryTable,
       "flWorkRoutingIpRouterDiscoveryEntry": flWorkRoutingIpRouterDiscoveryEntry,
       "flWorkRoutingIpRouterDiscoveryIfIndex": flWorkRoutingIpRouterDiscoveryIfIndex,
       "flWorkRoutingIpRouterDiscoveryAdvertiseMode": flWorkRoutingIpRouterDiscoveryAdvertiseMode,
       "flWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval": flWorkRoutingIpRouterDiscoveryMaxAdvertisementInterval,
       "flWorkRoutingIpRouterDiscoveryMinAdvertisementInterval": flWorkRoutingIpRouterDiscoveryMinAdvertisementInterval,
       "flWorkRoutingIpRouterDiscoveryAdvertisementLifetime": flWorkRoutingIpRouterDiscoveryAdvertisementLifetime,
       "flWorkRoutingIpRouterDiscoveryPreferenceLevel": flWorkRoutingIpRouterDiscoveryPreferenceLevel,
       "flWorkRoutingIpRouterDiscoveryAdvertisementAddress": flWorkRoutingIpRouterDiscoveryAdvertisementAddress,
       "flWorkRoutingIpVlanTable": flWorkRoutingIpVlanTable,
       "flWorkRoutingIpVlanEntry": flWorkRoutingIpVlanEntry,
       "flWorkRoutingIpVlanId": flWorkRoutingIpVlanId,
       "flWorkRoutingIpVlanIfIndex": flWorkRoutingIpVlanIfIndex,
       "flWorkRoutingIpVlanRoutingStatus": flWorkRoutingIpVlanRoutingStatus,
       "flWorkRoutingSecondaryAddressTable": flWorkRoutingSecondaryAddressTable,
       "flWorkRoutingSecondaryAddressEntry": flWorkRoutingSecondaryAddressEntry,
       "flWorkRoutingSecondaryIpAddress": flWorkRoutingSecondaryIpAddress,
       "flWorkRoutingSecondaryNetMask": flWorkRoutingSecondaryNetMask,
       "flWorkRoutingSecondaryStatus": flWorkRoutingSecondaryStatus,
       "flWorkRoutingHelperAddressTable": flWorkRoutingHelperAddressTable,
       "flWorkRoutingHelperAddressEntry": flWorkRoutingHelperAddressEntry,
       "flWorkRoutingHelperIpAddress": flWorkRoutingHelperIpAddress,
       "flWorkRoutingHelperStatus": flWorkRoutingHelperStatus,
       "flWorkRoutingIpIcmpControl": flWorkRoutingIpIcmpControl,
       "flWorkRoutingIpIcmpEchoReplyMode": flWorkRoutingIpIcmpEchoReplyMode,
       "flWorkRoutingIpIcmpRedirectsMode": flWorkRoutingIpIcmpRedirectsMode,
       "flWorkRoutingIpIcmpRateLimitInterval": flWorkRoutingIpIcmpRateLimitInterval,
       "flWorkRoutingIpIcmpRateLimitBurstSize": flWorkRoutingIpIcmpRateLimitBurstSize,
       "flWorkRoutingStaticRouteTable": flWorkRoutingStaticRouteTable,
       "flWorkRoutingStaticRouteEntry": flWorkRoutingStaticRouteEntry,
       "flWorkRoutingStaticRouteTableIndex": flWorkRoutingStaticRouteTableIndex,
       "flWorkRoutingStaticRouteTableDestNetwork": flWorkRoutingStaticRouteTableDestNetwork,
       "flWorkRoutingStaticRouteTableDestSubnetMask": flWorkRoutingStaticRouteTableDestSubnetMask,
       "flWorkRoutingStaticRouteTableNextHop": flWorkRoutingStaticRouteTableNextHop,
       "flWorkRoutingStaticRouteTablePreference": flWorkRoutingStaticRouteTablePreference,
       "flWorkRoutingStaticRouteTableActive": flWorkRoutingStaticRouteTableActive,
       "flWorkRoutingStaticRouteTableStatus": flWorkRoutingStaticRouteTableStatus,
       "flWorkRoutingArp": flWorkRoutingArp,
       "flWorkRoutingArpAgeoutTime": flWorkRoutingArpAgeoutTime,
       "flWorkRoutingArpResponseTime": flWorkRoutingArpResponseTime,
       "flWorkRoutingArpMaxRetries": flWorkRoutingArpMaxRetries,
       "flWorkRoutingArpCacheSize": flWorkRoutingArpCacheSize,
       "flWorkRoutingArpDynamicRenew": flWorkRoutingArpDynamicRenew,
       "flWorkRoutingArpTotalEntryCountCurrent": flWorkRoutingArpTotalEntryCountCurrent,
       "flWorkRoutingArpTotalEntryCountPeak": flWorkRoutingArpTotalEntryCountPeak,
       "flWorkRoutingArpStaticEntryCountCurrent": flWorkRoutingArpStaticEntryCountCurrent,
       "flWorkRoutingArpStaticEntryCountMax": flWorkRoutingArpStaticEntryCountMax,
       "flWorkRoutingLocalProxyArpTable": flWorkRoutingLocalProxyArpTable,
       "flWorkRoutingLocalProxyArpEntry": flWorkRoutingLocalProxyArpEntry,
       "flWorkRoutingLocalProxyArpMode": flWorkRoutingLocalProxyArpMode,
       "flWorkRoutingIntfArpTable": flWorkRoutingIntfArpTable,
       "flWorkRoutingIntfArpEntry": flWorkRoutingIntfArpEntry,
       "flWorkRoutingIntfArpIpAddress": flWorkRoutingIntfArpIpAddress,
       "flWorkRoutingIntfArpIfIndex": flWorkRoutingIntfArpIfIndex,
       "flWorkRoutingIntfArpAge": flWorkRoutingIntfArpAge,
       "flWorkRoutingIntfArpMacAddress": flWorkRoutingIntfArpMacAddress,
       "flWorkRoutingIntfArpType": flWorkRoutingIntfArpType,
       "flWorkRoutingIntfArpStatus": flWorkRoutingIntfArpStatus,
       "flWorkRoutingVrrp": flWorkRoutingVrrp,
       "flWorkRoutingVrrpAdminState": flWorkRoutingVrrpAdminState,
       "flWorkRoutingVrrpOperTable": flWorkRoutingVrrpOperTable,
       "flWorkRoutingVrrpOperEntry": flWorkRoutingVrrpOperEntry,
       "flWorkRoutingVrrpOperPriority": flWorkRoutingVrrpOperPriority,
       "flWorkRoutingVrrpTrackIntfTable": flWorkRoutingVrrpTrackIntfTable,
       "flWorkRoutingVrrpTrackIntfEntry": flWorkRoutingVrrpTrackIntfEntry,
       "flWorkRoutingVrrpTrackIntf": flWorkRoutingVrrpTrackIntf,
       "flWorkRoutingVrrpTrackIfPrioDec": flWorkRoutingVrrpTrackIfPrioDec,
       "flWorkRoutingVrrpTrackIfState": flWorkRoutingVrrpTrackIfState,
       "flWorkRoutingVrrpTrackIfStatus": flWorkRoutingVrrpTrackIfStatus,
       "flWorkRoutingVrrpTrackRouteTable": flWorkRoutingVrrpTrackRouteTable,
       "flWorkRoutingVrrpTrackRouteEntry": flWorkRoutingVrrpTrackRouteEntry,
       "flWorkRoutingVrrpTrackRtPfx": flWorkRoutingVrrpTrackRtPfx,
       "flWorkRoutingVrrpTrackRtPfxLen": flWorkRoutingVrrpTrackRtPfxLen,
       "flWorkRoutingVrrpTrackRtPrioDec": flWorkRoutingVrrpTrackRtPrioDec,
       "flWorkRoutingVrrpTrackRtReachable": flWorkRoutingVrrpTrackRtReachable,
       "flWorkRoutingVrrpTrackRtStatus": flWorkRoutingVrrpTrackRtStatus,
       "flWorkRoutingVrrpIcmpEcho": flWorkRoutingVrrpIcmpEcho,
       "flWorkRoutingRip": flWorkRoutingRip,
       "flWorkRoutingRipAdminState": flWorkRoutingRipAdminState,
       "flWorkRoutingRipSplitHorizonMode": flWorkRoutingRipSplitHorizonMode,
       "flWorkRoutingRipAutoSummaryMode": flWorkRoutingRipAutoSummaryMode,
       "flWorkRoutingRipHostRoutesAcceptMode": flWorkRoutingRipHostRoutesAcceptMode,
       "flWorkRoutingRipDefaultMetric": flWorkRoutingRipDefaultMetric,
       "flWorkRoutingRipDefaultMetricConfigured": flWorkRoutingRipDefaultMetricConfigured,
       "flWorkRoutingRipDefaultInfoOriginate": flWorkRoutingRipDefaultInfoOriginate,
       "flWorkRoutingRipRouteRedistTable": flWorkRoutingRipRouteRedistTable,
       "flWorkRoutingRipRouteRedistEntry": flWorkRoutingRipRouteRedistEntry,
       "flWorkRoutingRipRouteRedistSource": flWorkRoutingRipRouteRedistSource,
       "flWorkRoutingRipRouteRedistMode": flWorkRoutingRipRouteRedistMode,
       "flWorkRoutingRipRouteRedistMetric": flWorkRoutingRipRouteRedistMetric,
       "flWorkRoutingRipRouteRedistMetricConfigured": flWorkRoutingRipRouteRedistMetricConfigured,
       "flWorkRoutingRipRouteRedistMatchInternal": flWorkRoutingRipRouteRedistMatchInternal,
       "flWorkRoutingRipRouteRedistMatchExternal1": flWorkRoutingRipRouteRedistMatchExternal1,
       "flWorkRoutingRipRouteRedistMatchExternal2": flWorkRoutingRipRouteRedistMatchExternal2,
       "flWorkRoutingRipRouteRedistMatchNSSAExternal1": flWorkRoutingRipRouteRedistMatchNSSAExternal1,
       "flWorkRoutingRipRouteRedistMatchNSSAExternal2": flWorkRoutingRipRouteRedistMatchNSSAExternal2,
       "flWorkRoutingRipRouteRedistDistList": flWorkRoutingRipRouteRedistDistList,
       "flWorkRoutingRipRouteRedistDistListConfigured": flWorkRoutingRipRouteRedistDistListConfigured,
       "flWorkRoutingRip2IfConfTable": flWorkRoutingRip2IfConfTable,
       "flWorkRoutingRip2IfConfEntry": flWorkRoutingRip2IfConfEntry,
       "flWorkRoutingRip2IfConfAuthKeyId": flWorkRoutingRip2IfConfAuthKeyId,
       "flWorkRoutingOspf": flWorkRoutingOspf,
       "flWorkRoutingOspfDefaultMetric": flWorkRoutingOspfDefaultMetric,
       "flWorkRoutingOspfDefaultMetricConfigured": flWorkRoutingOspfDefaultMetricConfigured,
       "flWorkRoutingOspfDefaultInfoOriginate": flWorkRoutingOspfDefaultInfoOriginate,
       "flWorkRoutingOspfDefaultInfoOriginateAlways": flWorkRoutingOspfDefaultInfoOriginateAlways,
       "flWorkRoutingOspfDefaultInfoOriginateMetric": flWorkRoutingOspfDefaultInfoOriginateMetric,
       "flWorkRoutingOspfDefaultInfoOriginateMetricConfigured": flWorkRoutingOspfDefaultInfoOriginateMetricConfigured,
       "flWorkRoutingOspfDefaultInfoOriginateMetricType": flWorkRoutingOspfDefaultInfoOriginateMetricType,
       "flWorkRoutingOspfRouteRedistTable": flWorkRoutingOspfRouteRedistTable,
       "flWorkRoutingOspfRouteRedistEntry": flWorkRoutingOspfRouteRedistEntry,
       "flWorkRoutingOspfRouteRedistSource": flWorkRoutingOspfRouteRedistSource,
       "flWorkRoutingOspfRouteRedistMode": flWorkRoutingOspfRouteRedistMode,
       "flWorkRoutingOspfRouteRedistMetric": flWorkRoutingOspfRouteRedistMetric,
       "flWorkRoutingOspfRouteRedistMetricConfigured": flWorkRoutingOspfRouteRedistMetricConfigured,
       "flWorkRoutingOspfRouteRedistMetricType": flWorkRoutingOspfRouteRedistMetricType,
       "flWorkRoutingOspfRouteRedistTag": flWorkRoutingOspfRouteRedistTag,
       "flWorkRoutingOspfRouteRedistSubnets": flWorkRoutingOspfRouteRedistSubnets,
       "flWorkRoutingOspfRouteRedistDistList": flWorkRoutingOspfRouteRedistDistList,
       "flWorkRoutingOspfRouteRedistDistListConfigured": flWorkRoutingOspfRouteRedistDistListConfigured,
       "flWorkRoutingOspfIfTable": flWorkRoutingOspfIfTable,
       "flWorkRoutingOspfIfEntry": flWorkRoutingOspfIfEntry,
       "flWorkRoutingOspfIfAuthKeyId": flWorkRoutingOspfIfAuthKeyId,
       "flWorkRoutingOspfIfIpMtuIgnoreFlag": flWorkRoutingOspfIfIpMtuIgnoreFlag,
       "flWorkRoutingOspfIfPassiveMode": flWorkRoutingOspfIfPassiveMode,
       "flWorkRoutingOspfVirtIfTable": flWorkRoutingOspfVirtIfTable,
       "flWorkRoutingOspfVirtIfEntry": flWorkRoutingOspfVirtIfEntry,
       "flWorkRoutingOspfVirtIfAuthKeyId": flWorkRoutingOspfVirtIfAuthKeyId,
       "flWorkRoutingOspfRFC1583CompatibilityMode": flWorkRoutingOspfRFC1583CompatibilityMode,
       "flWorkRoutingOspfSpfDelayTime": flWorkRoutingOspfSpfDelayTime,
       "flWorkRoutingOspfSpfHoldTime": flWorkRoutingOspfSpfHoldTime,
       "flWorkRoutingOspfAutoCostRefBw": flWorkRoutingOspfAutoCostRefBw,
       "flWorkRoutingOspfOpaqueLsaSupport": flWorkRoutingOspfOpaqueLsaSupport,
       "flWorkRoutingOspfAreaOpaqueLsdbTable": flWorkRoutingOspfAreaOpaqueLsdbTable,
       "flWorkRoutingOspfAreaOpaqueLsdbEntry": flWorkRoutingOspfAreaOpaqueLsdbEntry,
       "flWorkRoutingOspfAreaOpaqueLsdbAreaId": flWorkRoutingOspfAreaOpaqueLsdbAreaId,
       "flWorkRoutingOspfAreaOpaqueLsdbType": flWorkRoutingOspfAreaOpaqueLsdbType,
       "flWorkRoutingOspfAreaOpaqueLsdbLsid": flWorkRoutingOspfAreaOpaqueLsdbLsid,
       "flWorkRoutingOspfAreaOpaqueLsdbRouterId": flWorkRoutingOspfAreaOpaqueLsdbRouterId,
       "flWorkRoutingOspfAreaOpaqueLsdbSequence": flWorkRoutingOspfAreaOpaqueLsdbSequence,
       "flWorkRoutingOspfAreaOpaqueLsdbAge": flWorkRoutingOspfAreaOpaqueLsdbAge,
       "flWorkRoutingOspfAreaOpaqueLsdbChecksum": flWorkRoutingOspfAreaOpaqueLsdbChecksum,
       "flWorkRoutingOspfAreaOpaqueLsdbAdvertisement": flWorkRoutingOspfAreaOpaqueLsdbAdvertisement,
       "flWorkRoutingOspfLocalLsdbTable": flWorkRoutingOspfLocalLsdbTable,
       "flWorkRoutingOspfLocalLsdbEntry": flWorkRoutingOspfLocalLsdbEntry,
       "flWorkRoutingOspfLocalLsdbIpAddress": flWorkRoutingOspfLocalLsdbIpAddress,
       "flWorkRoutingOspfLocalLsdbAddressLessIf": flWorkRoutingOspfLocalLsdbAddressLessIf,
       "flWorkRoutingOspfLocalLsdbType": flWorkRoutingOspfLocalLsdbType,
       "flWorkRoutingOspfLocalLsdbLsid": flWorkRoutingOspfLocalLsdbLsid,
       "flWorkRoutingOspfLocalLsdbRouterId": flWorkRoutingOspfLocalLsdbRouterId,
       "flWorkRoutingOspfLocalLsdbSequence": flWorkRoutingOspfLocalLsdbSequence,
       "flWorkRoutingOspfLocalLsdbAge": flWorkRoutingOspfLocalLsdbAge,
       "flWorkRoutingOspfLocalLsdbChecksum": flWorkRoutingOspfLocalLsdbChecksum,
       "flWorkRoutingOspfLocalLsdbAdvertisement": flWorkRoutingOspfLocalLsdbAdvertisement,
       "flWorkRoutingOspfAsLsdbTable": flWorkRoutingOspfAsLsdbTable,
       "flWorkRoutingOspfAsLsdbEntry": flWorkRoutingOspfAsLsdbEntry,
       "flWorkRoutingOspfAsLsdbType": flWorkRoutingOspfAsLsdbType,
       "flWorkRoutingOspfAsLsdbLsid": flWorkRoutingOspfAsLsdbLsid,
       "flWorkRoutingOspfAsLsdbRouterId": flWorkRoutingOspfAsLsdbRouterId,
       "flWorkRoutingOspfAsLsdbSequence": flWorkRoutingOspfAsLsdbSequence,
       "flWorkRoutingOspfAsLsdbAge": flWorkRoutingOspfAsLsdbAge,
       "flWorkRoutingOspfAsLsdbChecksum": flWorkRoutingOspfAsLsdbChecksum,
       "flWorkRoutingOspfAsLsdbAdvertisement": flWorkRoutingOspfAsLsdbAdvertisement,
       "flWorkRoutingOspfDefaultPassiveMode": flWorkRoutingOspfDefaultPassiveMode,
       "flWorkRoutingLoopback": flWorkRoutingLoopback,
       "flWorkRoutingLoopbackTable": flWorkRoutingLoopbackTable,
       "flWorkRoutingLoopbackEntry": flWorkRoutingLoopbackEntry,
       "flWorkRoutingLoopbackID": flWorkRoutingLoopbackID,
       "flWorkRoutingLoopbackIfIndex": flWorkRoutingLoopbackIfIndex,
       "flWorkRoutingLoopbackIPAddress": flWorkRoutingLoopbackIPAddress,
       "flWorkRoutingLoopbackIPSubnet": flWorkRoutingLoopbackIPSubnet,
       "flWorkRoutingLoopbackStatus": flWorkRoutingLoopbackStatus,
       "flWorkRoutingNAT": flWorkRoutingNAT,
       "flWorkRoutingNATIntfCtrl": flWorkRoutingNATIntfCtrl,
       "flWorkRoutingNATIntfCtrlTable": flWorkRoutingNATIntfCtrlTable,
       "flWorkRoutingNATIntfCtrlEntry": flWorkRoutingNATIntfCtrlEntry,
       "flWorkRoutingNATIntfCtrlIntfIndex": flWorkRoutingNATIntfCtrlIntfIndex,
       "flWorkRoutingNATIntfCtrlIntfMode": flWorkRoutingNATIntfCtrlIntfMode,
       "flWorkRoutingNATIntfForwarding": flWorkRoutingNATIntfForwarding,
       "flWorkRoutingNATIntfForwardingTable": flWorkRoutingNATIntfForwardingTable,
       "flWorkRoutingNATIntfForwardingEntry": flWorkRoutingNATIntfForwardingEntry,
       "flWorkRoutingNATIntfForwardingIntfIndex": flWorkRoutingNATIntfForwardingIntfIndex,
       "flWorkRoutingNATIntfForwardingTableIndex": flWorkRoutingNATIntfForwardingTableIndex,
       "flWorkRoutingNATIntfForwardingTableProtocol": flWorkRoutingNATIntfForwardingTableProtocol,
       "flWorkRoutingNATIntfForwardingTableDirection": flWorkRoutingNATIntfForwardingTableDirection,
       "flWorkRoutingNATIntfForwardingTableInboundAddr": flWorkRoutingNATIntfForwardingTableInboundAddr,
       "flWorkRoutingNATIntfForwardingTableInboundPort": flWorkRoutingNATIntfForwardingTableInboundPort,
       "flWorkRoutingNATIntfForwardingTableOutboundAddr": flWorkRoutingNATIntfForwardingTableOutboundAddr,
       "flWorkRoutingNATIntfForwardingTableOutboundPort": flWorkRoutingNATIntfForwardingTableOutboundPort,
       "flWorkRoutingNATIntfForwardingTableActive": flWorkRoutingNATIntfForwardingTableActive,
       "flWorkRoutingNATIntfForwardingTableStatus": flWorkRoutingNATIntfForwardingTableStatus,
       "flWorkRoutingNATIntf1to1": flWorkRoutingNATIntf1to1,
       "flWorkRoutingNATIntf1to1Table": flWorkRoutingNATIntf1to1Table,
       "flWorkRoutingNATIntf1to1Entry": flWorkRoutingNATIntf1to1Entry,
       "flWorkRoutingNATIntf1to1IntfIndex": flWorkRoutingNATIntf1to1IntfIndex,
       "flWorkRoutingNATIntf1to1TableIndex": flWorkRoutingNATIntf1to1TableIndex,
       "flWorkRoutingNATIntf1to1TableExternalNetwork": flWorkRoutingNATIntf1to1TableExternalNetwork,
       "flWorkRoutingNATIntf1to1TableInternalNetwork": flWorkRoutingNATIntf1to1TableInternalNetwork,
       "flWorkRoutingNATIntf1to1TableRange": flWorkRoutingNATIntf1to1TableRange,
       "flWorkRoutingNATIntf1to1TableActive": flWorkRoutingNATIntf1to1TableActive,
       "flWorkRoutingNATIntf1to1TableStatus": flWorkRoutingNATIntf1to1TableStatus,
       "flWorkRoutingNATIntfVirtual": flWorkRoutingNATIntfVirtual,
       "flWorkRoutingNATIntfVirtualTable": flWorkRoutingNATIntfVirtualTable,
       "flWorkRoutingNATIntfVirtualEntry": flWorkRoutingNATIntfVirtualEntry,
       "flWorkRoutingNATIntfVirtualIntfIndex": flWorkRoutingNATIntfVirtualIntfIndex,
       "flWorkRoutingNATIntfVirtualTableIndex": flWorkRoutingNATIntfVirtualTableIndex,
       "flWorkRoutingNATIntfVirtualTableVirtualNetwork": flWorkRoutingNATIntfVirtualTableVirtualNetwork,
       "flWorkRoutingNATIntfVirtualTableInternalNetwork": flWorkRoutingNATIntfVirtualTableInternalNetwork,
       "flWorkRoutingNATIntfVirtualTableRange": flWorkRoutingNATIntfVirtualTableRange,
       "flWorkCip": flWorkCip,
       "flWorkCipInfo": flWorkCipInfo,
       "flWorkCipActiveIOConns": flWorkCipActiveIOConns,
       "flWorkCipActiveExpMsgConns": flWorkCipActiveExpMsgConns,
       "flWorkCipActiveMcastGroups": flWorkCipActiveMcastGroups,
       "flWorkCipOpenRequestsRcvd": flWorkCipOpenRequestsRcvd,
       "flWorkCipOpenResourceRejects": flWorkCipOpenResourceRejects,
       "flWorkCipOpenFormatRejects": flWorkCipOpenFormatRejects,
       "flWorkCipOpenOtherRejects": flWorkCipOpenOtherRejects,
       "flWorkCipCloseRequests": flWorkCipCloseRequests,
       "flWorkCipCloseFormatRejects": flWorkCipCloseFormatRejects,
       "flWorkCipCloseOtherRejects": flWorkCipCloseOtherRejects,
       "flWorkCipConnectionTimeouts": flWorkCipConnectionTimeouts,
       "flWorkCipNetworkStatus": flWorkCipNetworkStatus,
       "flWorkCipModuleStatus": flWorkCipModuleStatus,
       "flWorkCipClearStats": flWorkCipClearStats,
       "flWorkCipConnectionTable": flWorkCipConnectionTable,
       "flWorkCipConnectionEntry": flWorkCipConnectionEntry,
       "flWorkCipConnectionID": flWorkCipConnectionID,
       "flWorkCipConnectionOwnerIP": flWorkCipConnectionOwnerIP,
       "flWorkCipConnectionTransportClass": flWorkCipConnectionTransportClass,
       "flWlan": flWlan,
       "flWlanRadio": flWlanRadio,
       "flWlanRadioHwTable": flWlanRadioHwTable,
       "flWlanRadioHwEntry": flWlanRadioHwEntry,
       "flWlanRadioHwID": flWlanRadioHwID,
       "flWlanRadioHwAntMask": flWlanRadioHwAntMask,
       "flWlanRadioHwAggMode": flWlanRadioHwAggMode,
       "flWlanWifi": flWlanWifi,
       "flWlanWifiVapTable": flWlanWifiVapTable,
       "flWlanWifiVapEntry": flWlanWifiVapEntry,
       "flWlanWifiVapID": flWlanWifiVapID,
       "flWlanWifiVapFastEapolRetry": flWlanWifiVapFastEapolRetry,
       "flWlanWifiVapHideSsid": flWlanWifiVapHideSsid,
       "flWlanWifiVapExcessiveRetries": flWlanWifiVapExcessiveRetries,
       "flWlanWifiVapWdsBroadcast": flWlanWifiVapWdsBroadcast,
       "flWlanWifiVapWdsAgingTime": flWlanWifiVapWdsAgingTime,
       "flWlanWifiVapEnableState": flWlanWifiVapEnableState,
       "flWlanWifiVapChScanlist": flWlanWifiVapChScanlist,
       "flWlanWifiVapMaxNumClients": flWlanWifiVapMaxNumClients,
       "flWlanWifiVapStartScanning": flWlanWifiVapStartScanning,
       "flWlanWifiVapNetworkId": flWlanWifiVapNetworkId,
       "flWlanWifiVapManRoaming": flWlanWifiVapManRoaming,
       "flWlanWifiVapBgScanIdle": flWlanWifiVapBgScanIdle,
       "flWlanWifiVapRssiThrshForceScan": flWlanWifiVapRssiThrshForceScan,
       "flWlanWifiVapRssiChangeRoam": flWlanWifiVapRssiChangeRoam,
       "flWlanWifiVapRssiChangeBgScan": flWlanWifiVapRssiChangeBgScan,
       "flWlanWifiVapRssiThrshBgScan": flWlanWifiVapRssiThrshBgScan,
       "flWlanWifiVapScbManMac": flWlanWifiVapScbManMac,
       "flWlanWifiVapScbMode": flWlanWifiVapScbMode,
       "flWlanWifiVapFragThreshold": flWlanWifiVapFragThreshold,
       "flWlanWifiVapTxPowerRadiated": flWlanWifiVapTxPowerRadiated,
       "flWlanWifiVapCurrentTxPowerRadiated": flWlanWifiVapCurrentTxPowerRadiated,
       "flWlanWifiVapChBandwidth": flWlanWifiVapChBandwidth,
       "flWlanWifiVapWlanCh": flWlanWifiVapWlanCh,
       "flWlanWifiVap80211Mode": flWlanWifiVap80211Mode,
       "flWlanWifiVapHwID": flWlanWifiVapHwID,
       "flWlanWifiVapOpMode": flWlanWifiVapOpMode,
       "flWlanWifiVapStatus": flWlanWifiVapStatus,
       "flWlanWifiVapActiveProfile": flWlanWifiVapActiveProfile,
       "flWlanWifiVapRowStatus": flWlanWifiVapRowStatus,
       "flWlanWifiVapProfileTable": flWlanWifiVapProfileTable,
       "flWlanWifiVapProfileEntry": flWlanWifiVapProfileEntry,
       "flWlanWifiVapProfileVapID": flWlanWifiVapProfileVapID,
       "flWlanWifiVapProfileID": flWlanWifiVapProfileID,
       "flWlanWifiVapProfileEapClientcertPsKey": flWlanWifiVapProfileEapClientcertPsKey,
       "flWlanWifiVapProfileEapUserPw": flWlanWifiVapProfileEapUserPw,
       "flWlanWifiVapProfileEapIdentity": flWlanWifiVapProfileEapIdentity,
       "flWlanWifiVapProfileEapPhase2Auth": flWlanWifiVapProfileEapPhase2Auth,
       "flWlanWifiVapProfileEapPairwiseMode": flWlanWifiVapProfileEapPairwiseMode,
       "flWlanWifiVapProfileEapMode": flWlanWifiVapProfileEapMode,
       "flWlanWifiVapProfilePsKey": flWlanWifiVapProfilePsKey,
       "flWlanWifiVapProfileEnc": flWlanWifiVapProfileEnc,
       "flWlanWifiVapProfileAuth": flWlanWifiVapProfileAuth,
       "flWlanWifiVapProfileSsid": flWlanWifiVapProfileSsid,
       "flWlanWifiScanResultsTable": flWlanWifiScanResultsTable,
       "flWlanWifiScanResultsEntry": flWlanWifiScanResultsEntry,
       "flWlanWifiScanResultsVapID": flWlanWifiScanResultsVapID,
       "flWlanWifiScanResultsID": flWlanWifiScanResultsID,
       "flWlanWifiScanResultsEssid": flWlanWifiScanResultsEssid,
       "flWlanWifiScanResultsBssid": flWlanWifiScanResultsBssid,
       "flWlanWifiScanResultsCh": flWlanWifiScanResultsCh,
       "flWlanWifiScanResultsSignal": flWlanWifiScanResultsSignal,
       "flWlanWifiScanResultsSecurity": flWlanWifiScanResultsSecurity,
       "flWlanWifiScanResultsEnc": flWlanWifiScanResultsEnc,
       "flWlanWifiScanResultsMode": flWlanWifiScanResultsMode,
       "flWlanWifiConnectionTable": flWlanWifiConnectionTable,
       "flWlanWifiConnectionEntry": flWlanWifiConnectionEntry,
       "flWlanWifiConnectionVapID": flWlanWifiConnectionVapID,
       "flWlanWifiConnectionID": flWlanWifiConnectionID,
       "flWlanWifiConnectionOpMode": flWlanWifiConnectionOpMode,
       "flWlanWifiConnectionSsid": flWlanWifiConnectionSsid,
       "flWlanWifiConnectionMac": flWlanWifiConnectionMac,
       "flWlanWifiConnectionRssi": flWlanWifiConnectionRssi,
       "flWlanWifiConnectionBitRate": flWlanWifiConnectionBitRate,
       "flWlanWifiConnectionFreq": flWlanWifiConnectionFreq,
       "flWlanWifiConnectionCh": flWlanWifiConnectionCh,
       "flWlanApplySettings": flWlanApplySettings,
       "flWlanSettingsApplyState": flWlanSettingsApplyState,
       "flWlanManagementAccess": flWlanManagementAccess,
       "flWlanPtcpLldpFilter": flWlanPtcpLldpFilter,
       "flWlanCountry": flWlanCountry,
       "flWlanCountryTable": flWlanCountryTable,
       "flWlanCountryEntry": flWlanCountryEntry,
       "flWlanCountryID": flWlanCountryID,
       "flWlanCountryName": flWlanCountryName,
       "flWlanOutdoorMode": flWlanOutdoorMode,
       "flWlanGlobalActivation": flWlanGlobalActivation,
       "flWlanCyclicRssiTracking": flWlanCyclicRssiTracking}
)
