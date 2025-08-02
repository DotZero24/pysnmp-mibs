_W='ssmProvDppGroup'
_V='ssmProvFeatureIfGroup'
_U='ssmProvFeatureGroup'
_T='ssmProvDppName'
_S='ssmProvDppEndPort'
_R='ssmProvFeatureIfRowStatus'
_Q='ssmProvFeatureIfPartnerImageURI'
_P='ssmProvFeatureIfForceRemove'
_O='ssmProvFeatureNeedsImage'
_N='ssmProvDppStartPort'
_M='ssmProvFeatureIfFeatureName'
_L='ssmProvFeatureIfEndPort'
_K='ssmProvFeatureIfStartPort'
_J='ssmProvFeatureName'
_I='Integer32'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='read-create'
_E='read-only'
_D='not-accessible'
_C='SnmpAdminString'
_B='CISCO-SSM-PROV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoSsmProvMIB=ModuleIdentity((1,3,6,1,4,1,9,9,448))
if mibBuilder.loadTexts:ciscoSsmProvMIB.setRevisions(('2005-02-15 00:00',))
_CiscoSsmProvMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSsmProvMIBObjects=_CiscoSsmProvMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,448,1))
_SsmProvConfiguration_ObjectIdentity=ObjectIdentity
ssmProvConfiguration=_SsmProvConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,448,1,1))
_SsmProvFeatureTable_Object=MibTable
ssmProvFeatureTable=_SsmProvFeatureTable_Object((1,3,6,1,4,1,9,9,448,1,1,1))
if mibBuilder.loadTexts:ssmProvFeatureTable.setStatus(_A)
_SsmProvFeatureEntry_Object=MibTableRow
ssmProvFeatureEntry=_SsmProvFeatureEntry_Object((1,3,6,1,4,1,9,9,448,1,1,1,1))
ssmProvFeatureEntry.setIndexNames((0,_G,_H),(0,_B,_J))
if mibBuilder.loadTexts:ssmProvFeatureEntry.setStatus(_A)
class _SsmProvFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_SsmProvFeatureName_Type.__name__=_C
_SsmProvFeatureName_Object=MibTableColumn
ssmProvFeatureName=_SsmProvFeatureName_Object((1,3,6,1,4,1,9,9,448,1,1,1,1,1),_SsmProvFeatureName_Type())
ssmProvFeatureName.setMaxAccess(_D)
if mibBuilder.loadTexts:ssmProvFeatureName.setStatus(_A)
_SsmProvFeatureNeedsImage_Type=TruthValue
_SsmProvFeatureNeedsImage_Object=MibTableColumn
ssmProvFeatureNeedsImage=_SsmProvFeatureNeedsImage_Object((1,3,6,1,4,1,9,9,448,1,1,1,1,2),_SsmProvFeatureNeedsImage_Type())
ssmProvFeatureNeedsImage.setMaxAccess(_E)
if mibBuilder.loadTexts:ssmProvFeatureNeedsImage.setStatus(_A)
_SsmProvFeatureIfTable_Object=MibTable
ssmProvFeatureIfTable=_SsmProvFeatureIfTable_Object((1,3,6,1,4,1,9,9,448,1,1,2))
if mibBuilder.loadTexts:ssmProvFeatureIfTable.setStatus(_A)
_SsmProvFeatureIfEntry_Object=MibTableRow
ssmProvFeatureIfEntry=_SsmProvFeatureIfEntry_Object((1,3,6,1,4,1,9,9,448,1,1,2,1))
ssmProvFeatureIfEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:ssmProvFeatureIfEntry.setStatus(_A)
_SsmProvFeatureIfStartPort_Type=InterfaceIndex
_SsmProvFeatureIfStartPort_Object=MibTableColumn
ssmProvFeatureIfStartPort=_SsmProvFeatureIfStartPort_Object((1,3,6,1,4,1,9,9,448,1,1,2,1,1),_SsmProvFeatureIfStartPort_Type())
ssmProvFeatureIfStartPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ssmProvFeatureIfStartPort.setStatus(_A)
_SsmProvFeatureIfEndPort_Type=InterfaceIndex
_SsmProvFeatureIfEndPort_Object=MibTableColumn
ssmProvFeatureIfEndPort=_SsmProvFeatureIfEndPort_Object((1,3,6,1,4,1,9,9,448,1,1,2,1,2),_SsmProvFeatureIfEndPort_Type())
ssmProvFeatureIfEndPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ssmProvFeatureIfEndPort.setStatus(_A)
class _SsmProvFeatureIfFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_SsmProvFeatureIfFeatureName_Type.__name__=_C
_SsmProvFeatureIfFeatureName_Object=MibTableColumn
ssmProvFeatureIfFeatureName=_SsmProvFeatureIfFeatureName_Object((1,3,6,1,4,1,9,9,448,1,1,2,1,3),_SsmProvFeatureIfFeatureName_Type())
ssmProvFeatureIfFeatureName.setMaxAccess(_D)
if mibBuilder.loadTexts:ssmProvFeatureIfFeatureName.setStatus(_A)
class _SsmProvFeatureIfForceRemove_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forceReset',1),('noop',2)))
_SsmProvFeatureIfForceRemove_Type.__name__=_I
_SsmProvFeatureIfForceRemove_Object=MibTableColumn
ssmProvFeatureIfForceRemove=_SsmProvFeatureIfForceRemove_Object((1,3,6,1,4,1,9,9,448,1,1,2,1,4),_SsmProvFeatureIfForceRemove_Type())
ssmProvFeatureIfForceRemove.setMaxAccess(_F)
if mibBuilder.loadTexts:ssmProvFeatureIfForceRemove.setStatus(_A)
class _SsmProvFeatureIfPartnerImageURI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_SsmProvFeatureIfPartnerImageURI_Type.__name__=_C
_SsmProvFeatureIfPartnerImageURI_Object=MibTableColumn
ssmProvFeatureIfPartnerImageURI=_SsmProvFeatureIfPartnerImageURI_Object((1,3,6,1,4,1,9,9,448,1,1,2,1,5),_SsmProvFeatureIfPartnerImageURI_Type())
ssmProvFeatureIfPartnerImageURI.setMaxAccess(_F)
if mibBuilder.loadTexts:ssmProvFeatureIfPartnerImageURI.setStatus(_A)
_SsmProvFeatureIfRowStatus_Type=RowStatus
_SsmProvFeatureIfRowStatus_Object=MibTableColumn
ssmProvFeatureIfRowStatus=_SsmProvFeatureIfRowStatus_Object((1,3,6,1,4,1,9,9,448,1,1,2,1,6),_SsmProvFeatureIfRowStatus_Type())
ssmProvFeatureIfRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ssmProvFeatureIfRowStatus.setStatus(_A)
_SsmProvDppTable_Object=MibTable
ssmProvDppTable=_SsmProvDppTable_Object((1,3,6,1,4,1,9,9,448,1,1,3))
if mibBuilder.loadTexts:ssmProvDppTable.setStatus(_A)
_SsmProvDppEntry_Object=MibTableRow
ssmProvDppEntry=_SsmProvDppEntry_Object((1,3,6,1,4,1,9,9,448,1,1,3,1))
ssmProvDppEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ssmProvDppEntry.setStatus(_A)
_SsmProvDppStartPort_Type=InterfaceIndex
_SsmProvDppStartPort_Object=MibTableColumn
ssmProvDppStartPort=_SsmProvDppStartPort_Object((1,3,6,1,4,1,9,9,448,1,1,3,1,1),_SsmProvDppStartPort_Type())
ssmProvDppStartPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ssmProvDppStartPort.setStatus(_A)
_SsmProvDppEndPort_Type=InterfaceIndex
_SsmProvDppEndPort_Object=MibTableColumn
ssmProvDppEndPort=_SsmProvDppEndPort_Object((1,3,6,1,4,1,9,9,448,1,1,3,1,2),_SsmProvDppEndPort_Type())
ssmProvDppEndPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ssmProvDppEndPort.setStatus(_A)
class _SsmProvDppName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_SsmProvDppName_Type.__name__=_C
_SsmProvDppName_Object=MibTableColumn
ssmProvDppName=_SsmProvDppName_Object((1,3,6,1,4,1,9,9,448,1,1,3,1,3),_SsmProvDppName_Type())
ssmProvDppName.setMaxAccess(_E)
if mibBuilder.loadTexts:ssmProvDppName.setStatus(_A)
_CiscoSsmProvMIBConform_ObjectIdentity=ObjectIdentity
ciscoSsmProvMIBConform=_CiscoSsmProvMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,448,2))
_SsmProvMIBCompliances_ObjectIdentity=ObjectIdentity
ssmProvMIBCompliances=_SsmProvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,448,2,1))
_SsmProvMIBGroups_ObjectIdentity=ObjectIdentity
ssmProvMIBGroups=_SsmProvMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,448,2,2))
ssmProvFeatureGroup=ObjectGroup((1,3,6,1,4,1,9,9,448,2,2,1))
ssmProvFeatureGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:ssmProvFeatureGroup.setStatus(_A)
ssmProvFeatureIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,448,2,2,2))
ssmProvFeatureIfGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ssmProvFeatureIfGroup.setStatus(_A)
ssmProvDppGroup=ObjectGroup((1,3,6,1,4,1,9,9,448,2,2,3))
ssmProvDppGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ssmProvDppGroup.setStatus(_A)
ssmProvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,448,2,1,1))
ssmProvMIBCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ssmProvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSsmProvMIB':ciscoSsmProvMIB,'ciscoSsmProvMIBObjects':ciscoSsmProvMIBObjects,'ssmProvConfiguration':ssmProvConfiguration,'ssmProvFeatureTable':ssmProvFeatureTable,'ssmProvFeatureEntry':ssmProvFeatureEntry,_J:ssmProvFeatureName,_O:ssmProvFeatureNeedsImage,'ssmProvFeatureIfTable':ssmProvFeatureIfTable,'ssmProvFeatureIfEntry':ssmProvFeatureIfEntry,_K:ssmProvFeatureIfStartPort,_L:ssmProvFeatureIfEndPort,_M:ssmProvFeatureIfFeatureName,_P:ssmProvFeatureIfForceRemove,_Q:ssmProvFeatureIfPartnerImageURI,_R:ssmProvFeatureIfRowStatus,'ssmProvDppTable':ssmProvDppTable,'ssmProvDppEntry':ssmProvDppEntry,_N:ssmProvDppStartPort,_S:ssmProvDppEndPort,_T:ssmProvDppName,'ciscoSsmProvMIBConform':ciscoSsmProvMIBConform,'ssmProvMIBCompliances':ssmProvMIBCompliances,'ssmProvMIBCompliance':ssmProvMIBCompliance,'ssmProvMIBGroups':ssmProvMIBGroups,_U:ssmProvFeatureGroup,_V:ssmProvFeatureIfGroup,_W:ssmProvDppGroup})