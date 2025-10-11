# SNMP MIB module (H3C-OFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-OFP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:10 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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


# MODULE-IDENTITY

h3cOfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167)
)
if mibBuilder.loadTexts:
    h3cOfp.setRevisions(
        ("2017-02-28 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cOfpInstanceObjects_ObjectIdentity = ObjectIdentity
h3cOfpInstanceObjects = _H3cOfpInstanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1)
)
_H3cOfpInstanceControllerTable_Object = MibTable
h3cOfpInstanceControllerTable = _H3cOfpInstanceControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1)
)
if mibBuilder.loadTexts:
    h3cOfpInstanceControllerTable.setStatus("current")
_H3cOfpInstanceControllerEntry_Object = MibTableRow
h3cOfpInstanceControllerEntry = _H3cOfpInstanceControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1)
)
h3cOfpInstanceControllerEntry.setIndexNames(
    (0, "H3C-OFP-MIB", "h3cOfpInstanceID"),
    (0, "H3C-OFP-MIB", "h3cOfpInstanceControllerID"),
)
if mibBuilder.loadTexts:
    h3cOfpInstanceControllerEntry.setStatus("current")


class _H3cOfpInstanceID_Type(Integer32):
    """Custom type h3cOfpInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cOfpInstanceID_Type.__name__ = "Integer32"
_H3cOfpInstanceID_Object = MibTableColumn
h3cOfpInstanceID = _H3cOfpInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 1),
    _H3cOfpInstanceID_Type()
)
h3cOfpInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cOfpInstanceID.setStatus("current")


class _H3cOfpInstanceControllerID_Type(Integer32):
    """Custom type h3cOfpInstanceControllerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cOfpInstanceControllerID_Type.__name__ = "Integer32"
_H3cOfpInstanceControllerID_Object = MibTableColumn
h3cOfpInstanceControllerID = _H3cOfpInstanceControllerID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 2),
    _H3cOfpInstanceControllerID_Type()
)
h3cOfpInstanceControllerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cOfpInstanceControllerID.setStatus("current")


class _H3cOfpInstanceControllerRole_Type(Integer32):
    """Custom type h3cOfpInstanceControllerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("master", 2),
          ("slave", 3))
    )


_H3cOfpInstanceControllerRole_Type.__name__ = "Integer32"
_H3cOfpInstanceControllerRole_Object = MibTableColumn
h3cOfpInstanceControllerRole = _H3cOfpInstanceControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 3),
    _H3cOfpInstanceControllerRole_Type()
)
h3cOfpInstanceControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cOfpInstanceControllerRole.setStatus("current")


class _H3cOfpInstanceCtrConnectType_Type(Integer32):
    """Custom type h3cOfpInstanceCtrConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("ssl", 2))
    )


_H3cOfpInstanceCtrConnectType_Type.__name__ = "Integer32"
_H3cOfpInstanceCtrConnectType_Object = MibTableColumn
h3cOfpInstanceCtrConnectType = _H3cOfpInstanceCtrConnectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 4),
    _H3cOfpInstanceCtrConnectType_Type()
)
h3cOfpInstanceCtrConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cOfpInstanceCtrConnectType.setStatus("current")


class _H3cOfpInstanceCtrConnectState_Type(Integer32):
    """Custom type h3cOfpInstanceCtrConnectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("established", 1))
    )


_H3cOfpInstanceCtrConnectState_Type.__name__ = "Integer32"
_H3cOfpInstanceCtrConnectState_Object = MibTableColumn
h3cOfpInstanceCtrConnectState = _H3cOfpInstanceCtrConnectState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 5),
    _H3cOfpInstanceCtrConnectState_Type()
)
h3cOfpInstanceCtrConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cOfpInstanceCtrConnectState.setStatus("current")


class _H3cOfpInstanceCtrSSLPolicy_Type(OctetString):
    """Custom type h3cOfpInstanceCtrSSLPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cOfpInstanceCtrSSLPolicy_Type.__name__ = "OctetString"
_H3cOfpInstanceCtrSSLPolicy_Object = MibTableColumn
h3cOfpInstanceCtrSSLPolicy = _H3cOfpInstanceCtrSSLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 6),
    _H3cOfpInstanceCtrSSLPolicy_Type()
)
h3cOfpInstanceCtrSSLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cOfpInstanceCtrSSLPolicy.setStatus("current")


class _H3cOfpInstanceCtrVRFName_Type(OctetString):
    """Custom type h3cOfpInstanceCtrVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cOfpInstanceCtrVRFName_Type.__name__ = "OctetString"
_H3cOfpInstanceCtrVRFName_Object = MibTableColumn
h3cOfpInstanceCtrVRFName = _H3cOfpInstanceCtrVRFName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 7),
    _H3cOfpInstanceCtrVRFName_Type()
)
h3cOfpInstanceCtrVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cOfpInstanceCtrVRFName.setStatus("current")
_H3cOfpInstanceCtrIPType_Type = InetAddressType
_H3cOfpInstanceCtrIPType_Object = MibTableColumn
h3cOfpInstanceCtrIPType = _H3cOfpInstanceCtrIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 8),
    _H3cOfpInstanceCtrIPType_Type()
)
h3cOfpInstanceCtrIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cOfpInstanceCtrIPType.setStatus("current")
_H3cOfpInstanceCtrIPaddress_Type = InetAddress
_H3cOfpInstanceCtrIPaddress_Object = MibTableColumn
h3cOfpInstanceCtrIPaddress = _H3cOfpInstanceCtrIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 9),
    _H3cOfpInstanceCtrIPaddress_Type()
)
h3cOfpInstanceCtrIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cOfpInstanceCtrIPaddress.setStatus("current")


class _H3cOfpInstanceCtrPort_Type(Integer32):
    """Custom type h3cOfpInstanceCtrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cOfpInstanceCtrPort_Type.__name__ = "Integer32"
_H3cOfpInstanceCtrPort_Object = MibTableColumn
h3cOfpInstanceCtrPort = _H3cOfpInstanceCtrPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 167, 1, 1, 1, 10),
    _H3cOfpInstanceCtrPort_Type()
)
h3cOfpInstanceCtrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cOfpInstanceCtrPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-OFP-MIB",
    **{"h3cOfp": h3cOfp,
       "h3cOfpInstanceObjects": h3cOfpInstanceObjects,
       "h3cOfpInstanceControllerTable": h3cOfpInstanceControllerTable,
       "h3cOfpInstanceControllerEntry": h3cOfpInstanceControllerEntry,
       "h3cOfpInstanceID": h3cOfpInstanceID,
       "h3cOfpInstanceControllerID": h3cOfpInstanceControllerID,
       "h3cOfpInstanceControllerRole": h3cOfpInstanceControllerRole,
       "h3cOfpInstanceCtrConnectType": h3cOfpInstanceCtrConnectType,
       "h3cOfpInstanceCtrConnectState": h3cOfpInstanceCtrConnectState,
       "h3cOfpInstanceCtrSSLPolicy": h3cOfpInstanceCtrSSLPolicy,
       "h3cOfpInstanceCtrVRFName": h3cOfpInstanceCtrVRFName,
       "h3cOfpInstanceCtrIPType": h3cOfpInstanceCtrIPType,
       "h3cOfpInstanceCtrIPaddress": h3cOfpInstanceCtrIPaddress,
       "h3cOfpInstanceCtrPort": h3cOfpInstanceCtrPort}
)
