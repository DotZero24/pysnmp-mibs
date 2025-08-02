_d='ciVplsBgpExtPwBindGroup'
_c='ciVplsBgpExtVEGroup'
_b='ciVplsBgpExtRTGroup'
_a='ciVplsBgpExtConfigGroup'
_Z='ciVplsBgpExtPwBindRemoteVEId'
_Y='ciVplsBgpExtPwBindLocalVEId'
_X='ciVplsBgpExtVEStorageType'
_W='ciVplsBgpExtVERowStatus'
_V='ciVplsBgpExtVEPreference'
_U='ciVplsBgpExtVEName'
_T='ciVplsBgpExtRTRowStatus'
_S='ciVplsBgpExtRTStorageType'
_R='ciVplsBgpExtConfigVERangeSize'
_Q='ciVplsBgpExtConfigRouteDistinguisher'
_P='read-only'
_O='ciVplsBgpExtVEId'
_N='CiVplsBgpExtRouteTarget'
_M='read-write'
_L='CiVplsBgpExtRouteDistinguisher'
_K='SnmpAdminString'
_J='cvplsPwBindIndex'
_I='ciVplsBgpExtRT'
_H='ciVplsBgpExtRTType'
_G='StorageType'
_F='Unsigned32'
_E='cvplsConfigIndex'
_D='CISCO-IETF-VPLS-GENERIC-MIB'
_C='read-create'
_B='CISCO-IETF-VPLS-BGP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cvplsConfigIndex,cvplsPwBindIndex=mibBuilder.importSymbols(_D,_E,_J)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_G,'TextualConvention')
ciscoIetfVplsBgpExtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,140))
if mibBuilder.loadTexts:ciscoIetfVplsBgpExtMIB.setRevisions(('2008-10-24 00:00',))
class CiVplsBgpExtRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class CiVplsBgpExtRouteTarget(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class CiVplsBgpExtRouteTargetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
class CiVplsBgpExtVEID(TextualConvention,Unsigned32):status=_A
_CiscoIetfVplsBgpExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIetfVplsBgpExtMIBNotifs=_CiscoIetfVplsBgpExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,140,0))
_CiscoIetfVplsBgpExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIetfVplsBgpExtMIBObjects=_CiscoIetfVplsBgpExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,140,1))
_CiVplsBgpExtConfigTable_Object=MibTable
ciVplsBgpExtConfigTable=_CiVplsBgpExtConfigTable_Object((1,3,6,1,4,1,9,10,140,1,1))
if mibBuilder.loadTexts:ciVplsBgpExtConfigTable.setStatus(_A)
_CiVplsBgpExtConfigEntry_Object=MibTableRow
ciVplsBgpExtConfigEntry=_CiVplsBgpExtConfigEntry_Object((1,3,6,1,4,1,9,10,140,1,1,1))
ciVplsBgpExtConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ciVplsBgpExtConfigEntry.setStatus(_A)
class _CiVplsBgpExtConfigRouteDistinguisher_Type(CiVplsBgpExtRouteDistinguisher):defaultValue=OctetString('')
_CiVplsBgpExtConfigRouteDistinguisher_Type.__name__=_L
_CiVplsBgpExtConfigRouteDistinguisher_Object=MibTableColumn
ciVplsBgpExtConfigRouteDistinguisher=_CiVplsBgpExtConfigRouteDistinguisher_Object((1,3,6,1,4,1,9,10,140,1,1,1,1),_CiVplsBgpExtConfigRouteDistinguisher_Type())
ciVplsBgpExtConfigRouteDistinguisher.setMaxAccess(_M)
if mibBuilder.loadTexts:ciVplsBgpExtConfigRouteDistinguisher.setStatus(_A)
class _CiVplsBgpExtConfigVERangeSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiVplsBgpExtConfigVERangeSize_Type.__name__=_F
_CiVplsBgpExtConfigVERangeSize_Object=MibTableColumn
ciVplsBgpExtConfigVERangeSize=_CiVplsBgpExtConfigVERangeSize_Object((1,3,6,1,4,1,9,10,140,1,1,1,4),_CiVplsBgpExtConfigVERangeSize_Type())
ciVplsBgpExtConfigVERangeSize.setMaxAccess(_M)
if mibBuilder.loadTexts:ciVplsBgpExtConfigVERangeSize.setStatus(_A)
_CivplsBgpExtRTTable_Object=MibTable
civplsBgpExtRTTable=_CivplsBgpExtRTTable_Object((1,3,6,1,4,1,9,10,140,1,2))
if mibBuilder.loadTexts:civplsBgpExtRTTable.setStatus(_A)
_CivplsBgpExtRTEntry_Object=MibTableRow
civplsBgpExtRTEntry=_CivplsBgpExtRTEntry_Object((1,3,6,1,4,1,9,10,140,1,2,1))
civplsBgpExtRTEntry.setIndexNames((0,_D,_E),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:civplsBgpExtRTEntry.setStatus(_A)
_CiVplsBgpExtRTType_Type=CiVplsBgpExtRouteTargetType
_CiVplsBgpExtRTType_Object=MibTableColumn
ciVplsBgpExtRTType=_CiVplsBgpExtRTType_Object((1,3,6,1,4,1,9,10,140,1,2,1,1),_CiVplsBgpExtRTType_Type())
ciVplsBgpExtRTType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciVplsBgpExtRTType.setStatus(_A)
class _CiVplsBgpExtRT_Type(CiVplsBgpExtRouteTarget):subtypeSpec=CiVplsBgpExtRouteTarget.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CiVplsBgpExtRT_Type.__name__=_N
_CiVplsBgpExtRT_Object=MibTableColumn
ciVplsBgpExtRT=_CiVplsBgpExtRT_Object((1,3,6,1,4,1,9,10,140,1,2,1,2),_CiVplsBgpExtRT_Type())
ciVplsBgpExtRT.setMaxAccess(_C)
if mibBuilder.loadTexts:ciVplsBgpExtRT.setStatus(_A)
class _CiVplsBgpExtRTStorageType_Type(StorageType):defaultValue=2
_CiVplsBgpExtRTStorageType_Type.__name__=_G
_CiVplsBgpExtRTStorageType_Object=MibTableColumn
ciVplsBgpExtRTStorageType=_CiVplsBgpExtRTStorageType_Object((1,3,6,1,4,1,9,10,140,1,2,1,3),_CiVplsBgpExtRTStorageType_Type())
ciVplsBgpExtRTStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciVplsBgpExtRTStorageType.setStatus(_A)
_CiVplsBgpExtRTRowStatus_Type=RowStatus
_CiVplsBgpExtRTRowStatus_Object=MibTableColumn
ciVplsBgpExtRTRowStatus=_CiVplsBgpExtRTRowStatus_Object((1,3,6,1,4,1,9,10,140,1,2,1,4),_CiVplsBgpExtRTRowStatus_Type())
ciVplsBgpExtRTRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciVplsBgpExtRTRowStatus.setStatus(_A)
_CiVplsBgpExtVETable_Object=MibTable
ciVplsBgpExtVETable=_CiVplsBgpExtVETable_Object((1,3,6,1,4,1,9,10,140,1,3))
if mibBuilder.loadTexts:ciVplsBgpExtVETable.setStatus(_A)
_CiVplsBgpExtVEEntry_Object=MibTableRow
ciVplsBgpExtVEEntry=_CiVplsBgpExtVEEntry_Object((1,3,6,1,4,1,9,10,140,1,3,1))
ciVplsBgpExtVEEntry.setIndexNames((0,_D,_E),(0,_B,_O))
if mibBuilder.loadTexts:ciVplsBgpExtVEEntry.setStatus(_A)
_CiVplsBgpExtVEId_Type=CiVplsBgpExtVEID
_CiVplsBgpExtVEId_Object=MibTableColumn
ciVplsBgpExtVEId=_CiVplsBgpExtVEId_Object((1,3,6,1,4,1,9,10,140,1,3,1,1),_CiVplsBgpExtVEId_Type())
ciVplsBgpExtVEId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciVplsBgpExtVEId.setStatus(_A)
class _CiVplsBgpExtVEName_Type(SnmpAdminString):defaultValue=OctetString('')
_CiVplsBgpExtVEName_Type.__name__=_K
_CiVplsBgpExtVEName_Object=MibTableColumn
ciVplsBgpExtVEName=_CiVplsBgpExtVEName_Object((1,3,6,1,4,1,9,10,140,1,3,1,2),_CiVplsBgpExtVEName_Type())
ciVplsBgpExtVEName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciVplsBgpExtVEName.setStatus(_A)
class _CiVplsBgpExtVEPreference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiVplsBgpExtVEPreference_Type.__name__=_F
_CiVplsBgpExtVEPreference_Object=MibTableColumn
ciVplsBgpExtVEPreference=_CiVplsBgpExtVEPreference_Object((1,3,6,1,4,1,9,10,140,1,3,1,3),_CiVplsBgpExtVEPreference_Type())
ciVplsBgpExtVEPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:ciVplsBgpExtVEPreference.setStatus(_A)
class _CiVplsBgpExtVEStorageType_Type(StorageType):defaultValue=2
_CiVplsBgpExtVEStorageType_Type.__name__=_G
_CiVplsBgpExtVEStorageType_Object=MibTableColumn
ciVplsBgpExtVEStorageType=_CiVplsBgpExtVEStorageType_Object((1,3,6,1,4,1,9,10,140,1,3,1,5),_CiVplsBgpExtVEStorageType_Type())
ciVplsBgpExtVEStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciVplsBgpExtVEStorageType.setStatus(_A)
_CiVplsBgpExtVERowStatus_Type=RowStatus
_CiVplsBgpExtVERowStatus_Object=MibTableColumn
ciVplsBgpExtVERowStatus=_CiVplsBgpExtVERowStatus_Object((1,3,6,1,4,1,9,10,140,1,3,1,6),_CiVplsBgpExtVERowStatus_Type())
ciVplsBgpExtVERowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciVplsBgpExtVERowStatus.setStatus(_A)
_CiVplsBgpExtPwBindTable_Object=MibTable
ciVplsBgpExtPwBindTable=_CiVplsBgpExtPwBindTable_Object((1,3,6,1,4,1,9,10,140,1,4))
if mibBuilder.loadTexts:ciVplsBgpExtPwBindTable.setStatus(_A)
_CiVplsBgpExtPwBindEntry_Object=MibTableRow
ciVplsBgpExtPwBindEntry=_CiVplsBgpExtPwBindEntry_Object((1,3,6,1,4,1,9,10,140,1,4,1))
ciVplsBgpExtPwBindEntry.setIndexNames((0,_D,_E),(0,_D,_J))
if mibBuilder.loadTexts:ciVplsBgpExtPwBindEntry.setStatus(_A)
_CiVplsBgpExtPwBindLocalVEId_Type=CiVplsBgpExtVEID
_CiVplsBgpExtPwBindLocalVEId_Object=MibTableColumn
ciVplsBgpExtPwBindLocalVEId=_CiVplsBgpExtPwBindLocalVEId_Object((1,3,6,1,4,1,9,10,140,1,4,1,1),_CiVplsBgpExtPwBindLocalVEId_Type())
ciVplsBgpExtPwBindLocalVEId.setMaxAccess(_P)
if mibBuilder.loadTexts:ciVplsBgpExtPwBindLocalVEId.setStatus(_A)
_CiVplsBgpExtPwBindRemoteVEId_Type=CiVplsBgpExtVEID
_CiVplsBgpExtPwBindRemoteVEId_Object=MibTableColumn
ciVplsBgpExtPwBindRemoteVEId=_CiVplsBgpExtPwBindRemoteVEId_Object((1,3,6,1,4,1,9,10,140,1,4,1,2),_CiVplsBgpExtPwBindRemoteVEId_Type())
ciVplsBgpExtPwBindRemoteVEId.setMaxAccess(_P)
if mibBuilder.loadTexts:ciVplsBgpExtPwBindRemoteVEId.setStatus(_A)
_CiscoIetfVplsBgpExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoIetfVplsBgpExtMIBConform=_CiscoIetfVplsBgpExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,10,140,2))
_CiscoIetfVplsBgpExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIetfVplsBgpExtMIBCompliances=_CiscoIetfVplsBgpExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,140,2,1))
_CiscoIetfVplsBgpExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIetfVplsBgpExtMIBGroups=_CiscoIetfVplsBgpExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,140,2,2))
ciVplsBgpExtConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,140,2,2,1))
ciVplsBgpExtConfigGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciVplsBgpExtConfigGroup.setStatus(_A)
ciVplsBgpExtRTGroup=ObjectGroup((1,3,6,1,4,1,9,10,140,2,2,2))
ciVplsBgpExtRTGroup.setObjects(*((_B,_H),(_B,_I),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciVplsBgpExtRTGroup.setStatus(_A)
ciVplsBgpExtVEGroup=ObjectGroup((1,3,6,1,4,1,9,10,140,2,2,3))
ciVplsBgpExtVEGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciVplsBgpExtVEGroup.setStatus(_A)
ciVplsBgpExtPwBindGroup=ObjectGroup((1,3,6,1,4,1,9,10,140,2,2,4))
ciVplsBgpExtPwBindGroup.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:ciVplsBgpExtPwBindGroup.setStatus(_A)
ciscoIetfVplsBgpExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,140,2,1,1))
ciscoIetfVplsBgpExtMIBCompliance.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ciscoIetfVplsBgpExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_L:CiVplsBgpExtRouteDistinguisher,_N:CiVplsBgpExtRouteTarget,'CiVplsBgpExtRouteTargetType':CiVplsBgpExtRouteTargetType,'CiVplsBgpExtVEID':CiVplsBgpExtVEID,'ciscoIetfVplsBgpExtMIB':ciscoIetfVplsBgpExtMIB,'ciscoIetfVplsBgpExtMIBNotifs':ciscoIetfVplsBgpExtMIBNotifs,'ciscoIetfVplsBgpExtMIBObjects':ciscoIetfVplsBgpExtMIBObjects,'ciVplsBgpExtConfigTable':ciVplsBgpExtConfigTable,'ciVplsBgpExtConfigEntry':ciVplsBgpExtConfigEntry,_Q:ciVplsBgpExtConfigRouteDistinguisher,_R:ciVplsBgpExtConfigVERangeSize,'civplsBgpExtRTTable':civplsBgpExtRTTable,'civplsBgpExtRTEntry':civplsBgpExtRTEntry,_H:ciVplsBgpExtRTType,_I:ciVplsBgpExtRT,_S:ciVplsBgpExtRTStorageType,_T:ciVplsBgpExtRTRowStatus,'ciVplsBgpExtVETable':ciVplsBgpExtVETable,'ciVplsBgpExtVEEntry':ciVplsBgpExtVEEntry,_O:ciVplsBgpExtVEId,_U:ciVplsBgpExtVEName,_V:ciVplsBgpExtVEPreference,_X:ciVplsBgpExtVEStorageType,_W:ciVplsBgpExtVERowStatus,'ciVplsBgpExtPwBindTable':ciVplsBgpExtPwBindTable,'ciVplsBgpExtPwBindEntry':ciVplsBgpExtPwBindEntry,_Y:ciVplsBgpExtPwBindLocalVEId,_Z:ciVplsBgpExtPwBindRemoteVEId,'ciscoIetfVplsBgpExtMIBConform':ciscoIetfVplsBgpExtMIBConform,'ciscoIetfVplsBgpExtMIBCompliances':ciscoIetfVplsBgpExtMIBCompliances,'ciscoIetfVplsBgpExtMIBCompliance':ciscoIetfVplsBgpExtMIBCompliance,'ciscoIetfVplsBgpExtMIBGroups':ciscoIetfVplsBgpExtMIBGroups,_a:ciVplsBgpExtConfigGroup,_b:ciVplsBgpExtRTGroup,_c:ciVplsBgpExtVEGroup,_d:ciVplsBgpExtPwBindGroup})