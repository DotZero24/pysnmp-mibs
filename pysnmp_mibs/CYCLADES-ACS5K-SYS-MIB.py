# SNMP MIB module (CYCLADES-ACS5K-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/vertiv/CYCLADES-ACS5K-SYS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:50 2025
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

(cyACS5KMgmt,) = mibBuilder.importSymbols(
    "CYCLADES-ACS5K-MIB",
    "cyACS5KMgmt")

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

cyACS5KSys = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1)
)
if mibBuilder.loadTexts:
    cyACS5KSys.setRevisions(
        ("2011-05-24 00:00",
         "2010-07-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyACS5Kpname_Type = DisplayString
_CyACS5Kpname_Object = MibScalar
cyACS5Kpname = _CyACS5Kpname_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 1),
    _CyACS5Kpname_Type()
)
cyACS5Kpname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5Kpname.setStatus("current")
_CyACS5Kversion_Type = DisplayString
_CyACS5Kversion_Object = MibScalar
cyACS5Kversion = _CyACS5Kversion_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 2),
    _CyACS5Kversion_Type()
)
cyACS5Kversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5Kversion.setStatus("current")
_CyACS5KPower_ObjectIdentity = ObjectIdentity
cyACS5KPower = _CyACS5KPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 3)
)
if mibBuilder.loadTexts:
    cyACS5KPower.setStatus("current")
_CyACS5KPwNum_Type = Integer32
_CyACS5KPwNum_Object = MibScalar
cyACS5KPwNum = _CyACS5KPwNum_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 3, 1),
    _CyACS5KPwNum_Type()
)
cyACS5KPwNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5KPwNum.setStatus("current")


class _CyACS5KPw1_Type(Integer32):
    """Custom type cyACS5KPw1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noinstalled", 0),
          ("powerON", 1),
          ("powerOFF", 2))
    )


_CyACS5KPw1_Type.__name__ = "Integer32"
_CyACS5KPw1_Object = MibScalar
cyACS5KPw1 = _CyACS5KPw1_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 3, 2),
    _CyACS5KPw1_Type()
)
cyACS5KPw1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5KPw1.setStatus("current")


class _CyACS5KPw2_Type(Integer32):
    """Custom type cyACS5KPw2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noinstalled", 0),
          ("powerON", 1),
          ("powerOFF", 2))
    )


_CyACS5KPw2_Type.__name__ = "Integer32"
_CyACS5KPw2_Object = MibScalar
cyACS5KPw2 = _CyACS5KPw2_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 3, 3),
    _CyACS5KPw2_Type()
)
cyACS5KPw2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5KPw2.setStatus("current")
_CyACS5KPcmcia_ObjectIdentity = ObjectIdentity
cyACS5KPcmcia = _CyACS5KPcmcia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 4)
)
if mibBuilder.loadTexts:
    cyACS5KPcmcia.setStatus("current")
_CyACS5KNPcmcia_Type = Integer32
_CyACS5KNPcmcia_Object = MibScalar
cyACS5KNPcmcia = _CyACS5KNPcmcia_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 4, 1),
    _CyACS5KNPcmcia_Type()
)
cyACS5KNPcmcia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5KNPcmcia.setStatus("current")
_CyACS5KFlashSize_Type = Integer32
_CyACS5KFlashSize_Object = MibScalar
cyACS5KFlashSize = _CyACS5KFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 5),
    _CyACS5KFlashSize_Type()
)
cyACS5KFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5KFlashSize.setStatus("current")
_CyACS5KRAMSize_Type = Integer32
_CyACS5KRAMSize_Object = MibScalar
cyACS5KRAMSize = _CyACS5KRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 6),
    _CyACS5KRAMSize_Type()
)
cyACS5KRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5KRAMSize.setStatus("current")
_CyACS5KCPUfreq_Type = Integer32
_CyACS5KCPUfreq_Object = MibScalar
cyACS5KCPUfreq = _CyACS5KCPUfreq_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 7),
    _CyACS5KCPUfreq_Type()
)
cyACS5KCPUfreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5KCPUfreq.setStatus("current")
_CyACS5KDevId_Type = DisplayString
_CyACS5KDevId_Object = MibScalar
cyACS5KDevId = _CyACS5KDevId_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 8),
    _CyACS5KDevId_Type()
)
cyACS5KDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5KDevId.setStatus("current")
_CyACS5KSerialN_Type = DisplayString
_CyACS5KSerialN_Object = MibScalar
cyACS5KSerialN = _CyACS5KSerialN_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 1, 9),
    _CyACS5KSerialN_Type()
)
cyACS5KSerialN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACS5KSerialN.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYCLADES-ACS5K-SYS-MIB",
    **{"cyACS5KSys": cyACS5KSys,
       "cyACS5Kpname": cyACS5Kpname,
       "cyACS5Kversion": cyACS5Kversion,
       "cyACS5KPower": cyACS5KPower,
       "cyACS5KPwNum": cyACS5KPwNum,
       "cyACS5KPw1": cyACS5KPw1,
       "cyACS5KPw2": cyACS5KPw2,
       "cyACS5KPcmcia": cyACS5KPcmcia,
       "cyACS5KNPcmcia": cyACS5KNPcmcia,
       "cyACS5KFlashSize": cyACS5KFlashSize,
       "cyACS5KRAMSize": cyACS5KRAMSize,
       "cyACS5KCPUfreq": cyACS5KCPUfreq,
       "cyACS5KDevId": cyACS5KDevId,
       "cyACS5KSerialN": cyACS5KSerialN}
)
