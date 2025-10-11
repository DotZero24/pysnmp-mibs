# SNMP MIB module (TPLINK-GARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-GARP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:10 2025
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

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkGarpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61)
)
if mibBuilder.loadTexts:
    tplinkGarpMIB.setRevisions(
        ("2014-11-24 14:42",)
    )


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkGarpMIBObjects_ObjectIdentity = ObjectIdentity
tplinkGarpMIBObjects = _TplinkGarpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1)
)
_TpGarpConfig_ObjectIdentity = ObjectIdentity
tpGarpConfig = _TpGarpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 1)
)


class _TpGarpDupIpEnable_Type(Integer32):
    """Custom type tpGarpDupIpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_TpGarpDupIpEnable_Type.__name__ = "Integer32"
_TpGarpDupIpEnable_Object = MibScalar
tpGarpDupIpEnable = _TpGarpDupIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 1, 1),
    _TpGarpDupIpEnable_Type()
)
tpGarpDupIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGarpDupIpEnable.setStatus("current")


class _TpGarpIntfUpEnable_Type(Integer32):
    """Custom type tpGarpIntfUpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_TpGarpIntfUpEnable_Type.__name__ = "Integer32"
_TpGarpIntfUpEnable_Object = MibScalar
tpGarpIntfUpEnable = _TpGarpIntfUpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 1, 2),
    _TpGarpIntfUpEnable_Type()
)
tpGarpIntfUpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGarpIntfUpEnable.setStatus("current")


class _TpGarpLearningEnable_Type(Integer32):
    """Custom type tpGarpLearningEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Disable", 0),
          ("Enable", 1))
    )


_TpGarpLearningEnable_Type.__name__ = "Integer32"
_TpGarpLearningEnable_Object = MibScalar
tpGarpLearningEnable = _TpGarpLearningEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 1, 3),
    _TpGarpLearningEnable_Type()
)
tpGarpLearningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGarpLearningEnable.setStatus("current")
_TpGarpIntfConfig_ObjectIdentity = ObjectIdentity
tpGarpIntfConfig = _TpGarpIntfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2)
)
_TpGarpIntfConfigTable_Object = MibTable
tpGarpIntfConfigTable = _TpGarpIntfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpGarpIntfConfigTable.setStatus("current")
_TpGarpIntfConfigEntry_Object = MibTableRow
tpGarpIntfConfigEntry = _TpGarpIntfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2, 1, 1)
)
tpGarpIntfConfigEntry.setIndexNames(
    (0, "TPLINK-GARP-MIB", "tpGarpInterface"),
)
if mibBuilder.loadTexts:
    tpGarpIntfConfigEntry.setStatus("current")


class _TpGarpInterface_Type(OctetString):
    """Custom type tpGarpInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TpGarpInterface_Type.__name__ = "OctetString"
_TpGarpInterface_Object = MibTableColumn
tpGarpInterface = _TpGarpInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2, 1, 1, 1),
    _TpGarpInterface_Type()
)
tpGarpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpGarpInterface.setStatus("current")


class _TpGarpSendInterval_Type(Integer32):
    """Custom type tpGarpSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpGarpSendInterval_Type.__name__ = "Integer32"
_TpGarpSendInterval_Object = MibTableColumn
tpGarpSendInterval = _TpGarpSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2, 1, 1, 2),
    _TpGarpSendInterval_Type()
)
tpGarpSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpGarpSendInterval.setStatus("current")
_TplinkGarpNotifications_ObjectIdentity = ObjectIdentity
tplinkGarpNotifications = _TplinkGarpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 2)
)

# Managed Objects groups


# Notification objects

tpGarpIpDuplicate = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 61, 2, 1)
)
tpGarpIpDuplicate.setObjects(
    ("TPLINK-GARP-MIB", "tpGarpInterface")
)
if mibBuilder.loadTexts:
    tpGarpIpDuplicate.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-GARP-MIB",
    **{"MacAddress": MacAddress,
       "tplinkGarpMIB": tplinkGarpMIB,
       "tplinkGarpMIBObjects": tplinkGarpMIBObjects,
       "tpGarpConfig": tpGarpConfig,
       "tpGarpDupIpEnable": tpGarpDupIpEnable,
       "tpGarpIntfUpEnable": tpGarpIntfUpEnable,
       "tpGarpLearningEnable": tpGarpLearningEnable,
       "tpGarpIntfConfig": tpGarpIntfConfig,
       "tpGarpIntfConfigTable": tpGarpIntfConfigTable,
       "tpGarpIntfConfigEntry": tpGarpIntfConfigEntry,
       "tpGarpInterface": tpGarpInterface,
       "tpGarpSendInterval": tpGarpSendInterval,
       "tplinkGarpNotifications": tplinkGarpNotifications,
       "tpGarpIpDuplicate": tpGarpIpDuplicate}
)
