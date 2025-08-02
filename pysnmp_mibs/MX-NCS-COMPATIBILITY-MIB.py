_G='ncsCompatibilityBasicGroupVer1'
_F='ncsCompatibilityVersion'
_E='ncsCompatibilityRtpPayloadType18EncodingName'
_D='read-write'
_C='Integer32'
_B='MX-NCS-COMPATIBILITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ncsCompatibilityMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,15))
if mibBuilder.loadTexts:ncsCompatibilityMIB.setRevisions(('2008-12-03 00:00','1902-08-28 00:00'))
_NcsCompatibilityMIBObjects_ObjectIdentity=ObjectIdentity
ncsCompatibilityMIBObjects=_NcsCompatibilityMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,15,1))
class _NcsCompatibilityRtpPayloadType18EncodingName_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('g729',0),('g729A',1)))
_NcsCompatibilityRtpPayloadType18EncodingName_Type.__name__=_C
_NcsCompatibilityRtpPayloadType18EncodingName_Object=MibScalar
ncsCompatibilityRtpPayloadType18EncodingName=_NcsCompatibilityRtpPayloadType18EncodingName_Object((1,3,6,1,4,1,4935,99,15,1,5),_NcsCompatibilityRtpPayloadType18EncodingName_Type())
ncsCompatibilityRtpPayloadType18EncodingName.setMaxAccess(_D)
if mibBuilder.loadTexts:ncsCompatibilityRtpPayloadType18EncodingName.setStatus(_A)
class _NcsCompatibilityVersion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('mgcp01Ncs10',0),('fakeMgcp10Ncs10',1)))
_NcsCompatibilityVersion_Type.__name__=_C
_NcsCompatibilityVersion_Object=MibScalar
ncsCompatibilityVersion=_NcsCompatibilityVersion_Object((1,3,6,1,4,1,4935,99,15,1,100),_NcsCompatibilityVersion_Type())
ncsCompatibilityVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:ncsCompatibilityVersion.setStatus(_A)
_NcsCompatibilityConformance_ObjectIdentity=ObjectIdentity
ncsCompatibilityConformance=_NcsCompatibilityConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,15,2))
_NcsCompatibilityCompliances_ObjectIdentity=ObjectIdentity
ncsCompatibilityCompliances=_NcsCompatibilityCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,15,2,1))
_NcsCompatibilityGroups_ObjectIdentity=ObjectIdentity
ncsCompatibilityGroups=_NcsCompatibilityGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,15,2,2))
ncsCompatibilityBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,15,2,2,10))
ncsCompatibilityBasicGroupVer1.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:ncsCompatibilityBasicGroupVer1.setStatus(_A)
ncsCompatibilityComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,15,2,1,10))
ncsCompatibilityComplVer1.setObjects((_B,_G))
if mibBuilder.loadTexts:ncsCompatibilityComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ncsCompatibilityMIB':ncsCompatibilityMIB,'ncsCompatibilityMIBObjects':ncsCompatibilityMIBObjects,_E:ncsCompatibilityRtpPayloadType18EncodingName,_F:ncsCompatibilityVersion,'ncsCompatibilityConformance':ncsCompatibilityConformance,'ncsCompatibilityCompliances':ncsCompatibilityCompliances,'ncsCompatibilityComplVer1':ncsCompatibilityComplVer1,'ncsCompatibilityGroups':ncsCompatibilityGroups,_G:ncsCompatibilityBasicGroupVer1})