# SNMP MIB module (SONICWALL-SMA-APPLIANCE-SECURITY-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonicwall/SONICWALL-SMA-APPLIANCE-SECURITY-HISTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:33 2025
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

(InternationalDisplayString,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString")

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

(sonicwallSMAAppliance,) = mibBuilder.importSymbols(
    "SONICWALL-SMA-MIB",
    "sonicwallSMAAppliance")


# MODULE-IDENTITY

sonicwallSecurityHistory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NumOfLoginDenials_Type = Integer32
_NumOfLoginDenials_Object = MibScalar
numOfLoginDenials = _NumOfLoginDenials_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4, 1),
    _NumOfLoginDenials_Type()
)
numOfLoginDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfLoginDenials.setStatus("current")
_LastLoginDenial_ObjectIdentity = ObjectIdentity
lastLoginDenial = _LastLoginDenial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4, 2)
)
_LastLoginDeniedUser_Type = InternationalDisplayString
_LastLoginDeniedUser_Object = MibScalar
lastLoginDeniedUser = _LastLoginDeniedUser_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4, 2, 1),
    _LastLoginDeniedUser_Type()
)
lastLoginDeniedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastLoginDeniedUser.setStatus("current")
_LastLoginDeniedTime_Type = InternationalDisplayString
_LastLoginDeniedTime_Object = MibScalar
lastLoginDeniedTime = _LastLoginDeniedTime_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4, 2, 2),
    _LastLoginDeniedTime_Type()
)
lastLoginDeniedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastLoginDeniedTime.setStatus("current")
_NumOfAccessDenials_Type = Integer32
_NumOfAccessDenials_Object = MibScalar
numOfAccessDenials = _NumOfAccessDenials_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4, 3),
    _NumOfAccessDenials_Type()
)
numOfAccessDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfAccessDenials.setStatus("current")
_LastAccessDenial_ObjectIdentity = ObjectIdentity
lastAccessDenial = _LastAccessDenial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4, 4)
)
_LastAccessDeniedUser_Type = InternationalDisplayString
_LastAccessDeniedUser_Object = MibScalar
lastAccessDeniedUser = _LastAccessDeniedUser_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4, 4, 1),
    _LastAccessDeniedUser_Type()
)
lastAccessDeniedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastAccessDeniedUser.setStatus("current")
_LastAccessDeniedResource_Type = InternationalDisplayString
_LastAccessDeniedResource_Object = MibScalar
lastAccessDeniedResource = _LastAccessDeniedResource_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4, 4, 2),
    _LastAccessDeniedResource_Type()
)
lastAccessDeniedResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastAccessDeniedResource.setStatus("current")
_LastAccessDeniedTime_Type = InternationalDisplayString
_LastAccessDeniedTime_Object = MibScalar
lastAccessDeniedTime = _LastAccessDeniedTime_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 4, 4, 3),
    _LastAccessDeniedTime_Type()
)
lastAccessDeniedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastAccessDeniedTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-SMA-APPLIANCE-SECURITY-HISTORY-MIB",
    **{"sonicwallSecurityHistory": sonicwallSecurityHistory,
       "numOfLoginDenials": numOfLoginDenials,
       "lastLoginDenial": lastLoginDenial,
       "lastLoginDeniedUser": lastLoginDeniedUser,
       "lastLoginDeniedTime": lastLoginDeniedTime,
       "numOfAccessDenials": numOfAccessDenials,
       "lastAccessDenial": lastAccessDenial,
       "lastAccessDeniedUser": lastAccessDeniedUser,
       "lastAccessDeniedResource": lastAccessDeniedResource,
       "lastAccessDeniedTime": lastAccessDeniedTime}
)
