# SNMP MIB module (MX-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:58 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

qosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20)
)
if mibBuilder.loadTexts:
    qosMIB.setRevisions(
        ("2010-11-02 00:00",
         "2009-03-06 00:00",
         "2005-09-26 00:00",
         "2005-02-21 00:00",
         "2004-06-17 00:00",
         "2001-08-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QosMIBObjects_ObjectIdentity = ObjectIdentity
qosMIBObjects = _QosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1)
)
_QosDiffServ_ObjectIdentity = ObjectIdentity
qosDiffServ = _QosDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 1)
)


class _QosSignalingDiffServ_Type(Unsigned32):
    """Custom type qosSignalingDiffServ based on Unsigned32"""
    defaultValue = 184

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QosSignalingDiffServ_Type.__name__ = "Unsigned32"
_QosSignalingDiffServ_Object = MibScalar
qosSignalingDiffServ = _QosSignalingDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 1, 1),
    _QosSignalingDiffServ_Type()
)
qosSignalingDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSignalingDiffServ.setStatus("current")


class _QosVoiceDiffServ_Type(Unsigned32):
    """Custom type qosVoiceDiffServ based on Unsigned32"""
    defaultValue = 184

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QosVoiceDiffServ_Type.__name__ = "Unsigned32"
_QosVoiceDiffServ_Object = MibScalar
qosVoiceDiffServ = _QosVoiceDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 1, 2),
    _QosVoiceDiffServ_Type()
)
qosVoiceDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVoiceDiffServ.setStatus("current")


class _QosT38FaxDiffServ_Type(Unsigned32):
    """Custom type qosT38FaxDiffServ based on Unsigned32"""
    defaultValue = 184

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QosT38FaxDiffServ_Type.__name__ = "Unsigned32"
_QosT38FaxDiffServ_Object = MibScalar
qosT38FaxDiffServ = _QosT38FaxDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 1, 3),
    _QosT38FaxDiffServ_Type()
)
qosT38FaxDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosT38FaxDiffServ.setStatus("current")


class _QosVbdDiffServ_Type(Unsigned32):
    """Custom type qosVbdDiffServ based on Unsigned32"""
    defaultValue = 184

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QosVbdDiffServ_Type.__name__ = "Unsigned32"
_QosVbdDiffServ_Object = MibScalar
qosVbdDiffServ = _QosVbdDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 1, 4),
    _QosVbdDiffServ_Type()
)
qosVbdDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVbdDiffServ.setStatus("current")
_QosIeee8021q_ObjectIdentity = ObjectIdentity
qosIeee8021q = _QosIeee8021q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2)
)


class _QosSignalingIeee8021qEnable_Type(Integer32):
    """Custom type qosSignalingIeee8021qEnable based on Integer32"""
    defaultValue = 0

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


_QosSignalingIeee8021qEnable_Type.__name__ = "Integer32"
_QosSignalingIeee8021qEnable_Object = MibScalar
qosSignalingIeee8021qEnable = _QosSignalingIeee8021qEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 1),
    _QosSignalingIeee8021qEnable_Type()
)
qosSignalingIeee8021qEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSignalingIeee8021qEnable.setStatus("current")


class _QosSignalingIeee8021qUserPriority_Type(Unsigned32):
    """Custom type qosSignalingIeee8021qUserPriority based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosSignalingIeee8021qUserPriority_Type.__name__ = "Unsigned32"
_QosSignalingIeee8021qUserPriority_Object = MibScalar
qosSignalingIeee8021qUserPriority = _QosSignalingIeee8021qUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 2),
    _QosSignalingIeee8021qUserPriority_Type()
)
qosSignalingIeee8021qUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSignalingIeee8021qUserPriority.setStatus("current")


class _QosVoiceIeee8021qEnable_Type(Integer32):
    """Custom type qosVoiceIeee8021qEnable based on Integer32"""
    defaultValue = 0

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


_QosVoiceIeee8021qEnable_Type.__name__ = "Integer32"
_QosVoiceIeee8021qEnable_Object = MibScalar
qosVoiceIeee8021qEnable = _QosVoiceIeee8021qEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 3),
    _QosVoiceIeee8021qEnable_Type()
)
qosVoiceIeee8021qEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVoiceIeee8021qEnable.setStatus("current")


class _QosVoiceIeee8021qUserPriority_Type(Unsigned32):
    """Custom type qosVoiceIeee8021qUserPriority based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosVoiceIeee8021qUserPriority_Type.__name__ = "Unsigned32"
_QosVoiceIeee8021qUserPriority_Object = MibScalar
qosVoiceIeee8021qUserPriority = _QosVoiceIeee8021qUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 4),
    _QosVoiceIeee8021qUserPriority_Type()
)
qosVoiceIeee8021qUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVoiceIeee8021qUserPriority.setStatus("current")


class _QosT38FaxIeee8021qEnable_Type(Integer32):
    """Custom type qosT38FaxIeee8021qEnable based on Integer32"""
    defaultValue = 0

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


_QosT38FaxIeee8021qEnable_Type.__name__ = "Integer32"
_QosT38FaxIeee8021qEnable_Object = MibScalar
qosT38FaxIeee8021qEnable = _QosT38FaxIeee8021qEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 5),
    _QosT38FaxIeee8021qEnable_Type()
)
qosT38FaxIeee8021qEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosT38FaxIeee8021qEnable.setStatus("current")


class _QosT38FaxIeee8021qUserPriority_Type(Unsigned32):
    """Custom type qosT38FaxIeee8021qUserPriority based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosT38FaxIeee8021qUserPriority_Type.__name__ = "Unsigned32"
_QosT38FaxIeee8021qUserPriority_Object = MibScalar
qosT38FaxIeee8021qUserPriority = _QosT38FaxIeee8021qUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 6),
    _QosT38FaxIeee8021qUserPriority_Type()
)
qosT38FaxIeee8021qUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosT38FaxIeee8021qUserPriority.setStatus("current")


class _QosVbdIeee8021qEnable_Type(Integer32):
    """Custom type qosVbdIeee8021qEnable based on Integer32"""
    defaultValue = 0

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


_QosVbdIeee8021qEnable_Type.__name__ = "Integer32"
_QosVbdIeee8021qEnable_Object = MibScalar
qosVbdIeee8021qEnable = _QosVbdIeee8021qEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 7),
    _QosVbdIeee8021qEnable_Type()
)
qosVbdIeee8021qEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVbdIeee8021qEnable.setStatus("current")


class _QosVbdIeee8021qUserPriority_Type(Unsigned32):
    """Custom type qosVbdIeee8021qUserPriority based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosVbdIeee8021qUserPriority_Type.__name__ = "Unsigned32"
_QosVbdIeee8021qUserPriority_Object = MibScalar
qosVbdIeee8021qUserPriority = _QosVbdIeee8021qUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 8),
    _QosVbdIeee8021qUserPriority_Type()
)
qosVbdIeee8021qUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVbdIeee8021qUserPriority.setStatus("current")
_QosVlanIeee8021q_ObjectIdentity = ObjectIdentity
qosVlanIeee8021q = _QosVlanIeee8021q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 15)
)


class _QosVlanIeee8021qTaggingEnable_Type(Integer32):
    """Custom type qosVlanIeee8021qTaggingEnable based on Integer32"""
    defaultValue = 0

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


_QosVlanIeee8021qTaggingEnable_Type.__name__ = "Integer32"
_QosVlanIeee8021qTaggingEnable_Object = MibScalar
qosVlanIeee8021qTaggingEnable = _QosVlanIeee8021qTaggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 15, 1),
    _QosVlanIeee8021qTaggingEnable_Type()
)
qosVlanIeee8021qTaggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanIeee8021qTaggingEnable.setStatus("current")


class _QosVlanIeee8021qVirtualLanID_Type(Unsigned32):
    """Custom type qosVlanIeee8021qVirtualLanID based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_QosVlanIeee8021qVirtualLanID_Type.__name__ = "Unsigned32"
_QosVlanIeee8021qVirtualLanID_Object = MibScalar
qosVlanIeee8021qVirtualLanID = _QosVlanIeee8021qVirtualLanID_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 15, 2),
    _QosVlanIeee8021qVirtualLanID_Type()
)
qosVlanIeee8021qVirtualLanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanIeee8021qVirtualLanID.setStatus("current")


class _QosVlanIeee8021qDefaultUserPriority_Type(Unsigned32):
    """Custom type qosVlanIeee8021qDefaultUserPriority based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosVlanIeee8021qDefaultUserPriority_Type.__name__ = "Unsigned32"
_QosVlanIeee8021qDefaultUserPriority_Object = MibScalar
qosVlanIeee8021qDefaultUserPriority = _QosVlanIeee8021qDefaultUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 2, 15, 3),
    _QosVlanIeee8021qDefaultUserPriority_Type()
)
qosVlanIeee8021qDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanIeee8021qDefaultUserPriority.setStatus("current")
_QosIeee8021qSubstitution_ObjectIdentity = ObjectIdentity
qosIeee8021qSubstitution = _QosIeee8021qSubstitution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 10)
)


class _QosVlanIeee8021qSubstitutionEnable_Type(MxEnableState):
    """Custom type qosVlanIeee8021qSubstitutionEnable based on MxEnableState"""
    defaultValue = 0


_QosVlanIeee8021qSubstitutionEnable_Type.__name__ = "MxEnableState"
_QosVlanIeee8021qSubstitutionEnable_Object = MibScalar
qosVlanIeee8021qSubstitutionEnable = _QosVlanIeee8021qSubstitutionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 10, 10),
    _QosVlanIeee8021qSubstitutionEnable_Type()
)
qosVlanIeee8021qSubstitutionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanIeee8021qSubstitutionEnable.setStatus("current")


class _QosVlanIeee8021qSubstitutionVlanID_Type(Unsigned32):
    """Custom type qosVlanIeee8021qSubstitutionVlanID based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_QosVlanIeee8021qSubstitutionVlanID_Type.__name__ = "Unsigned32"
_QosVlanIeee8021qSubstitutionVlanID_Object = MibScalar
qosVlanIeee8021qSubstitutionVlanID = _QosVlanIeee8021qSubstitutionVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 10, 20),
    _QosVlanIeee8021qSubstitutionVlanID_Type()
)
qosVlanIeee8021qSubstitutionVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanIeee8021qSubstitutionVlanID.setStatus("current")


class _QosVlanIeee8021qSubstitutionUserPriority_Type(Unsigned32):
    """Custom type qosVlanIeee8021qSubstitutionUserPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosVlanIeee8021qSubstitutionUserPriority_Type.__name__ = "Unsigned32"
_QosVlanIeee8021qSubstitutionUserPriority_Object = MibScalar
qosVlanIeee8021qSubstitutionUserPriority = _QosVlanIeee8021qSubstitutionUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 10, 30),
    _QosVlanIeee8021qSubstitutionUserPriority_Type()
)
qosVlanIeee8021qSubstitutionUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanIeee8021qSubstitutionUserPriority.setStatus("current")


class _QosVlanIeee8021qSubstitutionFiltering_Type(MxEnableState):
    """Custom type qosVlanIeee8021qSubstitutionFiltering based on MxEnableState"""
    defaultValue = 0


_QosVlanIeee8021qSubstitutionFiltering_Type.__name__ = "MxEnableState"
_QosVlanIeee8021qSubstitutionFiltering_Object = MibScalar
qosVlanIeee8021qSubstitutionFiltering = _QosVlanIeee8021qSubstitutionFiltering_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 10, 40),
    _QosVlanIeee8021qSubstitutionFiltering_Type()
)
qosVlanIeee8021qSubstitutionFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosVlanIeee8021qSubstitutionFiltering.setStatus("current")
_QosInterop_ObjectIdentity = ObjectIdentity
qosInterop = _QosInterop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 20)
)


class _QosInteropUseVoiceQoSForRtcpEnable_Type(MxEnableState):
    """Custom type qosInteropUseVoiceQoSForRtcpEnable based on MxEnableState"""
    defaultValue = 0


_QosInteropUseVoiceQoSForRtcpEnable_Type.__name__ = "MxEnableState"
_QosInteropUseVoiceQoSForRtcpEnable_Object = MibScalar
qosInteropUseVoiceQoSForRtcpEnable = _QosInteropUseVoiceQoSForRtcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 1, 20, 10),
    _QosInteropUseVoiceQoSForRtcpEnable_Type()
)
qosInteropUseVoiceQoSForRtcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosInteropUseVoiceQoSForRtcpEnable.setStatus("current")
_QosConformance_ObjectIdentity = ObjectIdentity
qosConformance = _QosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 2)
)
_QosCompliances_ObjectIdentity = ObjectIdentity
qosCompliances = _QosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 2, 1)
)
_QosGroups_ObjectIdentity = ObjectIdentity
qosGroups = _QosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 2, 2)
)

# Managed Objects groups

qosDiffServGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 2, 2, 1)
)
qosDiffServGroupVer1.setObjects(
      *(("MX-QOS-MIB", "qosSignalingDiffServ"),
        ("MX-QOS-MIB", "qosVoiceDiffServ"),
        ("MX-QOS-MIB", "qosT38FaxDiffServ"),
        ("MX-QOS-MIB", "qosVbdDiffServ"))
)
if mibBuilder.loadTexts:
    qosDiffServGroupVer1.setStatus("current")

qosIeee8021qGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 2, 2, 2)
)
qosIeee8021qGroupVer1.setObjects(
      *(("MX-QOS-MIB", "qosSignalingDiffServ"),
        ("MX-QOS-MIB", "qosVoiceDiffServ"),
        ("MX-QOS-MIB", "qosT38FaxDiffServ"),
        ("MX-QOS-MIB", "qosVbdDiffServ"))
)
if mibBuilder.loadTexts:
    qosIeee8021qGroupVer1.setStatus("current")

qosIeee8021qSubstitutionGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 2, 2, 10)
)
qosIeee8021qSubstitutionGroupVer1.setObjects(
      *(("MX-QOS-MIB", "qosVlanIeee8021qSubstitutionEnable"),
        ("MX-QOS-MIB", "qosVlanIeee8021qSubstitutionVlanID"),
        ("MX-QOS-MIB", "qosVlanIeee8021qSubstitutionUserPriority"),
        ("MX-QOS-MIB", "qosVlanIeee8021qSubstitutionFiltering"))
)
if mibBuilder.loadTexts:
    qosIeee8021qSubstitutionGroupVer1.setStatus("current")

qosInteropGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 2, 2, 20)
)
qosInteropGroupVer1.setObjects(
    ("MX-QOS-MIB", "qosInteropUseVoiceQoSForRtcpEnable")
)
if mibBuilder.loadTexts:
    qosInteropGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qosAnalogComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 20, 2, 1, 1)
)
qosAnalogComplVer1.setObjects(
      *(("MX-QOS-MIB", "qosDiffServGroupVer1"),
        ("MX-QOS-MIB", "qosIeee8021qGroupVer1"),
        ("MX-QOS-MIB", "qosIeee8021qSubstitutionGroupVer1"))
)
if mibBuilder.loadTexts:
    qosAnalogComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-QOS-MIB",
    **{"qosMIB": qosMIB,
       "qosMIBObjects": qosMIBObjects,
       "qosDiffServ": qosDiffServ,
       "qosSignalingDiffServ": qosSignalingDiffServ,
       "qosVoiceDiffServ": qosVoiceDiffServ,
       "qosT38FaxDiffServ": qosT38FaxDiffServ,
       "qosVbdDiffServ": qosVbdDiffServ,
       "qosIeee8021q": qosIeee8021q,
       "qosSignalingIeee8021qEnable": qosSignalingIeee8021qEnable,
       "qosSignalingIeee8021qUserPriority": qosSignalingIeee8021qUserPriority,
       "qosVoiceIeee8021qEnable": qosVoiceIeee8021qEnable,
       "qosVoiceIeee8021qUserPriority": qosVoiceIeee8021qUserPriority,
       "qosT38FaxIeee8021qEnable": qosT38FaxIeee8021qEnable,
       "qosT38FaxIeee8021qUserPriority": qosT38FaxIeee8021qUserPriority,
       "qosVbdIeee8021qEnable": qosVbdIeee8021qEnable,
       "qosVbdIeee8021qUserPriority": qosVbdIeee8021qUserPriority,
       "qosVlanIeee8021q": qosVlanIeee8021q,
       "qosVlanIeee8021qTaggingEnable": qosVlanIeee8021qTaggingEnable,
       "qosVlanIeee8021qVirtualLanID": qosVlanIeee8021qVirtualLanID,
       "qosVlanIeee8021qDefaultUserPriority": qosVlanIeee8021qDefaultUserPriority,
       "qosIeee8021qSubstitution": qosIeee8021qSubstitution,
       "qosVlanIeee8021qSubstitutionEnable": qosVlanIeee8021qSubstitutionEnable,
       "qosVlanIeee8021qSubstitutionVlanID": qosVlanIeee8021qSubstitutionVlanID,
       "qosVlanIeee8021qSubstitutionUserPriority": qosVlanIeee8021qSubstitutionUserPriority,
       "qosVlanIeee8021qSubstitutionFiltering": qosVlanIeee8021qSubstitutionFiltering,
       "qosInterop": qosInterop,
       "qosInteropUseVoiceQoSForRtcpEnable": qosInteropUseVoiceQoSForRtcpEnable,
       "qosConformance": qosConformance,
       "qosCompliances": qosCompliances,
       "qosAnalogComplVer1": qosAnalogComplVer1,
       "qosGroups": qosGroups,
       "qosDiffServGroupVer1": qosDiffServGroupVer1,
       "qosIeee8021qGroupVer1": qosIeee8021qGroupVer1,
       "qosIeee8021qSubstitutionGroupVer1": qosIeee8021qSubstitutionGroupVer1,
       "qosInteropGroupVer1": qosInteropGroupVer1}
)
