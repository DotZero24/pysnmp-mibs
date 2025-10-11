# SNMP MIB module (NEWTEC-MODULATORPOWERPROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-MODULATORPOWERPROXY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:04 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcEnable,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcEnable")

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

ntcModulatorPowerProxy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400)
)
if mibBuilder.loadTexts:
    ntcModulatorPowerProxy.setRevisions(
        ("2013-05-22 06:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcModulatorPowerProxyObjects_ObjectIdentity = ObjectIdentity
ntcModulatorPowerProxyObjects = _NtcModulatorPowerProxyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1)
)
if mibBuilder.loadTexts:
    ntcModulatorPowerProxyObjects.setStatus("current")


class _NtcModPowerProxyEnable_Type(NtcEnable):
    """Custom type ntcModPowerProxyEnable based on NtcEnable"""
    defaultValue = 0


_NtcModPowerProxyEnable_Type.__name__ = "NtcEnable"
_NtcModPowerProxyEnable_Object = MibScalar
ntcModPowerProxyEnable = _NtcModPowerProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 1),
    _NtcModPowerProxyEnable_Type()
)
ntcModPowerProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcModPowerProxyEnable.setStatus("current")
_NtcModPowerProxyMonitoring_ObjectIdentity = ObjectIdentity
ntcModPowerProxyMonitoring = _NtcModPowerProxyMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 2)
)
if mibBuilder.loadTexts:
    ntcModPowerProxyMonitoring.setStatus("current")


class _NtcModPowerProxyRmtUpcState_Type(Integer32):
    """Custom type ntcModPowerProxyRmtUpcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcModPowerProxyRmtUpcState_Type.__name__ = "Integer32"
_NtcModPowerProxyRmtUpcState_Object = MibScalar
ntcModPowerProxyRmtUpcState = _NtcModPowerProxyRmtUpcState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 2, 1),
    _NtcModPowerProxyRmtUpcState_Type()
)
ntcModPowerProxyRmtUpcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcModPowerProxyRmtUpcState.setStatus("current")


class _NtcModPowerProxyCurModPower_Type(Integer32):
    """Custom type ntcModPowerProxyCurModPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-350, 100),
    )


_NtcModPowerProxyCurModPower_Type.__name__ = "Integer32"
_NtcModPowerProxyCurModPower_Object = MibScalar
ntcModPowerProxyCurModPower = _NtcModPowerProxyCurModPower_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 2, 2),
    _NtcModPowerProxyCurModPower_Type()
)
ntcModPowerProxyCurModPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcModPowerProxyCurModPower.setStatus("current")
if mibBuilder.loadTexts:
    ntcModPowerProxyCurModPower.setUnits("dBm")
_NtcModPowerProxyPowerReqCounter_Type = Counter64
_NtcModPowerProxyPowerReqCounter_Object = MibScalar
ntcModPowerProxyPowerReqCounter = _NtcModPowerProxyPowerReqCounter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 2, 3),
    _NtcModPowerProxyPowerReqCounter_Type()
)
ntcModPowerProxyPowerReqCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcModPowerProxyPowerReqCounter.setStatus("current")
_NtcModPwrProxyConformance_ObjectIdentity = ObjectIdentity
ntcModPwrProxyConformance = _NtcModPwrProxyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2)
)
if mibBuilder.loadTexts:
    ntcModPwrProxyConformance.setStatus("current")
_NtcModPwrProxyConfCompliance_ObjectIdentity = ObjectIdentity
ntcModPwrProxyConfCompliance = _NtcModPwrProxyConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2, 1)
)
if mibBuilder.loadTexts:
    ntcModPwrProxyConfCompliance.setStatus("current")
_NtcModPwrProxyConfGroup_ObjectIdentity = ObjectIdentity
ntcModPwrProxyConfGroup = _NtcModPwrProxyConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2, 2)
)
if mibBuilder.loadTexts:
    ntcModPwrProxyConfGroup.setStatus("current")

# Managed Objects groups

ntcModPwrProxyConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2, 2, 1)
)
ntcModPwrProxyConfGrpV1Standard.setObjects(
      *(("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPowerProxyEnable"),
        ("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPowerProxyRmtUpcState"),
        ("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPowerProxyCurModPower"),
        ("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPowerProxyPowerReqCounter"))
)
if mibBuilder.loadTexts:
    ntcModPwrProxyConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcModPwrProxyConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2, 1, 1)
)
ntcModPwrProxyConfCompV1Standard.setObjects(
    ("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPwrProxyConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcModPwrProxyConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-MODULATORPOWERPROXY-MIB",
    **{"ntcModulatorPowerProxy": ntcModulatorPowerProxy,
       "ntcModulatorPowerProxyObjects": ntcModulatorPowerProxyObjects,
       "ntcModPowerProxyEnable": ntcModPowerProxyEnable,
       "ntcModPowerProxyMonitoring": ntcModPowerProxyMonitoring,
       "ntcModPowerProxyRmtUpcState": ntcModPowerProxyRmtUpcState,
       "ntcModPowerProxyCurModPower": ntcModPowerProxyCurModPower,
       "ntcModPowerProxyPowerReqCounter": ntcModPowerProxyPowerReqCounter,
       "ntcModPwrProxyConformance": ntcModPwrProxyConformance,
       "ntcModPwrProxyConfCompliance": ntcModPwrProxyConfCompliance,
       "ntcModPwrProxyConfCompV1Standard": ntcModPwrProxyConfCompV1Standard,
       "ntcModPwrProxyConfGroup": ntcModPwrProxyConfGroup,
       "ntcModPwrProxyConfGrpV1Standard": ntcModPwrProxyConfGrpV1Standard}
)
