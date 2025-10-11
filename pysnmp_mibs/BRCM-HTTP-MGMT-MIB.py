# SNMP MIB module (BRCM-HTTP-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-HTTP-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:25 2025
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

(cableDataMgmtBase,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "cableDataMgmtBase")

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

httpMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    httpMgmt.setRevisions(
        ("2007-02-05 00:00",
         "2004-02-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _HttpAdminId_Type(DisplayString):
    """Custom type httpAdminId based on DisplayString"""
    defaultValue = OctetString("")


_HttpAdminId_Type.__name__ = "DisplayString"
_HttpAdminId_Object = MibScalar
httpAdminId = _HttpAdminId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 3, 1),
    _HttpAdminId_Type()
)
httpAdminId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpAdminId.setStatus("current")


class _HttpAdminPassword_Type(DisplayString):
    """Custom type httpAdminPassword based on DisplayString"""
    defaultValue = OctetString("")


_HttpAdminPassword_Type.__name__ = "DisplayString"
_HttpAdminPassword_Object = MibScalar
httpAdminPassword = _HttpAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 3, 2),
    _HttpAdminPassword_Type()
)
httpAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpAdminPassword.setStatus("current")


class _HttpUserId_Type(DisplayString):
    """Custom type httpUserId based on DisplayString"""
    defaultValue = OctetString("")


_HttpUserId_Type.__name__ = "DisplayString"
_HttpUserId_Object = MibScalar
httpUserId = _HttpUserId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 3, 3),
    _HttpUserId_Type()
)
httpUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserId.setStatus("current")


class _HttpUserPassword_Type(DisplayString):
    """Custom type httpUserPassword based on DisplayString"""
    defaultValue = OctetString("")


_HttpUserPassword_Type.__name__ = "DisplayString"
_HttpUserPassword_Object = MibScalar
httpUserPassword = _HttpUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 3, 4),
    _HttpUserPassword_Type()
)
httpUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpUserPassword.setStatus("current")


class _HttpIpStackInterfaces_Type(Bits):
    """Custom type httpIpStackInterfaces based on Bits"""
    namedValues = NamedValues(
        *(("interface1", 0),
          ("interface2", 1),
          ("interface3", 2),
          ("interface4", 3),
          ("interface5", 4),
          ("interface6", 5),
          ("interface7", 6),
          ("interface8", 7))
    )

_HttpIpStackInterfaces_Type.__name__ = "Bits"
_HttpIpStackInterfaces_Object = MibScalar
httpIpStackInterfaces = _HttpIpStackInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 3, 5),
    _HttpIpStackInterfaces_Type()
)
httpIpStackInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpIpStackInterfaces.setStatus("current")


class _HttpAdvancedAccessEnabled_Type(Bits):
    """Custom type httpAdvancedAccessEnabled based on Bits"""
    namedValues = NamedValues(
        *(("interface1", 0),
          ("interface2", 1),
          ("interface3", 2),
          ("interface4", 3),
          ("interface5", 4),
          ("interface6", 5),
          ("interface7", 6),
          ("interface8", 7))
    )

_HttpAdvancedAccessEnabled_Type.__name__ = "Bits"
_HttpAdvancedAccessEnabled_Object = MibScalar
httpAdvancedAccessEnabled = _HttpAdvancedAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 3, 6),
    _HttpAdvancedAccessEnabled_Type()
)
httpAdvancedAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpAdvancedAccessEnabled.setStatus("current")


class _HttpPasswordOfTheDaySeed_Type(DisplayString):
    """Custom type httpPasswordOfTheDaySeed based on DisplayString"""
    defaultValue = OctetString("")


_HttpPasswordOfTheDaySeed_Type.__name__ = "DisplayString"
_HttpPasswordOfTheDaySeed_Object = MibScalar
httpPasswordOfTheDaySeed = _HttpPasswordOfTheDaySeed_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 3, 7),
    _HttpPasswordOfTheDaySeed_Type()
)
httpPasswordOfTheDaySeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPasswordOfTheDaySeed.setStatus("current")


class _HttpLoginTimeout_Type(Unsigned32):
    """Custom type httpLoginTimeout based on Unsigned32"""
    defaultValue = 0


_HttpLoginTimeout_Type.__name__ = "Unsigned32"
_HttpLoginTimeout_Object = MibScalar
httpLoginTimeout = _HttpLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 3, 8),
    _HttpLoginTimeout_Type()
)
httpLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpLoginTimeout.setStatus("current")
if mibBuilder.loadTexts:
    httpLoginTimeout.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-HTTP-MGMT-MIB",
    **{"httpMgmt": httpMgmt,
       "httpAdminId": httpAdminId,
       "httpAdminPassword": httpAdminPassword,
       "httpUserId": httpUserId,
       "httpUserPassword": httpUserPassword,
       "httpIpStackInterfaces": httpIpStackInterfaces,
       "httpAdvancedAccessEnabled": httpAdvancedAccessEnabled,
       "httpPasswordOfTheDaySeed": httpPasswordOfTheDaySeed,
       "httpLoginTimeout": httpLoginTimeout}
)
