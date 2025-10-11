# SNMP MIB module (MX-CROUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-CROUT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:14 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

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

cRoutMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CRoutMIBObjects_ObjectIdentity = ObjectIdentity
cRoutMIBObjects = _CRoutMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1)
)
_StatusGroup_ObjectIdentity = ObjectIdentity
statusGroup = _StatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100)
)


class _ConfigModifiedStatus_Type(Integer32):
    """Custom type configModifiedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("yes", 100),
          ("no", 200))
    )


_ConfigModifiedStatus_Type.__name__ = "Integer32"
_ConfigModifiedStatus_Object = MibScalar
configModifiedStatus = _ConfigModifiedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 100),
    _ConfigModifiedStatus_Type()
)
configModifiedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configModifiedStatus.setStatus("current")
_InterfaceStatusTable_Object = MibTable
interfaceStatusTable = _InterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 200)
)
if mibBuilder.loadTexts:
    interfaceStatusTable.setStatus("current")
_InterfaceStatusEntry_Object = MibTableRow
interfaceStatusEntry = _InterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 200, 1)
)
interfaceStatusEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "interfaceStatusIndex"),
)
if mibBuilder.loadTexts:
    interfaceStatusEntry.setStatus("current")
_InterfaceStatusIndex_Type = Unsigned32
_InterfaceStatusIndex_Object = MibTableColumn
interfaceStatusIndex = _InterfaceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 200, 1, 100),
    _InterfaceStatusIndex_Type()
)
interfaceStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatusIndex.setStatus("current")
_InterfaceStatusName_Type = OctetString
_InterfaceStatusName_Object = MibTableColumn
interfaceStatusName = _InterfaceStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 200, 1, 200),
    _InterfaceStatusName_Type()
)
interfaceStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatusName.setStatus("current")
_RouteStatusTable_Object = MibTable
routeStatusTable = _RouteStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300)
)
if mibBuilder.loadTexts:
    routeStatusTable.setStatus("current")
_RouteStatusEntry_Object = MibTableRow
routeStatusEntry = _RouteStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300, 1)
)
routeStatusEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "routeStatusIndex"),
)
if mibBuilder.loadTexts:
    routeStatusEntry.setStatus("current")
_RouteStatusIndex_Type = Unsigned32
_RouteStatusIndex_Object = MibTableColumn
routeStatusIndex = _RouteStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300, 1, 100),
    _RouteStatusIndex_Type()
)
routeStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatusIndex.setStatus("current")


class _RouteStatusType_Type(Integer32):
    """Custom type routeStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("user", 100),
          ("auto", 200))
    )


_RouteStatusType_Type.__name__ = "Integer32"
_RouteStatusType_Object = MibTableColumn
routeStatusType = _RouteStatusType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300, 1, 150),
    _RouteStatusType_Type()
)
routeStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatusType.setStatus("current")
_RouteStatusSourceCriteria_Type = OctetString
_RouteStatusSourceCriteria_Object = MibTableColumn
routeStatusSourceCriteria = _RouteStatusSourceCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300, 1, 200),
    _RouteStatusSourceCriteria_Type()
)
routeStatusSourceCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatusSourceCriteria.setStatus("current")


class _RouteStatusPropertiesCriteria_Type(Integer32):
    """Custom type routeStatusPropertiesCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600,
              1700,
              1800,
              1900,
              2000,
              2100,
              2200,
              2300,
              2400)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("calledE164", 200),
          ("callingE164", 300),
          ("calledName", 400),
          ("callingName", 500),
          ("calledTon", 600),
          ("callingTon", 700),
          ("calledNpi", 800),
          ("callingNpi", 900),
          ("calledHost", 1000),
          ("callingHost", 1100),
          ("callingPi", 1200),
          ("callingSi", 1300),
          ("callingItc", 1400),
          ("calledUri", 1500),
          ("callingUri", 1600),
          ("dateTime", 1700),
          ("calledPhoneContext", 1800),
          ("callingPhoneContext", 1900),
          ("calledSipUsername", 2000),
          ("callingSipUsername", 2100),
          ("calledBearerChannel", 2200),
          ("callingBearerChannel", 2300),
          ("callingSipPrivacy", 2400))
    )


_RouteStatusPropertiesCriteria_Type.__name__ = "Integer32"
_RouteStatusPropertiesCriteria_Object = MibTableColumn
routeStatusPropertiesCriteria = _RouteStatusPropertiesCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300, 1, 300),
    _RouteStatusPropertiesCriteria_Type()
)
routeStatusPropertiesCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatusPropertiesCriteria.setStatus("current")
_RouteStatusExpressionCriteria_Type = OctetString
_RouteStatusExpressionCriteria_Object = MibTableColumn
routeStatusExpressionCriteria = _RouteStatusExpressionCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300, 1, 400),
    _RouteStatusExpressionCriteria_Type()
)
routeStatusExpressionCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatusExpressionCriteria.setStatus("current")
_RouteStatusDestination_Type = OctetString
_RouteStatusDestination_Object = MibTableColumn
routeStatusDestination = _RouteStatusDestination_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300, 1, 500),
    _RouteStatusDestination_Type()
)
routeStatusDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatusDestination.setStatus("current")
_RouteStatusMappings_Type = OctetString
_RouteStatusMappings_Object = MibTableColumn
routeStatusMappings = _RouteStatusMappings_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300, 1, 600),
    _RouteStatusMappings_Type()
)
routeStatusMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatusMappings.setStatus("current")
_RouteStatusSignalingProperties_Type = OctetString
_RouteStatusSignalingProperties_Object = MibTableColumn
routeStatusSignalingProperties = _RouteStatusSignalingProperties_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 300, 1, 700),
    _RouteStatusSignalingProperties_Type()
)
routeStatusSignalingProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatusSignalingProperties.setStatus("current")
_MappingTypeStatusTable_Object = MibTable
mappingTypeStatusTable = _MappingTypeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 400)
)
if mibBuilder.loadTexts:
    mappingTypeStatusTable.setStatus("current")
_MappingTypeStatusEntry_Object = MibTableRow
mappingTypeStatusEntry = _MappingTypeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 400, 1)
)
mappingTypeStatusEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "mappingTypeStatusIndex"),
)
if mibBuilder.loadTexts:
    mappingTypeStatusEntry.setStatus("current")
_MappingTypeStatusIndex_Type = Unsigned32
_MappingTypeStatusIndex_Object = MibTableColumn
mappingTypeStatusIndex = _MappingTypeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 400, 1, 100),
    _MappingTypeStatusIndex_Type()
)
mappingTypeStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingTypeStatusIndex.setStatus("current")
_MappingTypeStatusName_Type = OctetString
_MappingTypeStatusName_Object = MibTableColumn
mappingTypeStatusName = _MappingTypeStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 400, 1, 200),
    _MappingTypeStatusName_Type()
)
mappingTypeStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingTypeStatusName.setStatus("current")


class _MappingTypeStatusCriteria_Type(Integer32):
    """Custom type mappingTypeStatusCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600,
              1700,
              1800,
              1900,
              2000,
              2100,
              2200,
              2300,
              2400,
              2500,
              2600,
              2700,
              2800,
              2900,
              3000,
              3100,
              3110,
              3120,
              3130,
              3140,
              3200,
              3300,
              3400,
              3500,
              3600,
              3700,
              3800,
              3900,
              4000)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("e164", 200),
          ("calledE164", 300),
          ("callingE164", 400),
          ("name", 500),
          ("calledName", 600),
          ("callingName", 700),
          ("ton", 800),
          ("calledTon", 900),
          ("callingTon", 1000),
          ("npi", 1100),
          ("calledNpi", 1200),
          ("callingNpi", 1300),
          ("host", 1400),
          ("calledHost", 1500),
          ("callingHost", 1600),
          ("callingPi", 1700),
          ("callingSi", 1800),
          ("callingItc", 1900),
          ("uri", 2000),
          ("calledUri", 2100),
          ("callingUri", 2200),
          ("dateTime", 2300),
          ("phoneContext", 2400),
          ("calledPhoneContext", 2500),
          ("callingPhoneContext", 2600),
          ("sipUsername", 2700),
          ("calledSipUsername", 2800),
          ("callingSipUsername", 2900),
          ("lastDivertingReason", 3000),
          ("lastDivertingE164", 3100),
          ("lastDivertingPartyNumberType", 3110),
          ("lastDivertingPublicTypeOfNumber", 3120),
          ("lastDivertingPrivateTypeOfNumber", 3130),
          ("lastDivertingNumberPresentation", 3140),
          ("originalDivertingReason", 3200),
          ("originalDivertingE164", 3300),
          ("originalDivertingPartyNumberType", 3400),
          ("originalDivertingPublicTypeOfNumber", 3500),
          ("originalDivertingPrivateTypeOfNumber", 3600),
          ("originalDivertingNumberPresentation", 3700),
          ("calledBearerChannel", 3800),
          ("callingBearerChannel", 3900),
          ("callingSipPrivacy", 4000))
    )


_MappingTypeStatusCriteria_Type.__name__ = "Integer32"
_MappingTypeStatusCriteria_Object = MibTableColumn
mappingTypeStatusCriteria = _MappingTypeStatusCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 400, 1, 300),
    _MappingTypeStatusCriteria_Type()
)
mappingTypeStatusCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingTypeStatusCriteria.setStatus("current")


class _MappingTypeStatusTransformation_Type(Integer32):
    """Custom type mappingTypeStatusTransformation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600,
              1700,
              1800,
              1900,
              2000,
              2100,
              2200,
              2300,
              2400,
              2500,
              2600,
              2700,
              2800,
              2900,
              3000,
              3010,
              3020,
              3030,
              3040,
              3100,
              3200,
              3300,
              3400,
              3500,
              3600,
              3700,
              3800,
              60000)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("e164", 200),
          ("calledE164", 300),
          ("callingE164", 400),
          ("name", 500),
          ("calledName", 600),
          ("callingName", 700),
          ("ton", 800),
          ("calledTon", 900),
          ("callingTon", 1000),
          ("npi", 1100),
          ("calledNpi", 1200),
          ("callingNpi", 1300),
          ("host", 1400),
          ("calledHost", 1500),
          ("callingHost", 1600),
          ("callingPi", 1700),
          ("callingSi", 1800),
          ("callingItc", 1900),
          ("uri", 2000),
          ("calledUri", 2100),
          ("callingUri", 2200),
          ("phoneContext", 2300),
          ("calledPhoneContext", 2400),
          ("callingPhoneContext", 2500),
          ("sipUsername", 2600),
          ("calledSipUsername", 2700),
          ("callingSipUsername", 2800),
          ("lastDivertingReason", 2900),
          ("lastDivertingE164", 3000),
          ("lastDivertingPartyNumberType", 3010),
          ("lastDivertingPublicTypeOfNumber", 3020),
          ("lastDivertingPrivateTypeOfNumber", 3030),
          ("lastDivertingNumberPresentation", 3040),
          ("originalDivertingReason", 3100),
          ("originalDivertingE164", 3200),
          ("originalDivertingPartyNumberType", 3300),
          ("originalDivertingPublicTypeOfNumber", 3400),
          ("originalDivertingPrivateTypeOfNumber", 3500),
          ("originalDivertingNumberPresentation", 3600),
          ("calledBearerChannel", 3700),
          ("callingBearerChannel", 3800),
          ("debug", 60000))
    )


_MappingTypeStatusTransformation_Type.__name__ = "Integer32"
_MappingTypeStatusTransformation_Object = MibTableColumn
mappingTypeStatusTransformation = _MappingTypeStatusTransformation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 400, 1, 400),
    _MappingTypeStatusTransformation_Type()
)
mappingTypeStatusTransformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingTypeStatusTransformation.setStatus("current")
_MappingExpressionStatusTable_Object = MibTable
mappingExpressionStatusTable = _MappingExpressionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 500)
)
if mibBuilder.loadTexts:
    mappingExpressionStatusTable.setStatus("current")
_MappingExpressionStatusEntry_Object = MibTableRow
mappingExpressionStatusEntry = _MappingExpressionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 500, 1)
)
mappingExpressionStatusEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "mappingExpressionStatusIndex"),
)
if mibBuilder.loadTexts:
    mappingExpressionStatusEntry.setStatus("current")
_MappingExpressionStatusIndex_Type = Unsigned32
_MappingExpressionStatusIndex_Object = MibTableColumn
mappingExpressionStatusIndex = _MappingExpressionStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 500, 1, 100),
    _MappingExpressionStatusIndex_Type()
)
mappingExpressionStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingExpressionStatusIndex.setStatus("current")
_MappingExpressionStatusName_Type = OctetString
_MappingExpressionStatusName_Object = MibTableColumn
mappingExpressionStatusName = _MappingExpressionStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 500, 1, 200),
    _MappingExpressionStatusName_Type()
)
mappingExpressionStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingExpressionStatusName.setStatus("current")
_MappingExpressionStatusCriteria_Type = OctetString
_MappingExpressionStatusCriteria_Object = MibTableColumn
mappingExpressionStatusCriteria = _MappingExpressionStatusCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 500, 1, 300),
    _MappingExpressionStatusCriteria_Type()
)
mappingExpressionStatusCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingExpressionStatusCriteria.setStatus("current")
_MappingExpressionStatusTransformation_Type = OctetString
_MappingExpressionStatusTransformation_Object = MibTableColumn
mappingExpressionStatusTransformation = _MappingExpressionStatusTransformation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 500, 1, 400),
    _MappingExpressionStatusTransformation_Type()
)
mappingExpressionStatusTransformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingExpressionStatusTransformation.setStatus("current")
_MappingExpressionStatusSubMappings_Type = OctetString
_MappingExpressionStatusSubMappings_Object = MibTableColumn
mappingExpressionStatusSubMappings = _MappingExpressionStatusSubMappings_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 500, 1, 500),
    _MappingExpressionStatusSubMappings_Type()
)
mappingExpressionStatusSubMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingExpressionStatusSubMappings.setStatus("current")
_HuntStatusTable_Object = MibTable
huntStatusTable = _HuntStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 600)
)
if mibBuilder.loadTexts:
    huntStatusTable.setStatus("current")
_HuntStatusEntry_Object = MibTableRow
huntStatusEntry = _HuntStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 600, 1)
)
huntStatusEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "huntStatusIndex"),
)
if mibBuilder.loadTexts:
    huntStatusEntry.setStatus("current")
_HuntStatusIndex_Type = Unsigned32
_HuntStatusIndex_Object = MibTableColumn
huntStatusIndex = _HuntStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 600, 1, 100),
    _HuntStatusIndex_Type()
)
huntStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    huntStatusIndex.setStatus("current")
_HuntStatusName_Type = OctetString
_HuntStatusName_Object = MibTableColumn
huntStatusName = _HuntStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 600, 1, 200),
    _HuntStatusName_Type()
)
huntStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    huntStatusName.setStatus("current")
_HuntStatusDestinations_Type = OctetString
_HuntStatusDestinations_Object = MibTableColumn
huntStatusDestinations = _HuntStatusDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 600, 1, 300),
    _HuntStatusDestinations_Type()
)
huntStatusDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    huntStatusDestinations.setStatus("current")


class _HuntStatusSelectionAlgorithm_Type(Integer32):
    """Custom type huntStatusSelectionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("sequential", 100),
          ("cyclic", 200),
          ("simultaneous", 300))
    )


_HuntStatusSelectionAlgorithm_Type.__name__ = "Integer32"
_HuntStatusSelectionAlgorithm_Object = MibTableColumn
huntStatusSelectionAlgorithm = _HuntStatusSelectionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 600, 1, 400),
    _HuntStatusSelectionAlgorithm_Type()
)
huntStatusSelectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    huntStatusSelectionAlgorithm.setStatus("current")
_HuntStatusTimeout_Type = Unsigned32
_HuntStatusTimeout_Object = MibTableColumn
huntStatusTimeout = _HuntStatusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 600, 1, 500),
    _HuntStatusTimeout_Type()
)
huntStatusTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    huntStatusTimeout.setStatus("current")
_HuntStatusCauses_Type = OctetString
_HuntStatusCauses_Object = MibTableColumn
huntStatusCauses = _HuntStatusCauses_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 600, 1, 600),
    _HuntStatusCauses_Type()
)
huntStatusCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    huntStatusCauses.setStatus("current")
_SignalingPropertiesStatusTable_Object = MibTable
signalingPropertiesStatusTable = _SignalingPropertiesStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700)
)
if mibBuilder.loadTexts:
    signalingPropertiesStatusTable.setStatus("current")
_SignalingPropertiesStatusEntry_Object = MibTableRow
signalingPropertiesStatusEntry = _SignalingPropertiesStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1)
)
signalingPropertiesStatusEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "signalingPropertiesStatusIndex"),
)
if mibBuilder.loadTexts:
    signalingPropertiesStatusEntry.setStatus("current")
_SignalingPropertiesStatusIndex_Type = Unsigned32
_SignalingPropertiesStatusIndex_Object = MibTableColumn
signalingPropertiesStatusIndex = _SignalingPropertiesStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 100),
    _SignalingPropertiesStatusIndex_Type()
)
signalingPropertiesStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusIndex.setStatus("current")
_SignalingPropertiesStatusName_Type = OctetString
_SignalingPropertiesStatusName_Object = MibTableColumn
signalingPropertiesStatusName = _SignalingPropertiesStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 200),
    _SignalingPropertiesStatusName_Type()
)
signalingPropertiesStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusName.setStatus("current")
_SignalingPropertiesStatusEarlyConnect_Type = MxEnableState
_SignalingPropertiesStatusEarlyConnect_Object = MibTableColumn
signalingPropertiesStatusEarlyConnect = _SignalingPropertiesStatusEarlyConnect_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 300),
    _SignalingPropertiesStatusEarlyConnect_Type()
)
signalingPropertiesStatusEarlyConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusEarlyConnect.setStatus("current")
_SignalingPropertiesStatusEarlyDisconnect_Type = MxEnableState
_SignalingPropertiesStatusEarlyDisconnect_Object = MibTableColumn
signalingPropertiesStatusEarlyDisconnect = _SignalingPropertiesStatusEarlyDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 400),
    _SignalingPropertiesStatusEarlyDisconnect_Type()
)
signalingPropertiesStatusEarlyDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusEarlyDisconnect.setStatus("current")
_SignalingPropertiesStatusDestinationHost_Type = OctetString
_SignalingPropertiesStatusDestinationHost_Object = MibTableColumn
signalingPropertiesStatusDestinationHost = _SignalingPropertiesStatusDestinationHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 500),
    _SignalingPropertiesStatusDestinationHost_Type()
)
signalingPropertiesStatusDestinationHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusDestinationHost.setStatus("current")
_SignalingPropertiesStatusAllow180Sdp_Type = MxEnableState
_SignalingPropertiesStatusAllow180Sdp_Object = MibTableColumn
signalingPropertiesStatusAllow180Sdp = _SignalingPropertiesStatusAllow180Sdp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 600),
    _SignalingPropertiesStatusAllow180Sdp_Type()
)
signalingPropertiesStatusAllow180Sdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusAllow180Sdp.setStatus("current")
_SignalingPropertiesStatusAllow183NoSdp_Type = MxEnableState
_SignalingPropertiesStatusAllow183NoSdp_Object = MibTableColumn
signalingPropertiesStatusAllow183NoSdp = _SignalingPropertiesStatusAllow183NoSdp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 700),
    _SignalingPropertiesStatusAllow183NoSdp_Type()
)
signalingPropertiesStatusAllow183NoSdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusAllow183NoSdp.setStatus("current")


class _SignalingPropertiesStatusPrivacy_Type(Integer32):
    """Custom type signalingPropertiesStatusPrivacy based on Integer32"""
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
        *(("disable", 100),
          ("none", 200),
          ("id", 300),
          ("rpid", 400))
    )


_SignalingPropertiesStatusPrivacy_Type.__name__ = "Integer32"
_SignalingPropertiesStatusPrivacy_Object = MibTableColumn
signalingPropertiesStatusPrivacy = _SignalingPropertiesStatusPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 800),
    _SignalingPropertiesStatusPrivacy_Type()
)
signalingPropertiesStatusPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusPrivacy.setStatus("current")
_SignalingPropertiesStatusCallPropertiesTranslation_Type = OctetString
_SignalingPropertiesStatusCallPropertiesTranslation_Object = MibTableColumn
signalingPropertiesStatusCallPropertiesTranslation = _SignalingPropertiesStatusCallPropertiesTranslation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 900),
    _SignalingPropertiesStatusCallPropertiesTranslation_Type()
)
signalingPropertiesStatusCallPropertiesTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusCallPropertiesTranslation.setStatus("current")
_SignalingPropertiesStatusSipHeadersTranslation_Type = OctetString
_SignalingPropertiesStatusSipHeadersTranslation_Object = MibTableColumn
signalingPropertiesStatusSipHeadersTranslation = _SignalingPropertiesStatusSipHeadersTranslation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 700, 1, 1000),
    _SignalingPropertiesStatusSipHeadersTranslation_Type()
)
signalingPropertiesStatusSipHeadersTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesStatusSipHeadersTranslation.setStatus("current")
_SipHeadersTranslationStatusTable_Object = MibTable
sipHeadersTranslationStatusTable = _SipHeadersTranslationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 800)
)
if mibBuilder.loadTexts:
    sipHeadersTranslationStatusTable.setStatus("current")
_SipHeadersTranslationStatusEntry_Object = MibTableRow
sipHeadersTranslationStatusEntry = _SipHeadersTranslationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 800, 1)
)
sipHeadersTranslationStatusEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "sipHeadersTranslationStatusIndex"),
)
if mibBuilder.loadTexts:
    sipHeadersTranslationStatusEntry.setStatus("current")
_SipHeadersTranslationStatusIndex_Type = Unsigned32
_SipHeadersTranslationStatusIndex_Object = MibTableColumn
sipHeadersTranslationStatusIndex = _SipHeadersTranslationStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 800, 1, 100),
    _SipHeadersTranslationStatusIndex_Type()
)
sipHeadersTranslationStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipHeadersTranslationStatusIndex.setStatus("current")


class _SipHeadersTranslationStatusName_Type(OctetString):
    """Custom type sipHeadersTranslationStatusName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SipHeadersTranslationStatusName_Type.__name__ = "OctetString"
_SipHeadersTranslationStatusName_Object = MibTableColumn
sipHeadersTranslationStatusName = _SipHeadersTranslationStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 800, 1, 200),
    _SipHeadersTranslationStatusName_Type()
)
sipHeadersTranslationStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipHeadersTranslationStatusName.setStatus("current")


class _SipHeadersTranslationStatusSipHeader_Type(Integer32):
    """Custom type sipHeadersTranslationStatusSipHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              550,
              600,
              700,
              800,
              900)
        )
    )
    namedValues = NamedValues(
        *(("fromHeaderHostPart", 100),
          ("fromHeaderUserPart", 200),
          ("identityHeaderHostPart", 300),
          ("identityHeaderUserPart", 400),
          ("identityHeaderPhoneNumber", 500),
          ("identityHeaderFriendlyName", 550),
          ("requestLineHostPart", 600),
          ("requestLineUserPart", 700),
          ("toHeaderHostPart", 800),
          ("toHeaderUserPart", 900))
    )


_SipHeadersTranslationStatusSipHeader_Type.__name__ = "Integer32"
_SipHeadersTranslationStatusSipHeader_Object = MibTableColumn
sipHeadersTranslationStatusSipHeader = _SipHeadersTranslationStatusSipHeader_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 800, 1, 300),
    _SipHeadersTranslationStatusSipHeader_Type()
)
sipHeadersTranslationStatusSipHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipHeadersTranslationStatusSipHeader.setStatus("current")


class _SipHeadersTranslationStatusBuiltFrom_Type(Integer32):
    """Custom type sipHeadersTranslationStatusBuiltFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("calledE164", 100),
          ("destinationHost", 200),
          ("domain", 300),
          ("fixValue", 400),
          ("hostName", 500),
          ("localIp", 600),
          ("callingBearerChannel", 700),
          ("sipEndpointUsername", 800),
          ("callingName", 900),
          ("callingE164", 1000))
    )


_SipHeadersTranslationStatusBuiltFrom_Type.__name__ = "Integer32"
_SipHeadersTranslationStatusBuiltFrom_Object = MibTableColumn
sipHeadersTranslationStatusBuiltFrom = _SipHeadersTranslationStatusBuiltFrom_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 800, 1, 400),
    _SipHeadersTranslationStatusBuiltFrom_Type()
)
sipHeadersTranslationStatusBuiltFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipHeadersTranslationStatusBuiltFrom.setStatus("current")


class _SipHeadersTranslationStatusFixValue_Type(OctetString):
    """Custom type sipHeadersTranslationStatusFixValue based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipHeadersTranslationStatusFixValue_Type.__name__ = "OctetString"
_SipHeadersTranslationStatusFixValue_Object = MibTableColumn
sipHeadersTranslationStatusFixValue = _SipHeadersTranslationStatusFixValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 800, 1, 500),
    _SipHeadersTranslationStatusFixValue_Type()
)
sipHeadersTranslationStatusFixValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipHeadersTranslationStatusFixValue.setStatus("current")
_CallPropertiesTranslationStatusTable_Object = MibTable
callPropertiesTranslationStatusTable = _CallPropertiesTranslationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 900)
)
if mibBuilder.loadTexts:
    callPropertiesTranslationStatusTable.setStatus("current")
_CallPropertiesTranslationStatusEntry_Object = MibTableRow
callPropertiesTranslationStatusEntry = _CallPropertiesTranslationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 900, 1)
)
callPropertiesTranslationStatusEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "callPropertiesTranslationStatusIndex"),
)
if mibBuilder.loadTexts:
    callPropertiesTranslationStatusEntry.setStatus("current")
_CallPropertiesTranslationStatusIndex_Type = Unsigned32
_CallPropertiesTranslationStatusIndex_Object = MibTableColumn
callPropertiesTranslationStatusIndex = _CallPropertiesTranslationStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 900, 1, 100),
    _CallPropertiesTranslationStatusIndex_Type()
)
callPropertiesTranslationStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callPropertiesTranslationStatusIndex.setStatus("current")


class _CallPropertiesTranslationStatusName_Type(OctetString):
    """Custom type callPropertiesTranslationStatusName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CallPropertiesTranslationStatusName_Type.__name__ = "OctetString"
_CallPropertiesTranslationStatusName_Object = MibTableColumn
callPropertiesTranslationStatusName = _CallPropertiesTranslationStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 900, 1, 200),
    _CallPropertiesTranslationStatusName_Type()
)
callPropertiesTranslationStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callPropertiesTranslationStatusName.setStatus("current")


class _CallPropertiesTranslationStatusCallProperty_Type(Integer32):
    """Custom type callPropertiesTranslationStatusCallProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700)
        )
    )
    namedValues = NamedValues(
        *(("calledE164", 100),
          ("callingE164", 200),
          ("calledName", 300),
          ("callingName", 400),
          ("calledUri", 500),
          ("callingUri", 600),
          ("calledBearerChannel", 700))
    )


_CallPropertiesTranslationStatusCallProperty_Type.__name__ = "Integer32"
_CallPropertiesTranslationStatusCallProperty_Object = MibTableColumn
callPropertiesTranslationStatusCallProperty = _CallPropertiesTranslationStatusCallProperty_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 900, 1, 300),
    _CallPropertiesTranslationStatusCallProperty_Type()
)
callPropertiesTranslationStatusCallProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callPropertiesTranslationStatusCallProperty.setStatus("current")


class _CallPropertiesTranslationStatusBuiltFrom_Type(Integer32):
    """Custom type callPropertiesTranslationStatusBuiltFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              850,
              900,
              1000,
              1100,
              1200,
              1300,
              1400)
        )
    )
    namedValues = NamedValues(
        *(("domain", 100),
          ("fixValue", 200),
          ("fromHeaderUri", 300),
          ("fromHeaderFriendlyName", 400),
          ("fromHeaderUserPart", 500),
          ("identityHeaderUri", 600),
          ("identityHeaderUserPart", 700),
          ("identityHeaderPhoneNumber", 800),
          ("identityHeaderFriendlyName", 850),
          ("localIp", 900),
          ("requestLineUri", 1000),
          ("requestLineUserPart", 1100),
          ("toHeaderUri", 1200),
          ("toHeaderFriendlyName", 1300),
          ("toHeaderUserPart", 1400))
    )


_CallPropertiesTranslationStatusBuiltFrom_Type.__name__ = "Integer32"
_CallPropertiesTranslationStatusBuiltFrom_Object = MibTableColumn
callPropertiesTranslationStatusBuiltFrom = _CallPropertiesTranslationStatusBuiltFrom_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 900, 1, 400),
    _CallPropertiesTranslationStatusBuiltFrom_Type()
)
callPropertiesTranslationStatusBuiltFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callPropertiesTranslationStatusBuiltFrom.setStatus("current")


class _CallPropertiesTranslationStatusFixValue_Type(OctetString):
    """Custom type callPropertiesTranslationStatusFixValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CallPropertiesTranslationStatusFixValue_Type.__name__ = "OctetString"
_CallPropertiesTranslationStatusFixValue_Object = MibTableColumn
callPropertiesTranslationStatusFixValue = _CallPropertiesTranslationStatusFixValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 900, 1, 500),
    _CallPropertiesTranslationStatusFixValue_Type()
)
callPropertiesTranslationStatusFixValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callPropertiesTranslationStatusFixValue.setStatus("current")
_SipRedirectStatusTable_Object = MibTable
sipRedirectStatusTable = _SipRedirectStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 1000)
)
if mibBuilder.loadTexts:
    sipRedirectStatusTable.setStatus("current")
_SipRedirectStatusEntry_Object = MibTableRow
sipRedirectStatusEntry = _SipRedirectStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 1000, 1)
)
sipRedirectStatusEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "sipRedirectStatusIndex"),
)
if mibBuilder.loadTexts:
    sipRedirectStatusEntry.setStatus("current")
_SipRedirectStatusIndex_Type = Unsigned32
_SipRedirectStatusIndex_Object = MibTableColumn
sipRedirectStatusIndex = _SipRedirectStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 1000, 1, 100),
    _SipRedirectStatusIndex_Type()
)
sipRedirectStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRedirectStatusIndex.setStatus("current")


class _SipRedirectStatusName_Type(OctetString):
    """Custom type sipRedirectStatusName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SipRedirectStatusName_Type.__name__ = "OctetString"
_SipRedirectStatusName_Object = MibTableColumn
sipRedirectStatusName = _SipRedirectStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 1000, 1, 200),
    _SipRedirectStatusName_Type()
)
sipRedirectStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRedirectStatusName.setStatus("current")


class _SipRedirectStatusDestinationHost_Type(OctetString):
    """Custom type sipRedirectStatusDestinationHost based on OctetString"""
    defaultValue = OctetString("")


_SipRedirectStatusDestinationHost_Type.__name__ = "OctetString"
_SipRedirectStatusDestinationHost_Object = MibTableColumn
sipRedirectStatusDestinationHost = _SipRedirectStatusDestinationHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 100, 1000, 1, 300),
    _SipRedirectStatusDestinationHost_Type()
)
sipRedirectStatusDestinationHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRedirectStatusDestinationHost.setStatus("current")


class _AutoRoutingEnable_Type(MxEnableState):
    """Custom type autoRoutingEnable based on MxEnableState"""
    defaultValue = 0


_AutoRoutingEnable_Type.__name__ = "MxEnableState"
_AutoRoutingEnable_Object = MibScalar
autoRoutingEnable = _AutoRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 200),
    _AutoRoutingEnable_Type()
)
autoRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRoutingEnable.setStatus("current")
_RouteTable_Object = MibTable
routeTable = _RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300)
)
if mibBuilder.loadTexts:
    routeTable.setStatus("current")
_RouteEntry_Object = MibTableRow
routeEntry = _RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1)
)
routeEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "routeIndex"),
)
if mibBuilder.loadTexts:
    routeEntry.setStatus("current")
_RouteIndex_Type = Unsigned32
_RouteIndex_Object = MibTableColumn
routeIndex = _RouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 100),
    _RouteIndex_Type()
)
routeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeIndex.setStatus("current")


class _RouteSourceCriteria_Type(OctetString):
    """Custom type routeSourceCriteria based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_RouteSourceCriteria_Type.__name__ = "OctetString"
_RouteSourceCriteria_Object = MibTableColumn
routeSourceCriteria = _RouteSourceCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 200),
    _RouteSourceCriteria_Type()
)
routeSourceCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeSourceCriteria.setStatus("current")


class _RoutePropertiesCriteria_Type(Integer32):
    """Custom type routePropertiesCriteria based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600,
              1700,
              1800,
              1900,
              2000,
              2100,
              2200,
              2300,
              2400)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("calledE164", 200),
          ("callingE164", 300),
          ("calledName", 400),
          ("callingName", 500),
          ("calledTon", 600),
          ("callingTon", 700),
          ("calledNpi", 800),
          ("callingNpi", 900),
          ("calledHost", 1000),
          ("callingHost", 1100),
          ("callingPi", 1200),
          ("callingSi", 1300),
          ("callingItc", 1400),
          ("calledUri", 1500),
          ("callingUri", 1600),
          ("dateTime", 1700),
          ("calledPhoneContext", 1800),
          ("callingPhoneContext", 1900),
          ("calledSipUsername", 2000),
          ("callingSipUsername", 2100),
          ("calledBearerChannel", 2200),
          ("callingBearerChannel", 2300),
          ("callingSipPrivacy", 2400))
    )


_RoutePropertiesCriteria_Type.__name__ = "Integer32"
_RoutePropertiesCriteria_Object = MibTableColumn
routePropertiesCriteria = _RoutePropertiesCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 300),
    _RoutePropertiesCriteria_Type()
)
routePropertiesCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routePropertiesCriteria.setStatus("current")


class _RouteExpressionCriteria_Type(OctetString):
    """Custom type routeExpressionCriteria based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RouteExpressionCriteria_Type.__name__ = "OctetString"
_RouteExpressionCriteria_Object = MibTableColumn
routeExpressionCriteria = _RouteExpressionCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 400),
    _RouteExpressionCriteria_Type()
)
routeExpressionCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeExpressionCriteria.setStatus("current")


class _RouteDestination_Type(OctetString):
    """Custom type routeDestination based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RouteDestination_Type.__name__ = "OctetString"
_RouteDestination_Object = MibTableColumn
routeDestination = _RouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 500),
    _RouteDestination_Type()
)
routeDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDestination.setStatus("current")


class _RouteMappings_Type(OctetString):
    """Custom type routeMappings based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RouteMappings_Type.__name__ = "OctetString"
_RouteMappings_Object = MibTableColumn
routeMappings = _RouteMappings_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 600),
    _RouteMappings_Type()
)
routeMappings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeMappings.setStatus("current")


class _RouteSignalingProperties_Type(OctetString):
    """Custom type routeSignalingProperties based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RouteSignalingProperties_Type.__name__ = "OctetString"
_RouteSignalingProperties_Object = MibTableColumn
routeSignalingProperties = _RouteSignalingProperties_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 650),
    _RouteSignalingProperties_Type()
)
routeSignalingProperties.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeSignalingProperties.setStatus("current")
_RouteConfigStatus_Type = OctetString
_RouteConfigStatus_Object = MibTableColumn
routeConfigStatus = _RouteConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 700),
    _RouteConfigStatus_Type()
)
routeConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeConfigStatus.setStatus("current")


class _RouteUp_Type(Integer32):
    """Custom type routeUp based on Integer32"""
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
          ("up", 10))
    )


_RouteUp_Type.__name__ = "Integer32"
_RouteUp_Object = MibTableColumn
routeUp = _RouteUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 800),
    _RouteUp_Type()
)
routeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeUp.setStatus("current")


class _RouteDown_Type(Integer32):
    """Custom type routeDown based on Integer32"""
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
          ("down", 10))
    )


_RouteDown_Type.__name__ = "Integer32"
_RouteDown_Object = MibTableColumn
routeDown = _RouteDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 900),
    _RouteDown_Type()
)
routeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDown.setStatus("current")


class _RouteInsert_Type(Integer32):
    """Custom type routeInsert based on Integer32"""
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
          ("insert", 10))
    )


_RouteInsert_Type.__name__ = "Integer32"
_RouteInsert_Object = MibTableColumn
routeInsert = _RouteInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 1000),
    _RouteInsert_Type()
)
routeInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeInsert.setStatus("current")


class _RouteDelete_Type(Integer32):
    """Custom type routeDelete based on Integer32"""
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
          ("delete", 10))
    )


_RouteDelete_Type.__name__ = "Integer32"
_RouteDelete_Object = MibTableColumn
routeDelete = _RouteDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 300, 1, 1100),
    _RouteDelete_Type()
)
routeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDelete.setStatus("current")
_MappingTypeTable_Object = MibTable
mappingTypeTable = _MappingTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500)
)
if mibBuilder.loadTexts:
    mappingTypeTable.setStatus("current")
_MappingTypeEntry_Object = MibTableRow
mappingTypeEntry = _MappingTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1)
)
mappingTypeEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "mappingTypeIndex"),
)
if mibBuilder.loadTexts:
    mappingTypeEntry.setStatus("current")
_MappingTypeIndex_Type = Unsigned32
_MappingTypeIndex_Object = MibTableColumn
mappingTypeIndex = _MappingTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1, 100),
    _MappingTypeIndex_Type()
)
mappingTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingTypeIndex.setStatus("current")


class _MappingTypeName_Type(OctetString):
    """Custom type mappingTypeName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MappingTypeName_Type.__name__ = "OctetString"
_MappingTypeName_Object = MibTableColumn
mappingTypeName = _MappingTypeName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1, 200),
    _MappingTypeName_Type()
)
mappingTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingTypeName.setStatus("current")


class _MappingTypeCriteria_Type(Integer32):
    """Custom type mappingTypeCriteria based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600,
              1700,
              1800,
              1900,
              2000,
              2100,
              2200,
              2300,
              2400,
              2500,
              2600,
              2700,
              2800,
              2900,
              3000,
              3100,
              3110,
              3120,
              3130,
              3140,
              3200,
              3300,
              3400,
              3500,
              3600,
              3700,
              3800,
              3900,
              4000)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("e164", 200),
          ("calledE164", 300),
          ("callingE164", 400),
          ("name", 500),
          ("calledName", 600),
          ("callingName", 700),
          ("ton", 800),
          ("calledTon", 900),
          ("callingTon", 1000),
          ("npi", 1100),
          ("calledNpi", 1200),
          ("callingNpi", 1300),
          ("host", 1400),
          ("calledHost", 1500),
          ("callingHost", 1600),
          ("callingPi", 1700),
          ("callingSi", 1800),
          ("callingItc", 1900),
          ("uri", 2000),
          ("calledUri", 2100),
          ("callingUri", 2200),
          ("dateTime", 2300),
          ("phoneContext", 2400),
          ("calledPhoneContext", 2500),
          ("callingPhoneContext", 2600),
          ("sipUsername", 2700),
          ("calledSipUsername", 2800),
          ("callingSipUsername", 2900),
          ("lastDivertingReason", 3000),
          ("lastDivertingE164", 3100),
          ("lastDivertingPartyNumberType", 3110),
          ("lastDivertingPublicTypeOfNumber", 3120),
          ("lastDivertingPrivateTypeOfNumber", 3130),
          ("lastDivertingNumberPresentation", 3140),
          ("originalDivertingReason", 3200),
          ("originalDivertingE164", 3300),
          ("originalDivertingPartyNumberType", 3400),
          ("originalDivertingPublicTypeOfNumber", 3500),
          ("originalDivertingPrivateTypeOfNumber", 3600),
          ("originalDivertingNumberPresentation", 3700),
          ("calledBearerChannel", 3800),
          ("callingBearerChannel", 3900),
          ("callingSipPrivacy", 4000))
    )


_MappingTypeCriteria_Type.__name__ = "Integer32"
_MappingTypeCriteria_Object = MibTableColumn
mappingTypeCriteria = _MappingTypeCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1, 300),
    _MappingTypeCriteria_Type()
)
mappingTypeCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingTypeCriteria.setStatus("current")


class _MappingTypeTransformation_Type(Integer32):
    """Custom type mappingTypeTransformation based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100,
              1200,
              1300,
              1400,
              1500,
              1600,
              1700,
              1800,
              1900,
              2000,
              2100,
              2200,
              2300,
              2400,
              2500,
              2600,
              2700,
              2800,
              2900,
              3000,
              3010,
              3020,
              3030,
              3040,
              3100,
              3200,
              3300,
              3400,
              3500,
              3600,
              3700,
              3800,
              60000)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("e164", 200),
          ("calledE164", 300),
          ("callingE164", 400),
          ("name", 500),
          ("calledName", 600),
          ("callingName", 700),
          ("ton", 800),
          ("calledTon", 900),
          ("callingTon", 1000),
          ("npi", 1100),
          ("calledNpi", 1200),
          ("callingNpi", 1300),
          ("host", 1400),
          ("calledHost", 1500),
          ("callingHost", 1600),
          ("callingPi", 1700),
          ("callingSi", 1800),
          ("callingItc", 1900),
          ("uri", 2000),
          ("calledUri", 2100),
          ("callingUri", 2200),
          ("phoneContext", 2300),
          ("calledPhoneContext", 2400),
          ("callingPhoneContext", 2500),
          ("sipUsername", 2600),
          ("calledSipUsername", 2700),
          ("callingSipUsername", 2800),
          ("lastDivertingReason", 2900),
          ("lastDivertingE164", 3000),
          ("lastDivertingPartyNumberType", 3010),
          ("lastDivertingPublicTypeOfNumber", 3020),
          ("lastDivertingPrivateTypeOfNumber", 3030),
          ("lastDivertingNumberPresentation", 3040),
          ("originalDivertingReason", 3100),
          ("originalDivertingE164", 3200),
          ("originalDivertingPartyNumberType", 3300),
          ("originalDivertingPublicTypeOfNumber", 3400),
          ("originalDivertingPrivateTypeOfNumber", 3500),
          ("originalDivertingNumberPresentation", 3600),
          ("calledBearerChannel", 3700),
          ("callingBearerChannel", 3800),
          ("debug", 60000))
    )


_MappingTypeTransformation_Type.__name__ = "Integer32"
_MappingTypeTransformation_Object = MibTableColumn
mappingTypeTransformation = _MappingTypeTransformation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1, 400),
    _MappingTypeTransformation_Type()
)
mappingTypeTransformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingTypeTransformation.setStatus("current")
_MappingTypeConfigStatus_Type = OctetString
_MappingTypeConfigStatus_Object = MibTableColumn
mappingTypeConfigStatus = _MappingTypeConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1, 500),
    _MappingTypeConfigStatus_Type()
)
mappingTypeConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingTypeConfigStatus.setStatus("current")


class _MappingTypeUp_Type(Integer32):
    """Custom type mappingTypeUp based on Integer32"""
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
          ("up", 10))
    )


_MappingTypeUp_Type.__name__ = "Integer32"
_MappingTypeUp_Object = MibTableColumn
mappingTypeUp = _MappingTypeUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1, 600),
    _MappingTypeUp_Type()
)
mappingTypeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingTypeUp.setStatus("current")


class _MappingTypeDown_Type(Integer32):
    """Custom type mappingTypeDown based on Integer32"""
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
          ("down", 10))
    )


_MappingTypeDown_Type.__name__ = "Integer32"
_MappingTypeDown_Object = MibTableColumn
mappingTypeDown = _MappingTypeDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1, 700),
    _MappingTypeDown_Type()
)
mappingTypeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingTypeDown.setStatus("current")


class _MappingTypeInsert_Type(Integer32):
    """Custom type mappingTypeInsert based on Integer32"""
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
          ("insert", 10))
    )


_MappingTypeInsert_Type.__name__ = "Integer32"
_MappingTypeInsert_Object = MibTableColumn
mappingTypeInsert = _MappingTypeInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1, 800),
    _MappingTypeInsert_Type()
)
mappingTypeInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingTypeInsert.setStatus("current")


class _MappingTypeDelete_Type(Integer32):
    """Custom type mappingTypeDelete based on Integer32"""
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
          ("delete", 10))
    )


_MappingTypeDelete_Type.__name__ = "Integer32"
_MappingTypeDelete_Object = MibTableColumn
mappingTypeDelete = _MappingTypeDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 500, 1, 900),
    _MappingTypeDelete_Type()
)
mappingTypeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingTypeDelete.setStatus("current")
_MappingExpressionTable_Object = MibTable
mappingExpressionTable = _MappingExpressionTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700)
)
if mibBuilder.loadTexts:
    mappingExpressionTable.setStatus("current")
_MappingExpressionEntry_Object = MibTableRow
mappingExpressionEntry = _MappingExpressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1)
)
mappingExpressionEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "mappingExpressionIndex"),
)
if mibBuilder.loadTexts:
    mappingExpressionEntry.setStatus("current")
_MappingExpressionIndex_Type = Unsigned32
_MappingExpressionIndex_Object = MibTableColumn
mappingExpressionIndex = _MappingExpressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 100),
    _MappingExpressionIndex_Type()
)
mappingExpressionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingExpressionIndex.setStatus("current")


class _MappingExpressionName_Type(OctetString):
    """Custom type mappingExpressionName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MappingExpressionName_Type.__name__ = "OctetString"
_MappingExpressionName_Object = MibTableColumn
mappingExpressionName = _MappingExpressionName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 200),
    _MappingExpressionName_Type()
)
mappingExpressionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingExpressionName.setStatus("current")


class _MappingExpressionCriteria_Type(OctetString):
    """Custom type mappingExpressionCriteria based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_MappingExpressionCriteria_Type.__name__ = "OctetString"
_MappingExpressionCriteria_Object = MibTableColumn
mappingExpressionCriteria = _MappingExpressionCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 300),
    _MappingExpressionCriteria_Type()
)
mappingExpressionCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingExpressionCriteria.setStatus("current")


class _MappingExpressionTransformation_Type(OctetString):
    """Custom type mappingExpressionTransformation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MappingExpressionTransformation_Type.__name__ = "OctetString"
_MappingExpressionTransformation_Object = MibTableColumn
mappingExpressionTransformation = _MappingExpressionTransformation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 400),
    _MappingExpressionTransformation_Type()
)
mappingExpressionTransformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingExpressionTransformation.setStatus("current")


class _MappingExpressionSubMappings_Type(OctetString):
    """Custom type mappingExpressionSubMappings based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MappingExpressionSubMappings_Type.__name__ = "OctetString"
_MappingExpressionSubMappings_Object = MibTableColumn
mappingExpressionSubMappings = _MappingExpressionSubMappings_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 500),
    _MappingExpressionSubMappings_Type()
)
mappingExpressionSubMappings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingExpressionSubMappings.setStatus("current")
_MappingExpressionConfigStatus_Type = OctetString
_MappingExpressionConfigStatus_Object = MibTableColumn
mappingExpressionConfigStatus = _MappingExpressionConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 600),
    _MappingExpressionConfigStatus_Type()
)
mappingExpressionConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mappingExpressionConfigStatus.setStatus("current")


class _MappingExpressionUp_Type(Integer32):
    """Custom type mappingExpressionUp based on Integer32"""
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
          ("up", 10))
    )


_MappingExpressionUp_Type.__name__ = "Integer32"
_MappingExpressionUp_Object = MibTableColumn
mappingExpressionUp = _MappingExpressionUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 700),
    _MappingExpressionUp_Type()
)
mappingExpressionUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingExpressionUp.setStatus("current")


class _MappingExpressionDown_Type(Integer32):
    """Custom type mappingExpressionDown based on Integer32"""
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
          ("down", 10))
    )


_MappingExpressionDown_Type.__name__ = "Integer32"
_MappingExpressionDown_Object = MibTableColumn
mappingExpressionDown = _MappingExpressionDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 800),
    _MappingExpressionDown_Type()
)
mappingExpressionDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingExpressionDown.setStatus("current")


class _MappingExpressionInsert_Type(Integer32):
    """Custom type mappingExpressionInsert based on Integer32"""
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
          ("insert", 10))
    )


_MappingExpressionInsert_Type.__name__ = "Integer32"
_MappingExpressionInsert_Object = MibTableColumn
mappingExpressionInsert = _MappingExpressionInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 900),
    _MappingExpressionInsert_Type()
)
mappingExpressionInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingExpressionInsert.setStatus("current")


class _MappingExpressionDelete_Type(Integer32):
    """Custom type mappingExpressionDelete based on Integer32"""
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
          ("delete", 10))
    )


_MappingExpressionDelete_Type.__name__ = "Integer32"
_MappingExpressionDelete_Object = MibTableColumn
mappingExpressionDelete = _MappingExpressionDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 700, 1, 1000),
    _MappingExpressionDelete_Type()
)
mappingExpressionDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingExpressionDelete.setStatus("current")
_HuntTable_Object = MibTable
huntTable = _HuntTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900)
)
if mibBuilder.loadTexts:
    huntTable.setStatus("current")
_HuntEntry_Object = MibTableRow
huntEntry = _HuntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1)
)
huntEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "huntIndex"),
)
if mibBuilder.loadTexts:
    huntEntry.setStatus("current")
_HuntIndex_Type = Unsigned32
_HuntIndex_Object = MibTableColumn
huntIndex = _HuntIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 100),
    _HuntIndex_Type()
)
huntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    huntIndex.setStatus("current")


class _HuntName_Type(OctetString):
    """Custom type huntName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HuntName_Type.__name__ = "OctetString"
_HuntName_Object = MibTableColumn
huntName = _HuntName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 200),
    _HuntName_Type()
)
huntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntName.setStatus("current")


class _HuntDestinations_Type(OctetString):
    """Custom type huntDestinations based on OctetString"""
    defaultValue = OctetString("")


_HuntDestinations_Type.__name__ = "OctetString"
_HuntDestinations_Object = MibTableColumn
huntDestinations = _HuntDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 300),
    _HuntDestinations_Type()
)
huntDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntDestinations.setStatus("current")


class _HuntSelectionAlgorithm_Type(Integer32):
    """Custom type huntSelectionAlgorithm based on Integer32"""
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
        *(("sequential", 100),
          ("cyclic", 200),
          ("simultaneous", 300))
    )


_HuntSelectionAlgorithm_Type.__name__ = "Integer32"
_HuntSelectionAlgorithm_Object = MibTableColumn
huntSelectionAlgorithm = _HuntSelectionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 400),
    _HuntSelectionAlgorithm_Type()
)
huntSelectionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntSelectionAlgorithm.setStatus("current")


class _HuntTimeout_Type(Unsigned32):
    """Custom type huntTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HuntTimeout_Type.__name__ = "Unsigned32"
_HuntTimeout_Object = MibTableColumn
huntTimeout = _HuntTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 500),
    _HuntTimeout_Type()
)
huntTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntTimeout.setStatus("current")


class _HuntCauses_Type(OctetString):
    """Custom type huntCauses based on OctetString"""
    defaultValue = OctetString("31, 34, 38, 41, 42, 43, 44, 47")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HuntCauses_Type.__name__ = "OctetString"
_HuntCauses_Object = MibTableColumn
huntCauses = _HuntCauses_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 600),
    _HuntCauses_Type()
)
huntCauses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntCauses.setStatus("current")
_HuntConfigStatus_Type = OctetString
_HuntConfigStatus_Object = MibTableColumn
huntConfigStatus = _HuntConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 700),
    _HuntConfigStatus_Type()
)
huntConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    huntConfigStatus.setStatus("current")


class _HuntUp_Type(Integer32):
    """Custom type huntUp based on Integer32"""
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
          ("up", 10))
    )


_HuntUp_Type.__name__ = "Integer32"
_HuntUp_Object = MibTableColumn
huntUp = _HuntUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 800),
    _HuntUp_Type()
)
huntUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntUp.setStatus("current")


class _HuntDown_Type(Integer32):
    """Custom type huntDown based on Integer32"""
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
          ("down", 10))
    )


_HuntDown_Type.__name__ = "Integer32"
_HuntDown_Object = MibTableColumn
huntDown = _HuntDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 900),
    _HuntDown_Type()
)
huntDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntDown.setStatus("current")


class _HuntInsert_Type(Integer32):
    """Custom type huntInsert based on Integer32"""
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
          ("insert", 10))
    )


_HuntInsert_Type.__name__ = "Integer32"
_HuntInsert_Object = MibTableColumn
huntInsert = _HuntInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 1000),
    _HuntInsert_Type()
)
huntInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntInsert.setStatus("current")


class _HuntDelete_Type(Integer32):
    """Custom type huntDelete based on Integer32"""
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
          ("delete", 10))
    )


_HuntDelete_Type.__name__ = "Integer32"
_HuntDelete_Object = MibTableColumn
huntDelete = _HuntDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 900, 1, 1100),
    _HuntDelete_Type()
)
huntDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    huntDelete.setStatus("current")
_SignalingPropertiesTable_Object = MibTable
signalingPropertiesTable = _SignalingPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200)
)
if mibBuilder.loadTexts:
    signalingPropertiesTable.setStatus("current")
_SignalingPropertiesEntry_Object = MibTableRow
signalingPropertiesEntry = _SignalingPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1)
)
signalingPropertiesEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "signalingPropertiesIndex"),
)
if mibBuilder.loadTexts:
    signalingPropertiesEntry.setStatus("current")
_SignalingPropertiesIndex_Type = Unsigned32
_SignalingPropertiesIndex_Object = MibTableColumn
signalingPropertiesIndex = _SignalingPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 100),
    _SignalingPropertiesIndex_Type()
)
signalingPropertiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesIndex.setStatus("current")


class _SignalingPropertiesName_Type(OctetString):
    """Custom type signalingPropertiesName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SignalingPropertiesName_Type.__name__ = "OctetString"
_SignalingPropertiesName_Object = MibTableColumn
signalingPropertiesName = _SignalingPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 200),
    _SignalingPropertiesName_Type()
)
signalingPropertiesName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesName.setStatus("current")


class _SignalingPropertiesEarlyConnect_Type(MxEnableState):
    """Custom type signalingPropertiesEarlyConnect based on MxEnableState"""
    defaultValue = 0


_SignalingPropertiesEarlyConnect_Type.__name__ = "MxEnableState"
_SignalingPropertiesEarlyConnect_Object = MibTableColumn
signalingPropertiesEarlyConnect = _SignalingPropertiesEarlyConnect_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 300),
    _SignalingPropertiesEarlyConnect_Type()
)
signalingPropertiesEarlyConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesEarlyConnect.setStatus("current")


class _SignalingPropertiesEarlyDisconnect_Type(MxEnableState):
    """Custom type signalingPropertiesEarlyDisconnect based on MxEnableState"""
    defaultValue = 0


_SignalingPropertiesEarlyDisconnect_Type.__name__ = "MxEnableState"
_SignalingPropertiesEarlyDisconnect_Object = MibTableColumn
signalingPropertiesEarlyDisconnect = _SignalingPropertiesEarlyDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 400),
    _SignalingPropertiesEarlyDisconnect_Type()
)
signalingPropertiesEarlyDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesEarlyDisconnect.setStatus("current")


class _SignalingPropertiesDestinationHost_Type(OctetString):
    """Custom type signalingPropertiesDestinationHost based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SignalingPropertiesDestinationHost_Type.__name__ = "OctetString"
_SignalingPropertiesDestinationHost_Object = MibTableColumn
signalingPropertiesDestinationHost = _SignalingPropertiesDestinationHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 500),
    _SignalingPropertiesDestinationHost_Type()
)
signalingPropertiesDestinationHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesDestinationHost.setStatus("current")


class _SignalingPropertiesAllow180Sdp_Type(MxEnableState):
    """Custom type signalingPropertiesAllow180Sdp based on MxEnableState"""
    defaultValue = 1


_SignalingPropertiesAllow180Sdp_Type.__name__ = "MxEnableState"
_SignalingPropertiesAllow180Sdp_Object = MibTableColumn
signalingPropertiesAllow180Sdp = _SignalingPropertiesAllow180Sdp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 550),
    _SignalingPropertiesAllow180Sdp_Type()
)
signalingPropertiesAllow180Sdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesAllow180Sdp.setStatus("current")


class _SignalingPropertiesAllow183NoSdp_Type(MxEnableState):
    """Custom type signalingPropertiesAllow183NoSdp based on MxEnableState"""
    defaultValue = 1


_SignalingPropertiesAllow183NoSdp_Type.__name__ = "MxEnableState"
_SignalingPropertiesAllow183NoSdp_Object = MibTableColumn
signalingPropertiesAllow183NoSdp = _SignalingPropertiesAllow183NoSdp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 560),
    _SignalingPropertiesAllow183NoSdp_Type()
)
signalingPropertiesAllow183NoSdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesAllow183NoSdp.setStatus("current")


class _SignalingPropertiesPrivacy_Type(Integer32):
    """Custom type signalingPropertiesPrivacy based on Integer32"""
    defaultValue = 100

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
        *(("disable", 100),
          ("none", 200),
          ("id", 300),
          ("rpid", 400))
    )


_SignalingPropertiesPrivacy_Type.__name__ = "Integer32"
_SignalingPropertiesPrivacy_Object = MibTableColumn
signalingPropertiesPrivacy = _SignalingPropertiesPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 570),
    _SignalingPropertiesPrivacy_Type()
)
signalingPropertiesPrivacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesPrivacy.setStatus("current")


class _SignalingPropertiesCallPropertiesTranslation_Type(OctetString):
    """Custom type signalingPropertiesCallPropertiesTranslation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SignalingPropertiesCallPropertiesTranslation_Type.__name__ = "OctetString"
_SignalingPropertiesCallPropertiesTranslation_Object = MibTableColumn
signalingPropertiesCallPropertiesTranslation = _SignalingPropertiesCallPropertiesTranslation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 580),
    _SignalingPropertiesCallPropertiesTranslation_Type()
)
signalingPropertiesCallPropertiesTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesCallPropertiesTranslation.setStatus("current")


class _SignalingPropertiesSipHeadersTranslation_Type(OctetString):
    """Custom type signalingPropertiesSipHeadersTranslation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SignalingPropertiesSipHeadersTranslation_Type.__name__ = "OctetString"
_SignalingPropertiesSipHeadersTranslation_Object = MibTableColumn
signalingPropertiesSipHeadersTranslation = _SignalingPropertiesSipHeadersTranslation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 590),
    _SignalingPropertiesSipHeadersTranslation_Type()
)
signalingPropertiesSipHeadersTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesSipHeadersTranslation.setStatus("current")
_SignalingPropertiesConfigStatus_Type = OctetString
_SignalingPropertiesConfigStatus_Object = MibTableColumn
signalingPropertiesConfigStatus = _SignalingPropertiesConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 600),
    _SignalingPropertiesConfigStatus_Type()
)
signalingPropertiesConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingPropertiesConfigStatus.setStatus("current")


class _SignalingPropertiesUp_Type(Integer32):
    """Custom type signalingPropertiesUp based on Integer32"""
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
          ("up", 10))
    )


_SignalingPropertiesUp_Type.__name__ = "Integer32"
_SignalingPropertiesUp_Object = MibTableColumn
signalingPropertiesUp = _SignalingPropertiesUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 700),
    _SignalingPropertiesUp_Type()
)
signalingPropertiesUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesUp.setStatus("current")


class _SignalingPropertiesDown_Type(Integer32):
    """Custom type signalingPropertiesDown based on Integer32"""
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
          ("down", 10))
    )


_SignalingPropertiesDown_Type.__name__ = "Integer32"
_SignalingPropertiesDown_Object = MibTableColumn
signalingPropertiesDown = _SignalingPropertiesDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 800),
    _SignalingPropertiesDown_Type()
)
signalingPropertiesDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesDown.setStatus("current")


class _SignalingPropertiesInsert_Type(Integer32):
    """Custom type signalingPropertiesInsert based on Integer32"""
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
          ("insert", 10))
    )


_SignalingPropertiesInsert_Type.__name__ = "Integer32"
_SignalingPropertiesInsert_Object = MibTableColumn
signalingPropertiesInsert = _SignalingPropertiesInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 900),
    _SignalingPropertiesInsert_Type()
)
signalingPropertiesInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesInsert.setStatus("current")


class _SignalingPropertiesDelete_Type(Integer32):
    """Custom type signalingPropertiesDelete based on Integer32"""
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
          ("delete", 10))
    )


_SignalingPropertiesDelete_Type.__name__ = "Integer32"
_SignalingPropertiesDelete_Object = MibTableColumn
signalingPropertiesDelete = _SignalingPropertiesDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1200, 1, 1000),
    _SignalingPropertiesDelete_Type()
)
signalingPropertiesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingPropertiesDelete.setStatus("current")
_SipHeadersTranslationTable_Object = MibTable
sipHeadersTranslationTable = _SipHeadersTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400)
)
if mibBuilder.loadTexts:
    sipHeadersTranslationTable.setStatus("current")
_SipHeadersTranslationEntry_Object = MibTableRow
sipHeadersTranslationEntry = _SipHeadersTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1)
)
sipHeadersTranslationEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "sipHeadersTranslationIndex"),
)
if mibBuilder.loadTexts:
    sipHeadersTranslationEntry.setStatus("current")
_SipHeadersTranslationIndex_Type = Unsigned32
_SipHeadersTranslationIndex_Object = MibTableColumn
sipHeadersTranslationIndex = _SipHeadersTranslationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 100),
    _SipHeadersTranslationIndex_Type()
)
sipHeadersTranslationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipHeadersTranslationIndex.setStatus("current")


class _SipHeadersTranslationName_Type(OctetString):
    """Custom type sipHeadersTranslationName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SipHeadersTranslationName_Type.__name__ = "OctetString"
_SipHeadersTranslationName_Object = MibTableColumn
sipHeadersTranslationName = _SipHeadersTranslationName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 200),
    _SipHeadersTranslationName_Type()
)
sipHeadersTranslationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHeadersTranslationName.setStatus("current")


class _SipHeadersTranslationSipHeader_Type(Integer32):
    """Custom type sipHeadersTranslationSipHeader based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              550,
              600,
              700,
              800,
              900)
        )
    )
    namedValues = NamedValues(
        *(("fromHeaderHostPart", 100),
          ("fromHeaderUserPart", 200),
          ("identityHeaderHostPart", 300),
          ("identityHeaderUserPart", 400),
          ("identityHeaderPhoneNumber", 500),
          ("identityHeaderFriendlyName", 550),
          ("requestLineHostPart", 600),
          ("requestLineUserPart", 700),
          ("toHeaderHostPart", 800),
          ("toHeaderUserPart", 900))
    )


_SipHeadersTranslationSipHeader_Type.__name__ = "Integer32"
_SipHeadersTranslationSipHeader_Object = MibTableColumn
sipHeadersTranslationSipHeader = _SipHeadersTranslationSipHeader_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 300),
    _SipHeadersTranslationSipHeader_Type()
)
sipHeadersTranslationSipHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHeadersTranslationSipHeader.setStatus("current")


class _SipHeadersTranslationBuiltFrom_Type(Integer32):
    """Custom type sipHeadersTranslationBuiltFrom based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("calledE164", 100),
          ("destinationHost", 200),
          ("domain", 300),
          ("fixValue", 400),
          ("hostName", 500),
          ("localIp", 600),
          ("callingBearerChannel", 700),
          ("sipEndpointUsername", 800),
          ("callingName", 900),
          ("callingE164", 1000))
    )


_SipHeadersTranslationBuiltFrom_Type.__name__ = "Integer32"
_SipHeadersTranslationBuiltFrom_Object = MibTableColumn
sipHeadersTranslationBuiltFrom = _SipHeadersTranslationBuiltFrom_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 400),
    _SipHeadersTranslationBuiltFrom_Type()
)
sipHeadersTranslationBuiltFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHeadersTranslationBuiltFrom.setStatus("current")


class _SipHeadersTranslationFixValue_Type(OctetString):
    """Custom type sipHeadersTranslationFixValue based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipHeadersTranslationFixValue_Type.__name__ = "OctetString"
_SipHeadersTranslationFixValue_Object = MibTableColumn
sipHeadersTranslationFixValue = _SipHeadersTranslationFixValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 500),
    _SipHeadersTranslationFixValue_Type()
)
sipHeadersTranslationFixValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHeadersTranslationFixValue.setStatus("current")
_SipHeadersTranslationConfigStatus_Type = OctetString
_SipHeadersTranslationConfigStatus_Object = MibTableColumn
sipHeadersTranslationConfigStatus = _SipHeadersTranslationConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 600),
    _SipHeadersTranslationConfigStatus_Type()
)
sipHeadersTranslationConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipHeadersTranslationConfigStatus.setStatus("current")


class _SipHeadersTranslationUp_Type(Integer32):
    """Custom type sipHeadersTranslationUp based on Integer32"""
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
          ("up", 10))
    )


_SipHeadersTranslationUp_Type.__name__ = "Integer32"
_SipHeadersTranslationUp_Object = MibTableColumn
sipHeadersTranslationUp = _SipHeadersTranslationUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 700),
    _SipHeadersTranslationUp_Type()
)
sipHeadersTranslationUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHeadersTranslationUp.setStatus("current")


class _SipHeadersTranslationDown_Type(Integer32):
    """Custom type sipHeadersTranslationDown based on Integer32"""
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
          ("down", 10))
    )


_SipHeadersTranslationDown_Type.__name__ = "Integer32"
_SipHeadersTranslationDown_Object = MibTableColumn
sipHeadersTranslationDown = _SipHeadersTranslationDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 800),
    _SipHeadersTranslationDown_Type()
)
sipHeadersTranslationDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHeadersTranslationDown.setStatus("current")


class _SipHeadersTranslationInsert_Type(Integer32):
    """Custom type sipHeadersTranslationInsert based on Integer32"""
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
          ("insert", 10))
    )


_SipHeadersTranslationInsert_Type.__name__ = "Integer32"
_SipHeadersTranslationInsert_Object = MibTableColumn
sipHeadersTranslationInsert = _SipHeadersTranslationInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 900),
    _SipHeadersTranslationInsert_Type()
)
sipHeadersTranslationInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHeadersTranslationInsert.setStatus("current")


class _SipHeadersTranslationDelete_Type(Integer32):
    """Custom type sipHeadersTranslationDelete based on Integer32"""
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
          ("delete", 10))
    )


_SipHeadersTranslationDelete_Type.__name__ = "Integer32"
_SipHeadersTranslationDelete_Object = MibTableColumn
sipHeadersTranslationDelete = _SipHeadersTranslationDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1400, 1, 1000),
    _SipHeadersTranslationDelete_Type()
)
sipHeadersTranslationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHeadersTranslationDelete.setStatus("current")
_CallPropertiesTranslationTable_Object = MibTable
callPropertiesTranslationTable = _CallPropertiesTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600)
)
if mibBuilder.loadTexts:
    callPropertiesTranslationTable.setStatus("current")
_CallPropertiesTranslationEntry_Object = MibTableRow
callPropertiesTranslationEntry = _CallPropertiesTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1)
)
callPropertiesTranslationEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "callPropertiesTranslationIndex"),
)
if mibBuilder.loadTexts:
    callPropertiesTranslationEntry.setStatus("current")
_CallPropertiesTranslationIndex_Type = Unsigned32
_CallPropertiesTranslationIndex_Object = MibTableColumn
callPropertiesTranslationIndex = _CallPropertiesTranslationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 100),
    _CallPropertiesTranslationIndex_Type()
)
callPropertiesTranslationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callPropertiesTranslationIndex.setStatus("current")


class _CallPropertiesTranslationName_Type(OctetString):
    """Custom type callPropertiesTranslationName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CallPropertiesTranslationName_Type.__name__ = "OctetString"
_CallPropertiesTranslationName_Object = MibTableColumn
callPropertiesTranslationName = _CallPropertiesTranslationName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 200),
    _CallPropertiesTranslationName_Type()
)
callPropertiesTranslationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callPropertiesTranslationName.setStatus("current")


class _CallPropertiesTranslationCallProperty_Type(Integer32):
    """Custom type callPropertiesTranslationCallProperty based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700)
        )
    )
    namedValues = NamedValues(
        *(("calledE164", 100),
          ("callingE164", 200),
          ("calledName", 300),
          ("callingName", 400),
          ("calledUri", 500),
          ("callingUri", 600),
          ("calledBearerChannel", 700))
    )


_CallPropertiesTranslationCallProperty_Type.__name__ = "Integer32"
_CallPropertiesTranslationCallProperty_Object = MibTableColumn
callPropertiesTranslationCallProperty = _CallPropertiesTranslationCallProperty_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 300),
    _CallPropertiesTranslationCallProperty_Type()
)
callPropertiesTranslationCallProperty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callPropertiesTranslationCallProperty.setStatus("current")


class _CallPropertiesTranslationBuiltFrom_Type(Integer32):
    """Custom type callPropertiesTranslationBuiltFrom based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              850,
              900,
              1000,
              1100,
              1200,
              1300,
              1400)
        )
    )
    namedValues = NamedValues(
        *(("domain", 100),
          ("fixValue", 200),
          ("fromHeaderUri", 300),
          ("fromHeaderFriendlyName", 400),
          ("fromHeaderUserPart", 500),
          ("identityHeaderUri", 600),
          ("identityHeaderUserPart", 700),
          ("identityHeaderPhoneNumber", 800),
          ("identityHeaderFriendlyName", 850),
          ("localIp", 900),
          ("requestLineUri", 1000),
          ("requestLineUserPart", 1100),
          ("toHeaderUri", 1200),
          ("toHeaderFriendlyName", 1300),
          ("toHeaderUserPart", 1400))
    )


_CallPropertiesTranslationBuiltFrom_Type.__name__ = "Integer32"
_CallPropertiesTranslationBuiltFrom_Object = MibTableColumn
callPropertiesTranslationBuiltFrom = _CallPropertiesTranslationBuiltFrom_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 400),
    _CallPropertiesTranslationBuiltFrom_Type()
)
callPropertiesTranslationBuiltFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callPropertiesTranslationBuiltFrom.setStatus("current")


class _CallPropertiesTranslationFixValue_Type(OctetString):
    """Custom type callPropertiesTranslationFixValue based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CallPropertiesTranslationFixValue_Type.__name__ = "OctetString"
_CallPropertiesTranslationFixValue_Object = MibTableColumn
callPropertiesTranslationFixValue = _CallPropertiesTranslationFixValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 500),
    _CallPropertiesTranslationFixValue_Type()
)
callPropertiesTranslationFixValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callPropertiesTranslationFixValue.setStatus("current")
_CallPropertiesTranslationConfigStatus_Type = OctetString
_CallPropertiesTranslationConfigStatus_Object = MibTableColumn
callPropertiesTranslationConfigStatus = _CallPropertiesTranslationConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 600),
    _CallPropertiesTranslationConfigStatus_Type()
)
callPropertiesTranslationConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callPropertiesTranslationConfigStatus.setStatus("current")


class _CallPropertiesTranslationUp_Type(Integer32):
    """Custom type callPropertiesTranslationUp based on Integer32"""
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
          ("up", 10))
    )


_CallPropertiesTranslationUp_Type.__name__ = "Integer32"
_CallPropertiesTranslationUp_Object = MibTableColumn
callPropertiesTranslationUp = _CallPropertiesTranslationUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 700),
    _CallPropertiesTranslationUp_Type()
)
callPropertiesTranslationUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callPropertiesTranslationUp.setStatus("current")


class _CallPropertiesTranslationDown_Type(Integer32):
    """Custom type callPropertiesTranslationDown based on Integer32"""
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
          ("down", 10))
    )


_CallPropertiesTranslationDown_Type.__name__ = "Integer32"
_CallPropertiesTranslationDown_Object = MibTableColumn
callPropertiesTranslationDown = _CallPropertiesTranslationDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 800),
    _CallPropertiesTranslationDown_Type()
)
callPropertiesTranslationDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callPropertiesTranslationDown.setStatus("current")


class _CallPropertiesTranslationInsert_Type(Integer32):
    """Custom type callPropertiesTranslationInsert based on Integer32"""
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
          ("insert", 10))
    )


_CallPropertiesTranslationInsert_Type.__name__ = "Integer32"
_CallPropertiesTranslationInsert_Object = MibTableColumn
callPropertiesTranslationInsert = _CallPropertiesTranslationInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 900),
    _CallPropertiesTranslationInsert_Type()
)
callPropertiesTranslationInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callPropertiesTranslationInsert.setStatus("current")


class _CallPropertiesTranslationDelete_Type(Integer32):
    """Custom type callPropertiesTranslationDelete based on Integer32"""
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
          ("delete", 10))
    )


_CallPropertiesTranslationDelete_Type.__name__ = "Integer32"
_CallPropertiesTranslationDelete_Object = MibTableColumn
callPropertiesTranslationDelete = _CallPropertiesTranslationDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1600, 1, 1000),
    _CallPropertiesTranslationDelete_Type()
)
callPropertiesTranslationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callPropertiesTranslationDelete.setStatus("current")
_AutoRoutingTable_Object = MibTable
autoRoutingTable = _AutoRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1900)
)
if mibBuilder.loadTexts:
    autoRoutingTable.setStatus("current")
_AutoRoutingEntry_Object = MibTableRow
autoRoutingEntry = _AutoRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1900, 1)
)
autoRoutingEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "autoRoutingEpId"),
)
if mibBuilder.loadTexts:
    autoRoutingEntry.setStatus("current")
_AutoRoutingEpId_Type = OctetString
_AutoRoutingEpId_Object = MibTableColumn
autoRoutingEpId = _AutoRoutingEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1900, 1, 100),
    _AutoRoutingEpId_Type()
)
autoRoutingEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoRoutingEpId.setStatus("current")


class _AutoRoutingAutoroutable_Type(Integer32):
    """Custom type autoRoutingAutoroutable based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("enable", 100),
          ("disable", 200),
          ("hardwareDependent", 300))
    )


_AutoRoutingAutoroutable_Type.__name__ = "Integer32"
_AutoRoutingAutoroutable_Object = MibTableColumn
autoRoutingAutoroutable = _AutoRoutingAutoroutable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1900, 1, 200),
    _AutoRoutingAutoroutable_Type()
)
autoRoutingAutoroutable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRoutingAutoroutable.setStatus("current")


class _AutoRoutingAutoRoutingGateway_Type(OctetString):
    """Custom type autoRoutingAutoRoutingGateway based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AutoRoutingAutoRoutingGateway_Type.__name__ = "OctetString"
_AutoRoutingAutoRoutingGateway_Object = MibTableColumn
autoRoutingAutoRoutingGateway = _AutoRoutingAutoRoutingGateway_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1900, 1, 300),
    _AutoRoutingAutoRoutingGateway_Type()
)
autoRoutingAutoRoutingGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRoutingAutoRoutingGateway.setStatus("current")


class _AutoRoutingAutoRoutingDestination_Type(OctetString):
    """Custom type autoRoutingAutoRoutingDestination based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AutoRoutingAutoRoutingDestination_Type.__name__ = "OctetString"
_AutoRoutingAutoRoutingDestination_Object = MibTableColumn
autoRoutingAutoRoutingDestination = _AutoRoutingAutoRoutingDestination_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1900, 1, 350),
    _AutoRoutingAutoRoutingDestination_Type()
)
autoRoutingAutoRoutingDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRoutingAutoRoutingDestination.setStatus("current")


class _AutoRoutingE164_Type(OctetString):
    """Custom type autoRoutingE164 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AutoRoutingE164_Type.__name__ = "OctetString"
_AutoRoutingE164_Object = MibTableColumn
autoRoutingE164 = _AutoRoutingE164_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1900, 1, 400),
    _AutoRoutingE164_Type()
)
autoRoutingE164.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoRoutingE164.setStatus("current")


class _AutoRoutingSipUsername_Type(OctetString):
    """Custom type autoRoutingSipUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AutoRoutingSipUsername_Type.__name__ = "OctetString"
_AutoRoutingSipUsername_Object = MibTableColumn
autoRoutingSipUsername = _AutoRoutingSipUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1900, 1, 450),
    _AutoRoutingSipUsername_Type()
)
autoRoutingSipUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoRoutingSipUsername.setStatus("current")


class _AutoRoutingName_Type(OctetString):
    """Custom type autoRoutingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AutoRoutingName_Type.__name__ = "OctetString"
_AutoRoutingName_Object = MibTableColumn
autoRoutingName = _AutoRoutingName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 1900, 1, 500),
    _AutoRoutingName_Type()
)
autoRoutingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoRoutingName.setStatus("current")


class _AutoRoutingCriteriaType_Type(Integer32):
    """Custom type autoRoutingCriteriaType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("e164", 100),
          ("sipUsername", 200))
    )


_AutoRoutingCriteriaType_Type.__name__ = "Integer32"
_AutoRoutingCriteriaType_Object = MibScalar
autoRoutingCriteriaType = _AutoRoutingCriteriaType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2000),
    _AutoRoutingCriteriaType_Type()
)
autoRoutingCriteriaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRoutingCriteriaType.setStatus("current")


class _AutoRoutingIncomingMappings_Type(OctetString):
    """Custom type autoRoutingIncomingMappings based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AutoRoutingIncomingMappings_Type.__name__ = "OctetString"
_AutoRoutingIncomingMappings_Object = MibScalar
autoRoutingIncomingMappings = _AutoRoutingIncomingMappings_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2100),
    _AutoRoutingIncomingMappings_Type()
)
autoRoutingIncomingMappings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRoutingIncomingMappings.setStatus("current")


class _AutoRoutingOutgoingMappings_Type(OctetString):
    """Custom type autoRoutingOutgoingMappings based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AutoRoutingOutgoingMappings_Type.__name__ = "OctetString"
_AutoRoutingOutgoingMappings_Object = MibScalar
autoRoutingOutgoingMappings = _AutoRoutingOutgoingMappings_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2200),
    _AutoRoutingOutgoingMappings_Type()
)
autoRoutingOutgoingMappings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRoutingOutgoingMappings.setStatus("current")


class _AutoRoutingIncomingSignalingProperties_Type(OctetString):
    """Custom type autoRoutingIncomingSignalingProperties based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AutoRoutingIncomingSignalingProperties_Type.__name__ = "OctetString"
_AutoRoutingIncomingSignalingProperties_Object = MibScalar
autoRoutingIncomingSignalingProperties = _AutoRoutingIncomingSignalingProperties_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2300),
    _AutoRoutingIncomingSignalingProperties_Type()
)
autoRoutingIncomingSignalingProperties.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRoutingIncomingSignalingProperties.setStatus("current")


class _AutoRoutingOutgoingSignalingProperties_Type(OctetString):
    """Custom type autoRoutingOutgoingSignalingProperties based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AutoRoutingOutgoingSignalingProperties_Type.__name__ = "OctetString"
_AutoRoutingOutgoingSignalingProperties_Object = MibScalar
autoRoutingOutgoingSignalingProperties = _AutoRoutingOutgoingSignalingProperties_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2400),
    _AutoRoutingOutgoingSignalingProperties_Type()
)
autoRoutingOutgoingSignalingProperties.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoRoutingOutgoingSignalingProperties.setStatus("current")
_SipRedirectTable_Object = MibTable
sipRedirectTable = _SipRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500)
)
if mibBuilder.loadTexts:
    sipRedirectTable.setStatus("current")
_SipRedirectEntry_Object = MibTableRow
sipRedirectEntry = _SipRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500, 1)
)
sipRedirectEntry.setIndexNames(
    (0, "MX-CROUT-MIB", "sipRedirectIndex"),
)
if mibBuilder.loadTexts:
    sipRedirectEntry.setStatus("current")
_SipRedirectIndex_Type = Unsigned32
_SipRedirectIndex_Object = MibTableColumn
sipRedirectIndex = _SipRedirectIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500, 1, 100),
    _SipRedirectIndex_Type()
)
sipRedirectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRedirectIndex.setStatus("current")


class _SipRedirectName_Type(OctetString):
    """Custom type sipRedirectName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SipRedirectName_Type.__name__ = "OctetString"
_SipRedirectName_Object = MibTableColumn
sipRedirectName = _SipRedirectName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500, 1, 200),
    _SipRedirectName_Type()
)
sipRedirectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRedirectName.setStatus("current")


class _SipRedirectDestinationHost_Type(OctetString):
    """Custom type sipRedirectDestinationHost based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SipRedirectDestinationHost_Type.__name__ = "OctetString"
_SipRedirectDestinationHost_Object = MibTableColumn
sipRedirectDestinationHost = _SipRedirectDestinationHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500, 1, 300),
    _SipRedirectDestinationHost_Type()
)
sipRedirectDestinationHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRedirectDestinationHost.setStatus("current")
_SipRedirectConfigStatus_Type = OctetString
_SipRedirectConfigStatus_Object = MibTableColumn
sipRedirectConfigStatus = _SipRedirectConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500, 1, 400),
    _SipRedirectConfigStatus_Type()
)
sipRedirectConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRedirectConfigStatus.setStatus("current")


class _SipRedirectUp_Type(Integer32):
    """Custom type sipRedirectUp based on Integer32"""
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
          ("up", 10))
    )


_SipRedirectUp_Type.__name__ = "Integer32"
_SipRedirectUp_Object = MibTableColumn
sipRedirectUp = _SipRedirectUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500, 1, 500),
    _SipRedirectUp_Type()
)
sipRedirectUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRedirectUp.setStatus("current")


class _SipRedirectDown_Type(Integer32):
    """Custom type sipRedirectDown based on Integer32"""
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
          ("down", 10))
    )


_SipRedirectDown_Type.__name__ = "Integer32"
_SipRedirectDown_Object = MibTableColumn
sipRedirectDown = _SipRedirectDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500, 1, 600),
    _SipRedirectDown_Type()
)
sipRedirectDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRedirectDown.setStatus("current")


class _SipRedirectInsert_Type(Integer32):
    """Custom type sipRedirectInsert based on Integer32"""
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
          ("insert", 10))
    )


_SipRedirectInsert_Type.__name__ = "Integer32"
_SipRedirectInsert_Object = MibTableColumn
sipRedirectInsert = _SipRedirectInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500, 1, 700),
    _SipRedirectInsert_Type()
)
sipRedirectInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRedirectInsert.setStatus("current")


class _SipRedirectDelete_Type(Integer32):
    """Custom type sipRedirectDelete based on Integer32"""
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
          ("delete", 10))
    )


_SipRedirectDelete_Type.__name__ = "Integer32"
_SipRedirectDelete_Object = MibTableColumn
sipRedirectDelete = _SipRedirectDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 2500, 1, 800),
    _SipRedirectDelete_Type()
)
sipRedirectDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRedirectDelete.setStatus("current")
_CallSimulationGroup_ObjectIdentity = ObjectIdentity
callSimulationGroup = _CallSimulationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 3000)
)
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1750, 1, 60020, 100),
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
    "MX-CROUT-MIB",
    **{"cRoutMIB": cRoutMIB,
       "cRoutMIBObjects": cRoutMIBObjects,
       "statusGroup": statusGroup,
       "configModifiedStatus": configModifiedStatus,
       "interfaceStatusTable": interfaceStatusTable,
       "interfaceStatusEntry": interfaceStatusEntry,
       "interfaceStatusIndex": interfaceStatusIndex,
       "interfaceStatusName": interfaceStatusName,
       "routeStatusTable": routeStatusTable,
       "routeStatusEntry": routeStatusEntry,
       "routeStatusIndex": routeStatusIndex,
       "routeStatusType": routeStatusType,
       "routeStatusSourceCriteria": routeStatusSourceCriteria,
       "routeStatusPropertiesCriteria": routeStatusPropertiesCriteria,
       "routeStatusExpressionCriteria": routeStatusExpressionCriteria,
       "routeStatusDestination": routeStatusDestination,
       "routeStatusMappings": routeStatusMappings,
       "routeStatusSignalingProperties": routeStatusSignalingProperties,
       "mappingTypeStatusTable": mappingTypeStatusTable,
       "mappingTypeStatusEntry": mappingTypeStatusEntry,
       "mappingTypeStatusIndex": mappingTypeStatusIndex,
       "mappingTypeStatusName": mappingTypeStatusName,
       "mappingTypeStatusCriteria": mappingTypeStatusCriteria,
       "mappingTypeStatusTransformation": mappingTypeStatusTransformation,
       "mappingExpressionStatusTable": mappingExpressionStatusTable,
       "mappingExpressionStatusEntry": mappingExpressionStatusEntry,
       "mappingExpressionStatusIndex": mappingExpressionStatusIndex,
       "mappingExpressionStatusName": mappingExpressionStatusName,
       "mappingExpressionStatusCriteria": mappingExpressionStatusCriteria,
       "mappingExpressionStatusTransformation": mappingExpressionStatusTransformation,
       "mappingExpressionStatusSubMappings": mappingExpressionStatusSubMappings,
       "huntStatusTable": huntStatusTable,
       "huntStatusEntry": huntStatusEntry,
       "huntStatusIndex": huntStatusIndex,
       "huntStatusName": huntStatusName,
       "huntStatusDestinations": huntStatusDestinations,
       "huntStatusSelectionAlgorithm": huntStatusSelectionAlgorithm,
       "huntStatusTimeout": huntStatusTimeout,
       "huntStatusCauses": huntStatusCauses,
       "signalingPropertiesStatusTable": signalingPropertiesStatusTable,
       "signalingPropertiesStatusEntry": signalingPropertiesStatusEntry,
       "signalingPropertiesStatusIndex": signalingPropertiesStatusIndex,
       "signalingPropertiesStatusName": signalingPropertiesStatusName,
       "signalingPropertiesStatusEarlyConnect": signalingPropertiesStatusEarlyConnect,
       "signalingPropertiesStatusEarlyDisconnect": signalingPropertiesStatusEarlyDisconnect,
       "signalingPropertiesStatusDestinationHost": signalingPropertiesStatusDestinationHost,
       "signalingPropertiesStatusAllow180Sdp": signalingPropertiesStatusAllow180Sdp,
       "signalingPropertiesStatusAllow183NoSdp": signalingPropertiesStatusAllow183NoSdp,
       "signalingPropertiesStatusPrivacy": signalingPropertiesStatusPrivacy,
       "signalingPropertiesStatusCallPropertiesTranslation": signalingPropertiesStatusCallPropertiesTranslation,
       "signalingPropertiesStatusSipHeadersTranslation": signalingPropertiesStatusSipHeadersTranslation,
       "sipHeadersTranslationStatusTable": sipHeadersTranslationStatusTable,
       "sipHeadersTranslationStatusEntry": sipHeadersTranslationStatusEntry,
       "sipHeadersTranslationStatusIndex": sipHeadersTranslationStatusIndex,
       "sipHeadersTranslationStatusName": sipHeadersTranslationStatusName,
       "sipHeadersTranslationStatusSipHeader": sipHeadersTranslationStatusSipHeader,
       "sipHeadersTranslationStatusBuiltFrom": sipHeadersTranslationStatusBuiltFrom,
       "sipHeadersTranslationStatusFixValue": sipHeadersTranslationStatusFixValue,
       "callPropertiesTranslationStatusTable": callPropertiesTranslationStatusTable,
       "callPropertiesTranslationStatusEntry": callPropertiesTranslationStatusEntry,
       "callPropertiesTranslationStatusIndex": callPropertiesTranslationStatusIndex,
       "callPropertiesTranslationStatusName": callPropertiesTranslationStatusName,
       "callPropertiesTranslationStatusCallProperty": callPropertiesTranslationStatusCallProperty,
       "callPropertiesTranslationStatusBuiltFrom": callPropertiesTranslationStatusBuiltFrom,
       "callPropertiesTranslationStatusFixValue": callPropertiesTranslationStatusFixValue,
       "sipRedirectStatusTable": sipRedirectStatusTable,
       "sipRedirectStatusEntry": sipRedirectStatusEntry,
       "sipRedirectStatusIndex": sipRedirectStatusIndex,
       "sipRedirectStatusName": sipRedirectStatusName,
       "sipRedirectStatusDestinationHost": sipRedirectStatusDestinationHost,
       "autoRoutingEnable": autoRoutingEnable,
       "routeTable": routeTable,
       "routeEntry": routeEntry,
       "routeIndex": routeIndex,
       "routeSourceCriteria": routeSourceCriteria,
       "routePropertiesCriteria": routePropertiesCriteria,
       "routeExpressionCriteria": routeExpressionCriteria,
       "routeDestination": routeDestination,
       "routeMappings": routeMappings,
       "routeSignalingProperties": routeSignalingProperties,
       "routeConfigStatus": routeConfigStatus,
       "routeUp": routeUp,
       "routeDown": routeDown,
       "routeInsert": routeInsert,
       "routeDelete": routeDelete,
       "mappingTypeTable": mappingTypeTable,
       "mappingTypeEntry": mappingTypeEntry,
       "mappingTypeIndex": mappingTypeIndex,
       "mappingTypeName": mappingTypeName,
       "mappingTypeCriteria": mappingTypeCriteria,
       "mappingTypeTransformation": mappingTypeTransformation,
       "mappingTypeConfigStatus": mappingTypeConfigStatus,
       "mappingTypeUp": mappingTypeUp,
       "mappingTypeDown": mappingTypeDown,
       "mappingTypeInsert": mappingTypeInsert,
       "mappingTypeDelete": mappingTypeDelete,
       "mappingExpressionTable": mappingExpressionTable,
       "mappingExpressionEntry": mappingExpressionEntry,
       "mappingExpressionIndex": mappingExpressionIndex,
       "mappingExpressionName": mappingExpressionName,
       "mappingExpressionCriteria": mappingExpressionCriteria,
       "mappingExpressionTransformation": mappingExpressionTransformation,
       "mappingExpressionSubMappings": mappingExpressionSubMappings,
       "mappingExpressionConfigStatus": mappingExpressionConfigStatus,
       "mappingExpressionUp": mappingExpressionUp,
       "mappingExpressionDown": mappingExpressionDown,
       "mappingExpressionInsert": mappingExpressionInsert,
       "mappingExpressionDelete": mappingExpressionDelete,
       "huntTable": huntTable,
       "huntEntry": huntEntry,
       "huntIndex": huntIndex,
       "huntName": huntName,
       "huntDestinations": huntDestinations,
       "huntSelectionAlgorithm": huntSelectionAlgorithm,
       "huntTimeout": huntTimeout,
       "huntCauses": huntCauses,
       "huntConfigStatus": huntConfigStatus,
       "huntUp": huntUp,
       "huntDown": huntDown,
       "huntInsert": huntInsert,
       "huntDelete": huntDelete,
       "signalingPropertiesTable": signalingPropertiesTable,
       "signalingPropertiesEntry": signalingPropertiesEntry,
       "signalingPropertiesIndex": signalingPropertiesIndex,
       "signalingPropertiesName": signalingPropertiesName,
       "signalingPropertiesEarlyConnect": signalingPropertiesEarlyConnect,
       "signalingPropertiesEarlyDisconnect": signalingPropertiesEarlyDisconnect,
       "signalingPropertiesDestinationHost": signalingPropertiesDestinationHost,
       "signalingPropertiesAllow180Sdp": signalingPropertiesAllow180Sdp,
       "signalingPropertiesAllow183NoSdp": signalingPropertiesAllow183NoSdp,
       "signalingPropertiesPrivacy": signalingPropertiesPrivacy,
       "signalingPropertiesCallPropertiesTranslation": signalingPropertiesCallPropertiesTranslation,
       "signalingPropertiesSipHeadersTranslation": signalingPropertiesSipHeadersTranslation,
       "signalingPropertiesConfigStatus": signalingPropertiesConfigStatus,
       "signalingPropertiesUp": signalingPropertiesUp,
       "signalingPropertiesDown": signalingPropertiesDown,
       "signalingPropertiesInsert": signalingPropertiesInsert,
       "signalingPropertiesDelete": signalingPropertiesDelete,
       "sipHeadersTranslationTable": sipHeadersTranslationTable,
       "sipHeadersTranslationEntry": sipHeadersTranslationEntry,
       "sipHeadersTranslationIndex": sipHeadersTranslationIndex,
       "sipHeadersTranslationName": sipHeadersTranslationName,
       "sipHeadersTranslationSipHeader": sipHeadersTranslationSipHeader,
       "sipHeadersTranslationBuiltFrom": sipHeadersTranslationBuiltFrom,
       "sipHeadersTranslationFixValue": sipHeadersTranslationFixValue,
       "sipHeadersTranslationConfigStatus": sipHeadersTranslationConfigStatus,
       "sipHeadersTranslationUp": sipHeadersTranslationUp,
       "sipHeadersTranslationDown": sipHeadersTranslationDown,
       "sipHeadersTranslationInsert": sipHeadersTranslationInsert,
       "sipHeadersTranslationDelete": sipHeadersTranslationDelete,
       "callPropertiesTranslationTable": callPropertiesTranslationTable,
       "callPropertiesTranslationEntry": callPropertiesTranslationEntry,
       "callPropertiesTranslationIndex": callPropertiesTranslationIndex,
       "callPropertiesTranslationName": callPropertiesTranslationName,
       "callPropertiesTranslationCallProperty": callPropertiesTranslationCallProperty,
       "callPropertiesTranslationBuiltFrom": callPropertiesTranslationBuiltFrom,
       "callPropertiesTranslationFixValue": callPropertiesTranslationFixValue,
       "callPropertiesTranslationConfigStatus": callPropertiesTranslationConfigStatus,
       "callPropertiesTranslationUp": callPropertiesTranslationUp,
       "callPropertiesTranslationDown": callPropertiesTranslationDown,
       "callPropertiesTranslationInsert": callPropertiesTranslationInsert,
       "callPropertiesTranslationDelete": callPropertiesTranslationDelete,
       "autoRoutingTable": autoRoutingTable,
       "autoRoutingEntry": autoRoutingEntry,
       "autoRoutingEpId": autoRoutingEpId,
       "autoRoutingAutoroutable": autoRoutingAutoroutable,
       "autoRoutingAutoRoutingGateway": autoRoutingAutoRoutingGateway,
       "autoRoutingAutoRoutingDestination": autoRoutingAutoRoutingDestination,
       "autoRoutingE164": autoRoutingE164,
       "autoRoutingSipUsername": autoRoutingSipUsername,
       "autoRoutingName": autoRoutingName,
       "autoRoutingCriteriaType": autoRoutingCriteriaType,
       "autoRoutingIncomingMappings": autoRoutingIncomingMappings,
       "autoRoutingOutgoingMappings": autoRoutingOutgoingMappings,
       "autoRoutingIncomingSignalingProperties": autoRoutingIncomingSignalingProperties,
       "autoRoutingOutgoingSignalingProperties": autoRoutingOutgoingSignalingProperties,
       "sipRedirectTable": sipRedirectTable,
       "sipRedirectEntry": sipRedirectEntry,
       "sipRedirectIndex": sipRedirectIndex,
       "sipRedirectName": sipRedirectName,
       "sipRedirectDestinationHost": sipRedirectDestinationHost,
       "sipRedirectConfigStatus": sipRedirectConfigStatus,
       "sipRedirectUp": sipRedirectUp,
       "sipRedirectDown": sipRedirectDown,
       "sipRedirectInsert": sipRedirectInsert,
       "sipRedirectDelete": sipRedirectDelete,
       "callSimulationGroup": callSimulationGroup,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
