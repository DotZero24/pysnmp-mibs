# SNMP MIB module (TPLINK-HTTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-HTTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:20 2025
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkHttp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51)
)
if mibBuilder.loadTexts:
    tplinkHttp.setRevisions(
        ("2015-01-21 10:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkHttpMIBObjects_ObjectIdentity = ObjectIdentity
tplinkHttpMIBObjects = _TplinkHttpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1)
)


class _HttpEnable_Type(Integer32):
    """Custom type httpEnable based on Integer32"""
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


_HttpEnable_Type.__name__ = "Integer32"
_HttpEnable_Object = MibScalar
httpEnable = _HttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 1),
    _HttpEnable_Type()
)
httpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpEnable.setStatus("current")


class _HttpSessionTimeOut_Type(Integer32):
    """Custom type httpSessionTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_HttpSessionTimeOut_Type.__name__ = "Integer32"
_HttpSessionTimeOut_Object = MibScalar
httpSessionTimeOut = _HttpSessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 2),
    _HttpSessionTimeOut_Type()
)
httpSessionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpSessionTimeOut.setStatus("current")


class _HttpUserLimitEnable_Type(Integer32):
    """Custom type httpUserLimitEnable based on Integer32"""
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


_HttpUserLimitEnable_Type.__name__ = "Integer32"
_HttpUserLimitEnable_Object = MibScalar
httpUserLimitEnable = _HttpUserLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 3),
    _HttpUserLimitEnable_Type()
)
httpUserLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserLimitEnable.setStatus("current")
_HttpUserLimitMaxAdminNum_Type = Integer32
_HttpUserLimitMaxAdminNum_Object = MibScalar
httpUserLimitMaxAdminNum = _HttpUserLimitMaxAdminNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 4),
    _HttpUserLimitMaxAdminNum_Type()
)
httpUserLimitMaxAdminNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserLimitMaxAdminNum.setStatus("current")
_HttpUserLimitMaxOperatorNum_Type = Integer32
_HttpUserLimitMaxOperatorNum_Object = MibScalar
httpUserLimitMaxOperatorNum = _HttpUserLimitMaxOperatorNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 5),
    _HttpUserLimitMaxOperatorNum_Type()
)
httpUserLimitMaxOperatorNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserLimitMaxOperatorNum.setStatus("current")
_HttpUserLimitMaxPowerUserNum_Type = Integer32
_HttpUserLimitMaxPowerUserNum_Object = MibScalar
httpUserLimitMaxPowerUserNum = _HttpUserLimitMaxPowerUserNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 6),
    _HttpUserLimitMaxPowerUserNum_Type()
)
httpUserLimitMaxPowerUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserLimitMaxPowerUserNum.setStatus("current")
_HttpUserLimitMaxUserNum_Type = Integer32
_HttpUserLimitMaxUserNum_Object = MibScalar
httpUserLimitMaxUserNum = _HttpUserLimitMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 7),
    _HttpUserLimitMaxUserNum_Type()
)
httpUserLimitMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserLimitMaxUserNum.setStatus("current")


class _HttpPort_Type(Integer32):
    """Custom type httpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpPort_Type.__name__ = "Integer32"
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 1, 8),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")
_TplinkHttpMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkHttpMIBNotifications = _TplinkHttpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 51, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-HTTP-MIB",
    **{"tplinkHttp": tplinkHttp,
       "tplinkHttpMIBObjects": tplinkHttpMIBObjects,
       "httpEnable": httpEnable,
       "httpSessionTimeOut": httpSessionTimeOut,
       "httpUserLimitEnable": httpUserLimitEnable,
       "httpUserLimitMaxAdminNum": httpUserLimitMaxAdminNum,
       "httpUserLimitMaxOperatorNum": httpUserLimitMaxOperatorNum,
       "httpUserLimitMaxPowerUserNum": httpUserLimitMaxPowerUserNum,
       "httpUserLimitMaxUserNum": httpUserLimitMaxUserNum,
       "httpPort": httpPort,
       "tplinkHttpMIBNotifications": tplinkHttpMIBNotifications}
)
