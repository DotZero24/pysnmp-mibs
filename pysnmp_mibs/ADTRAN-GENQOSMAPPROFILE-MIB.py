_F='adGenQosMapProfileName'
_E='ADTRAN-GENQOSMAPPROFILE-MIB'
_D='read-only'
_C='read-create'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','RowStatus','TextualConvention')
adGenQosMapProfileMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,83))
if mibBuilder.loadTexts:adGenQosMapProfileMIB.setRevisions(('2012-05-17 00:00','2012-04-09 04:51'))
_AdGenQosMapProfile_ObjectIdentity=ObjectIdentity
adGenQosMapProfile=_AdGenQosMapProfile_ObjectIdentity((1,3,6,1,4,1,664,5,83))
_AdGenQosMapProfileProvisioning_ObjectIdentity=ObjectIdentity
adGenQosMapProfileProvisioning=_AdGenQosMapProfileProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,83,1))
_AdGenQosMapProfileProvisioningTable_Object=MibTable
adGenQosMapProfileProvisioningTable=_AdGenQosMapProfileProvisioningTable_Object((1,3,6,1,4,1,664,5,83,1,1))
if mibBuilder.loadTexts:adGenQosMapProfileProvisioningTable.setStatus(_A)
_AdGenQosMapProfileProvisioningEntry_Object=MibTableRow
adGenQosMapProfileProvisioningEntry=_AdGenQosMapProfileProvisioningEntry_Object((1,3,6,1,4,1,664,5,83,1,1,1))
adGenQosMapProfileProvisioningEntry.setIndexNames((1,_E,_F))
if mibBuilder.loadTexts:adGenQosMapProfileProvisioningEntry.setStatus(_A)
class _AdGenQosMapProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenQosMapProfileName_Type.__name__=_B
_AdGenQosMapProfileName_Object=MibTableColumn
adGenQosMapProfileName=_AdGenQosMapProfileName_Object((1,3,6,1,4,1,664,5,83,1,1,1,1),_AdGenQosMapProfileName_Type())
adGenQosMapProfileName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenQosMapProfileName.setStatus(_A)
_AdGenQosMapProfileClassification_Type=OctetString
_AdGenQosMapProfileClassification_Object=MibTableColumn
adGenQosMapProfileClassification=_AdGenQosMapProfileClassification_Object((1,3,6,1,4,1,664,5,83,1,1,1,2),_AdGenQosMapProfileClassification_Type())
adGenQosMapProfileClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenQosMapProfileClassification.setStatus(_A)
_AdGenQosMapProfileRowStatus_Type=RowStatus
_AdGenQosMapProfileRowStatus_Object=MibTableColumn
adGenQosMapProfileRowStatus=_AdGenQosMapProfileRowStatus_Object((1,3,6,1,4,1,664,5,83,1,1,1,3),_AdGenQosMapProfileRowStatus_Type())
adGenQosMapProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenQosMapProfileRowStatus.setStatus(_A)
class _AdGenQosMapProfileDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenQosMapProfileDescription_Type.__name__=_B
_AdGenQosMapProfileDescription_Object=MibTableColumn
adGenQosMapProfileDescription=_AdGenQosMapProfileDescription_Object((1,3,6,1,4,1,664,5,83,1,1,1,4),_AdGenQosMapProfileDescription_Type())
adGenQosMapProfileDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenQosMapProfileDescription.setStatus(_A)
_AdGenQosMapProfileStatus_ObjectIdentity=ObjectIdentity
adGenQosMapProfileStatus=_AdGenQosMapProfileStatus_ObjectIdentity((1,3,6,1,4,1,664,5,83,2))
_AdGenQosMapProfileLastInsertStatus_Type=DisplayString
_AdGenQosMapProfileLastInsertStatus_Object=MibScalar
adGenQosMapProfileLastInsertStatus=_AdGenQosMapProfileLastInsertStatus_Object((1,3,6,1,4,1,664,5,83,2,1),_AdGenQosMapProfileLastInsertStatus_Type())
adGenQosMapProfileLastInsertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenQosMapProfileLastInsertStatus.setStatus(_A)
_AdGenQosMapProfileMaxAllowedProfiles_Type=Unsigned32
_AdGenQosMapProfileMaxAllowedProfiles_Object=MibScalar
adGenQosMapProfileMaxAllowedProfiles=_AdGenQosMapProfileMaxAllowedProfiles_Object((1,3,6,1,4,1,664,5,83,2,2),_AdGenQosMapProfileMaxAllowedProfiles_Type())
adGenQosMapProfileMaxAllowedProfiles.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenQosMapProfileMaxAllowedProfiles.setStatus(_A)
_AdGenQosMapProfileCurrentProfileCount_Type=Unsigned32
_AdGenQosMapProfileCurrentProfileCount_Object=MibScalar
adGenQosMapProfileCurrentProfileCount=_AdGenQosMapProfileCurrentProfileCount_Object((1,3,6,1,4,1,664,5,83,2,3),_AdGenQosMapProfileCurrentProfileCount_Type())
adGenQosMapProfileCurrentProfileCount.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenQosMapProfileCurrentProfileCount.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'adGenQosMapProfile':adGenQosMapProfile,'adGenQosMapProfileProvisioning':adGenQosMapProfileProvisioning,'adGenQosMapProfileProvisioningTable':adGenQosMapProfileProvisioningTable,'adGenQosMapProfileProvisioningEntry':adGenQosMapProfileProvisioningEntry,_F:adGenQosMapProfileName,'adGenQosMapProfileClassification':adGenQosMapProfileClassification,'adGenQosMapProfileRowStatus':adGenQosMapProfileRowStatus,'adGenQosMapProfileDescription':adGenQosMapProfileDescription,'adGenQosMapProfileStatus':adGenQosMapProfileStatus,'adGenQosMapProfileLastInsertStatus':adGenQosMapProfileLastInsertStatus,'adGenQosMapProfileMaxAllowedProfiles':adGenQosMapProfileMaxAllowedProfiles,'adGenQosMapProfileCurrentProfileCount':adGenQosMapProfileCurrentProfileCount,'adGenQosMapProfileMIB':adGenQosMapProfileMIB})