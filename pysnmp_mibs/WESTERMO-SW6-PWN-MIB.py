# SNMP MIB module (WESTERMO-SW6-PWN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-SW6-PWN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:31 2025
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

pwn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9)
)
if mibBuilder.loadTexts:
    pwn.setRevisions(
        ("2019-09-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1)
)
_CfgWireless_ObjectIdentity = ObjectIdentity
cfgWireless = _CfgWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1, 1)
)
_CfgWlanBandsteering_ObjectIdentity = ObjectIdentity
cfgWlanBandsteering = _CfgWlanBandsteering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1, 1, 1)
)


class _CfgWlanBsteerEnabled_Type(Integer32):
    """Custom type cfgWlanBsteerEnabled based on Integer32"""
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


_CfgWlanBsteerEnabled_Type.__name__ = "Integer32"
_CfgWlanBsteerEnabled_Object = MibScalar
cfgWlanBsteerEnabled = _CfgWlanBsteerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1, 1, 1, 1),
    _CfgWlanBsteerEnabled_Type()
)
cfgWlanBsteerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanBsteerEnabled.setStatus("current")


class _CfgWlanBsteerMatchingSsid_Type(DisplayString):
    """Custom type cfgWlanBsteerMatchingSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgWlanBsteerMatchingSsid_Type.__name__ = "DisplayString"
_CfgWlanBsteerMatchingSsid_Object = MibScalar
cfgWlanBsteerMatchingSsid = _CfgWlanBsteerMatchingSsid_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 1, 1, 1, 2),
    _CfgWlanBsteerMatchingSsid_Type()
)
cfgWlanBsteerMatchingSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgWlanBsteerMatchingSsid.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 1)
)
_GroupConfiguration_ObjectIdentity = ObjectIdentity
groupConfiguration = _GroupConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 1, 1)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 2)
)

# Managed Objects groups

groupCfgWlanBandsteering = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 1, 1, 1)
)
groupCfgWlanBandsteering.setObjects(
      *(("WESTERMO-SW6-PWN-MIB", "cfgWlanBsteerEnabled"),
        ("WESTERMO-SW6-PWN-MIB", "cfgWlanBsteerMatchingSsid"))
)
if mibBuilder.loadTexts:
    groupCfgWlanBandsteering.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 9, 10000, 2, 1)
)
compliance.setObjects(
    ("WESTERMO-SW6-PWN-MIB", "groupCfgWlanBandsteering")
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-SW6-PWN-MIB",
    **{"pwn": pwn,
       "configuration": configuration,
       "cfgWireless": cfgWireless,
       "cfgWlanBandsteering": cfgWlanBandsteering,
       "cfgWlanBsteerEnabled": cfgWlanBsteerEnabled,
       "cfgWlanBsteerMatchingSsid": cfgWlanBsteerMatchingSsid,
       "conformance": conformance,
       "groups": groups,
       "groupConfiguration": groupConfiguration,
       "groupCfgWlanBandsteering": groupCfgWlanBandsteering,
       "compliances": compliances,
       "compliance": compliance}
)
