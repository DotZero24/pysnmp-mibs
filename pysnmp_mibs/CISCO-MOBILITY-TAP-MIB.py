_Y='ciscoMobilityTapStreamGroupSup1'
_X='cmtapStreamInterceptType'
_W='cmtapStreamLocationInfo'
_V='cmtapStreamLIIdentifier'
_U='cmtapStreamStatus'
_T='cmtapStreamStorageType'
_S='cmtapStreamSubscriberID'
_R='cmtapStreamSubscriberIDType'
_Q='cmtapStreamCalledSubscriberID'
_P='cmtapStreamCalledSubscriberIDType'
_O='cmtapStreamCapabilities'
_N='CmtapLawfulInterceptID'
_M='servedMdn'
_L='TruthValue'
_K='StorageType'
_J='Integer32'
_I='cTap2StreamIndex'
_H='cTap2MediationContentId'
_G='ciscoMobilityTapStreamGroup'
_F='ciscoMobilityTapCapabilityGroup'
_E='CmtapSubscriberIDType'
_D='CISCO-TAP2-MIB'
_C='read-create'
_B='CISCO-MOBILITY-TAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
cTap2MediationContentId,cTap2StreamIndex=mibBuilder.importSymbols(_D,_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_K,'TextualConvention',_L)
ciscoMobilityTapMIB=ModuleIdentity((1,3,6,1,4,1,9,9,672))
if mibBuilder.loadTexts:ciscoMobilityTapMIB.setRevisions(('2010-06-16 00:00','2010-04-15 00:00','2008-08-05 00:00'))
class CmtapLawfulInterceptID(TextualConvention,OctetString):status=_A;displayHint='256a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,256))
class CmtapSubscriberIDType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('msid',2),('imsi',3),('nai',4),('esn',5),(_M,6)))
class CmtapSubscriberID(TextualConvention,OctetString):status=_A;displayHint='256a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,256))
_CiscoMobilityTapMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoMobilityTapMIBNotifs=_CiscoMobilityTapMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,672,0))
_CiscoMobilityTapMIBObjects_ObjectIdentity=ObjectIdentity
ciscoMobilityTapMIBObjects=_CiscoMobilityTapMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,672,1))
_CmtapStreamGroup_ObjectIdentity=ObjectIdentity
cmtapStreamGroup=_CmtapStreamGroup_ObjectIdentity((1,3,6,1,4,1,9,9,672,1,1))
class _CmtapStreamCapabilities_Type(Bits):namedValues=NamedValues(*(('tapEnable',0),('interface',1),('calledSubscriberID',2),('nonvolatileStorage',3),('msid',4),('imsi',5),('nai',6),('esn',7),(_M,8)))
_CmtapStreamCapabilities_Type.__name__='Bits'
_CmtapStreamCapabilities_Object=MibScalar
cmtapStreamCapabilities=_CmtapStreamCapabilities_Object((1,3,6,1,4,1,9,9,672,1,1,1),_CmtapStreamCapabilities_Type())
cmtapStreamCapabilities.setMaxAccess('read-only')
if mibBuilder.loadTexts:cmtapStreamCapabilities.setStatus(_A)
_CmtapStreamTable_Object=MibTable
cmtapStreamTable=_CmtapStreamTable_Object((1,3,6,1,4,1,9,9,672,1,1,2))
if mibBuilder.loadTexts:cmtapStreamTable.setStatus(_A)
_CmtapStreamEntry_Object=MibTableRow
cmtapStreamEntry=_CmtapStreamEntry_Object((1,3,6,1,4,1,9,9,672,1,1,2,1))
cmtapStreamEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:cmtapStreamEntry.setStatus(_A)
class _CmtapStreamCalledSubscriberIDType_Type(CmtapSubscriberIDType):defaultValue=1
_CmtapStreamCalledSubscriberIDType_Type.__name__=_E
_CmtapStreamCalledSubscriberIDType_Object=MibTableColumn
cmtapStreamCalledSubscriberIDType=_CmtapStreamCalledSubscriberIDType_Object((1,3,6,1,4,1,9,9,672,1,1,2,1,1),_CmtapStreamCalledSubscriberIDType_Type())
cmtapStreamCalledSubscriberIDType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmtapStreamCalledSubscriberIDType.setStatus(_A)
_CmtapStreamCalledSubscriberID_Type=CmtapSubscriberID
_CmtapStreamCalledSubscriberID_Object=MibTableColumn
cmtapStreamCalledSubscriberID=_CmtapStreamCalledSubscriberID_Object((1,3,6,1,4,1,9,9,672,1,1,2,1,2),_CmtapStreamCalledSubscriberID_Type())
cmtapStreamCalledSubscriberID.setMaxAccess(_C)
if mibBuilder.loadTexts:cmtapStreamCalledSubscriberID.setStatus(_A)
class _CmtapStreamSubscriberIDType_Type(CmtapSubscriberIDType):defaultValue=1
_CmtapStreamSubscriberIDType_Type.__name__=_E
_CmtapStreamSubscriberIDType_Object=MibTableColumn
cmtapStreamSubscriberIDType=_CmtapStreamSubscriberIDType_Object((1,3,6,1,4,1,9,9,672,1,1,2,1,3),_CmtapStreamSubscriberIDType_Type())
cmtapStreamSubscriberIDType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmtapStreamSubscriberIDType.setStatus(_A)
_CmtapStreamSubscriberID_Type=CmtapSubscriberID
_CmtapStreamSubscriberID_Object=MibTableColumn
cmtapStreamSubscriberID=_CmtapStreamSubscriberID_Object((1,3,6,1,4,1,9,9,672,1,1,2,1,4),_CmtapStreamSubscriberID_Type())
cmtapStreamSubscriberID.setMaxAccess(_C)
if mibBuilder.loadTexts:cmtapStreamSubscriberID.setStatus(_A)
class _CmtapStreamStorageType_Type(StorageType):defaultValue=2
_CmtapStreamStorageType_Type.__name__=_K
_CmtapStreamStorageType_Object=MibTableColumn
cmtapStreamStorageType=_CmtapStreamStorageType_Object((1,3,6,1,4,1,9,9,672,1,1,2,1,5),_CmtapStreamStorageType_Type())
cmtapStreamStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmtapStreamStorageType.setStatus(_A)
_CmtapStreamStatus_Type=RowStatus
_CmtapStreamStatus_Object=MibTableColumn
cmtapStreamStatus=_CmtapStreamStatus_Object((1,3,6,1,4,1,9,9,672,1,1,2,1,6),_CmtapStreamStatus_Type())
cmtapStreamStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmtapStreamStatus.setStatus(_A)
class _CmtapStreamLIIdentifier_Type(CmtapLawfulInterceptID):defaultValue=OctetString('not set')
_CmtapStreamLIIdentifier_Type.__name__=_N
_CmtapStreamLIIdentifier_Object=MibTableColumn
cmtapStreamLIIdentifier=_CmtapStreamLIIdentifier_Object((1,3,6,1,4,1,9,9,672,1,1,2,1,7),_CmtapStreamLIIdentifier_Type())
cmtapStreamLIIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cmtapStreamLIIdentifier.setStatus(_A)
class _CmtapStreamLocationInfo_Type(TruthValue):defaultValue=1
_CmtapStreamLocationInfo_Type.__name__=_L
_CmtapStreamLocationInfo_Object=MibTableColumn
cmtapStreamLocationInfo=_CmtapStreamLocationInfo_Object((1,3,6,1,4,1,9,9,672,1,1,2,1,8),_CmtapStreamLocationInfo_Type())
cmtapStreamLocationInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cmtapStreamLocationInfo.setStatus(_A)
class _CmtapStreamInterceptType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ccOnly',1),('iriOnly',2),('both',3)))
_CmtapStreamInterceptType_Type.__name__=_J
_CmtapStreamInterceptType_Object=MibTableColumn
cmtapStreamInterceptType=_CmtapStreamInterceptType_Object((1,3,6,1,4,1,9,9,672,1,1,2,1,9),_CmtapStreamInterceptType_Type())
cmtapStreamInterceptType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmtapStreamInterceptType.setStatus(_A)
_CiscoMobilityTapMIBConform_ObjectIdentity=ObjectIdentity
ciscoMobilityTapMIBConform=_CiscoMobilityTapMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,672,2))
_CiscoMobilityTapMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoMobilityTapMIBCompliances=_CiscoMobilityTapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,672,2,1))
_CiscoMobilityTapMIBGroups_ObjectIdentity=ObjectIdentity
ciscoMobilityTapMIBGroups=_CiscoMobilityTapMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,672,2,2))
ciscoMobilityTapCapabilityGroup=ObjectGroup((1,3,6,1,4,1,9,9,672,2,2,1))
ciscoMobilityTapCapabilityGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoMobilityTapCapabilityGroup.setStatus(_A)
ciscoMobilityTapStreamGroup=ObjectGroup((1,3,6,1,4,1,9,9,672,2,2,2))
ciscoMobilityTapStreamGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoMobilityTapStreamGroup.setStatus(_A)
ciscoMobilityTapStreamGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,672,2,2,3))
ciscoMobilityTapStreamGroupSup1.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoMobilityTapStreamGroupSup1.setStatus(_A)
ciscoMobilityTapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,672,2,1,1))
ciscoMobilityTapMIBCompliance.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ciscoMobilityTapMIBCompliance.setStatus('deprecated')
ciscoMobilityTapMIBComplianceRev01=ModuleCompliance((1,3,6,1,4,1,9,9,672,2,1,2))
ciscoMobilityTapMIBComplianceRev01.setObjects(*((_B,_F),(_B,_G),(_B,_Y)))
if mibBuilder.loadTexts:ciscoMobilityTapMIBComplianceRev01.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_N:CmtapLawfulInterceptID,_E:CmtapSubscriberIDType,'CmtapSubscriberID':CmtapSubscriberID,'ciscoMobilityTapMIB':ciscoMobilityTapMIB,'ciscoMobilityTapMIBNotifs':ciscoMobilityTapMIBNotifs,'ciscoMobilityTapMIBObjects':ciscoMobilityTapMIBObjects,'cmtapStreamGroup':cmtapStreamGroup,_O:cmtapStreamCapabilities,'cmtapStreamTable':cmtapStreamTable,'cmtapStreamEntry':cmtapStreamEntry,_P:cmtapStreamCalledSubscriberIDType,_Q:cmtapStreamCalledSubscriberID,_R:cmtapStreamSubscriberIDType,_S:cmtapStreamSubscriberID,_T:cmtapStreamStorageType,_U:cmtapStreamStatus,_V:cmtapStreamLIIdentifier,_W:cmtapStreamLocationInfo,_X:cmtapStreamInterceptType,'ciscoMobilityTapMIBConform':ciscoMobilityTapMIBConform,'ciscoMobilityTapMIBCompliances':ciscoMobilityTapMIBCompliances,'ciscoMobilityTapMIBCompliance':ciscoMobilityTapMIBCompliance,'ciscoMobilityTapMIBComplianceRev01':ciscoMobilityTapMIBComplianceRev01,'ciscoMobilityTapMIBGroups':ciscoMobilityTapMIBGroups,_F:ciscoMobilityTapCapabilityGroup,_G:ciscoMobilityTapStreamGroup,_Y:ciscoMobilityTapStreamGroupSup1})