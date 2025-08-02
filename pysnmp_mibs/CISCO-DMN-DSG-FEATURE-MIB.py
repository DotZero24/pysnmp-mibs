_H='installedOptionIdx'
_G='not-accessible'
_F='featureLicenceIdx'
_E='CISCO-DMN-DSG-FEATURE-MIB'
_D='Integer32'
_C='read-only'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
ciscoDSGFeature=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,27))
if mibBuilder.loadTexts:ciscoDSGFeature.setRevisions(('2012-02-28 18:00',))
_FeatureTable_ObjectIdentity=ObjectIdentity
featureTable=_FeatureTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,27,2))
_FeatureLicenceTable_Object=MibTable
featureLicenceTable=_FeatureLicenceTable_Object((1,3,6,1,4,1,1429,2,2,5,27,2,1))
if mibBuilder.loadTexts:featureLicenceTable.setStatus(_A)
_FeatureLicenceEntry_Object=MibTableRow
featureLicenceEntry=_FeatureLicenceEntry_Object((1,3,6,1,4,1,1429,2,2,5,27,2,1,1))
featureLicenceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:featureLicenceEntry.setStatus(_A)
class _FeatureLicenceIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_FeatureLicenceIdx_Type.__name__=_D
_FeatureLicenceIdx_Object=MibTableColumn
featureLicenceIdx=_FeatureLicenceIdx_Object((1,3,6,1,4,1,1429,2,2,5,27,2,1,1,1),_FeatureLicenceIdx_Type())
featureLicenceIdx.setMaxAccess(_G)
if mibBuilder.loadTexts:featureLicenceIdx.setStatus(_A)
class _FeatureLicenceID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FeatureLicenceID_Type.__name__=_B
_FeatureLicenceID_Object=MibTableColumn
featureLicenceID=_FeatureLicenceID_Object((1,3,6,1,4,1,1429,2,2,5,27,2,1,1,2),_FeatureLicenceID_Type())
featureLicenceID.setMaxAccess(_C)
if mibBuilder.loadTexts:featureLicenceID.setStatus(_A)
class _FeatureLicenceStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FeatureLicenceStatus_Type.__name__=_B
_FeatureLicenceStatus_Object=MibTableColumn
featureLicenceStatus=_FeatureLicenceStatus_Object((1,3,6,1,4,1,1429,2,2,5,27,2,1,1,3),_FeatureLicenceStatus_Type())
featureLicenceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:featureLicenceStatus.setStatus(_A)
_InstalledOptionTable_Object=MibTable
installedOptionTable=_InstalledOptionTable_Object((1,3,6,1,4,1,1429,2,2,5,27,2,2))
if mibBuilder.loadTexts:installedOptionTable.setStatus(_A)
_InstalledOptionEntry_Object=MibTableRow
installedOptionEntry=_InstalledOptionEntry_Object((1,3,6,1,4,1,1429,2,2,5,27,2,2,1))
installedOptionEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:installedOptionEntry.setStatus(_A)
class _InstalledOptionIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_InstalledOptionIdx_Type.__name__=_D
_InstalledOptionIdx_Object=MibTableColumn
installedOptionIdx=_InstalledOptionIdx_Object((1,3,6,1,4,1,1429,2,2,5,27,2,2,1,1),_InstalledOptionIdx_Type())
installedOptionIdx.setMaxAccess(_G)
if mibBuilder.loadTexts:installedOptionIdx.setStatus(_A)
class _InstalledOptionID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_InstalledOptionID_Type.__name__=_B
_InstalledOptionID_Object=MibTableColumn
installedOptionID=_InstalledOptionID_Object((1,3,6,1,4,1,1429,2,2,5,27,2,2,1,2),_InstalledOptionID_Type())
installedOptionID.setMaxAccess(_C)
if mibBuilder.loadTexts:installedOptionID.setStatus(_A)
class _InstalledOptionStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_InstalledOptionStatus_Type.__name__=_B
_InstalledOptionStatus_Object=MibTableColumn
installedOptionStatus=_InstalledOptionStatus_Object((1,3,6,1,4,1,1429,2,2,5,27,2,2,1,3),_InstalledOptionStatus_Type())
installedOptionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:installedOptionStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGFeature':ciscoDSGFeature,'featureTable':featureTable,'featureLicenceTable':featureLicenceTable,'featureLicenceEntry':featureLicenceEntry,_F:featureLicenceIdx,'featureLicenceID':featureLicenceID,'featureLicenceStatus':featureLicenceStatus,'installedOptionTable':installedOptionTable,'installedOptionEntry':installedOptionEntry,_H:installedOptionIdx,'installedOptionID':installedOptionID,'installedOptionStatus':installedOptionStatus})