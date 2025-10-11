# SNMP MIB module (BRCM-RG-FACTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-RG-FACTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:50 2025
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

(cableDataFactory,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-FACTORY-MIB",
    "cableDataFactory")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

residentialGatewayFactory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    residentialGatewayFactory.setRevisions(
        ("2007-02-05 00:00",
         "2003-01-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RgFactoryBase_ObjectIdentity = ObjectIdentity
rgFactoryBase = _RgFactoryBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1)
)


class _RgInitialMode_Type(Integer32):
    """Custom type rgInitialMode based on Integer32"""
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
        *(("disabled", 1),
          ("residentialGateway", 2),
          ("cableHome10", 3),
          ("cableHome11", 4))
    )


_RgInitialMode_Type.__name__ = "Integer32"
_RgInitialMode_Object = MibScalar
rgInitialMode = _RgInitialMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 1),
    _RgInitialMode_Type()
)
rgInitialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgInitialMode.setStatus("current")
_RgRipAuthEnabled_Type = TruthValue
_RgRipAuthEnabled_Object = MibScalar
rgRipAuthEnabled = _RgRipAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 2),
    _RgRipAuthEnabled_Type()
)
rgRipAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgRipAuthEnabled.setStatus("current")


class _RgRipAuthKeyValue_Type(DisplayString):
    """Custom type rgRipAuthKeyValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RgRipAuthKeyValue_Type.__name__ = "DisplayString"
_RgRipAuthKeyValue_Object = MibScalar
rgRipAuthKeyValue = _RgRipAuthKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 3),
    _RgRipAuthKeyValue_Type()
)
rgRipAuthKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgRipAuthKeyValue.setStatus("current")


class _RgRipAuthKeyId_Type(Integer32):
    """Custom type rgRipAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RgRipAuthKeyId_Type.__name__ = "Integer32"
_RgRipAuthKeyId_Object = MibScalar
rgRipAuthKeyId = _RgRipAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 4),
    _RgRipAuthKeyId_Type()
)
rgRipAuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgRipAuthKeyId.setStatus("current")


class _RgRipReportingInterval_Type(Integer32):
    """Custom type rgRipReportingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16535),
    )


_RgRipReportingInterval_Type.__name__ = "Integer32"
_RgRipReportingInterval_Object = MibScalar
rgRipReportingInterval = _RgRipReportingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 5),
    _RgRipReportingInterval_Type()
)
rgRipReportingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgRipReportingInterval.setStatus("current")
if mibBuilder.loadTexts:
    rgRipReportingInterval.setUnits("seconds")
_RgRipUnicastDestIpAddress_Type = IpAddress
_RgRipUnicastDestIpAddress_Object = MibScalar
rgRipUnicastDestIpAddress = _RgRipUnicastDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 6),
    _RgRipUnicastDestIpAddress_Type()
)
rgRipUnicastDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgRipUnicastDestIpAddress.setStatus("current")
_RgRipSubnetMask_Type = IpAddress
_RgRipSubnetMask_Object = MibScalar
rgRipSubnetMask = _RgRipSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 7, 1, 7),
    _RgRipSubnetMask_Type()
)
rgRipSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgRipSubnetMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-RG-FACTORY-MIB",
    **{"residentialGatewayFactory": residentialGatewayFactory,
       "rgFactoryBase": rgFactoryBase,
       "rgInitialMode": rgInitialMode,
       "rgRipAuthEnabled": rgRipAuthEnabled,
       "rgRipAuthKeyValue": rgRipAuthKeyValue,
       "rgRipAuthKeyId": rgRipAuthKeyId,
       "rgRipReportingInterval": rgRipReportingInterval,
       "rgRipUnicastDestIpAddress": rgRipUnicastDestIpAddress,
       "rgRipSubnetMask": rgRipSubnetMask}
)
