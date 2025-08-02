_i='assocRFC2788Group'
_h='assocRFC2248Group'
_g='assocRFC1565Group'
_f='applDirectoryName'
_e='assocIndex'
_d='not-accessible'
_c='applRFC2788Group'
_b='applRFC2248Group'
_a='applRFC1565Group'
_Z='applURL'
_Y='applDescription'
_X='applIndex'
_W='deprecated'
_V='applFailedOutboundAssociations'
_U='applRejectedInboundAssociations'
_T='applLastOutboundActivity'
_S='applLastInboundActivity'
_R='applAccumulatedOutboundAssociations'
_Q='applAccumulatedInboundAssociations'
_P='applOutboundAssociations'
_O='applInboundAssociations'
_N='applLastChange'
_M='applOperStatus'
_L='applUptime'
_K='applVersion'
_J='applName'
_I='obsolete'
_H='assocDuration'
_G='assocApplicationType'
_F='assocApplicationProtocol'
_E='assocRemoteApplication'
_D='Integer32'
_C='read-only'
_B='current'
_A='NETWORK-SERVICES-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
application=ModuleIdentity((1,3,6,1,2,1,27))
if mibBuilder.loadTexts:application.setRevisions(('2000-03-03 00:00','1999-05-12 00:00','1997-08-17 00:00','1993-11-28 00:00'))
class DistinguishedName(TextualConvention,OctetString):status=_B;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class URLString(TextualConvention,OctetString):status=_B;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApplTable_Object=MibTable
applTable=_ApplTable_Object((1,3,6,1,2,1,27,1))
if mibBuilder.loadTexts:applTable.setStatus(_B)
_ApplEntry_Object=MibTableRow
applEntry=_ApplEntry_Object((1,3,6,1,2,1,27,1,1))
applEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:applEntry.setStatus(_B)
class _ApplIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApplIndex_Type.__name__=_D
_ApplIndex_Object=MibTableColumn
applIndex=_ApplIndex_Object((1,3,6,1,2,1,27,1,1,1),_ApplIndex_Type())
applIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:applIndex.setStatus(_B)
_ApplName_Type=SnmpAdminString
_ApplName_Object=MibTableColumn
applName=_ApplName_Object((1,3,6,1,2,1,27,1,1,2),_ApplName_Type())
applName.setMaxAccess(_C)
if mibBuilder.loadTexts:applName.setStatus(_B)
_ApplDirectoryName_Type=DistinguishedName
_ApplDirectoryName_Object=MibTableColumn
applDirectoryName=_ApplDirectoryName_Object((1,3,6,1,2,1,27,1,1,3),_ApplDirectoryName_Type())
applDirectoryName.setMaxAccess(_C)
if mibBuilder.loadTexts:applDirectoryName.setStatus(_B)
_ApplVersion_Type=SnmpAdminString
_ApplVersion_Object=MibTableColumn
applVersion=_ApplVersion_Object((1,3,6,1,2,1,27,1,1,4),_ApplVersion_Type())
applVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:applVersion.setStatus(_B)
_ApplUptime_Type=TimeStamp
_ApplUptime_Object=MibTableColumn
applUptime=_ApplUptime_Object((1,3,6,1,2,1,27,1,1,5),_ApplUptime_Type())
applUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:applUptime.setStatus(_B)
class _ApplOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('up',1),('down',2),('halted',3),('congested',4),('restarting',5),('quiescing',6)))
_ApplOperStatus_Type.__name__=_D
_ApplOperStatus_Object=MibTableColumn
applOperStatus=_ApplOperStatus_Object((1,3,6,1,2,1,27,1,1,6),_ApplOperStatus_Type())
applOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:applOperStatus.setStatus(_B)
_ApplLastChange_Type=TimeStamp
_ApplLastChange_Object=MibTableColumn
applLastChange=_ApplLastChange_Object((1,3,6,1,2,1,27,1,1,7),_ApplLastChange_Type())
applLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:applLastChange.setStatus(_B)
_ApplInboundAssociations_Type=Gauge32
_ApplInboundAssociations_Object=MibTableColumn
applInboundAssociations=_ApplInboundAssociations_Object((1,3,6,1,2,1,27,1,1,8),_ApplInboundAssociations_Type())
applInboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:applInboundAssociations.setStatus(_B)
_ApplOutboundAssociations_Type=Gauge32
_ApplOutboundAssociations_Object=MibTableColumn
applOutboundAssociations=_ApplOutboundAssociations_Object((1,3,6,1,2,1,27,1,1,9),_ApplOutboundAssociations_Type())
applOutboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:applOutboundAssociations.setStatus(_B)
_ApplAccumulatedInboundAssociations_Type=Counter32
_ApplAccumulatedInboundAssociations_Object=MibTableColumn
applAccumulatedInboundAssociations=_ApplAccumulatedInboundAssociations_Object((1,3,6,1,2,1,27,1,1,10),_ApplAccumulatedInboundAssociations_Type())
applAccumulatedInboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:applAccumulatedInboundAssociations.setStatus(_B)
_ApplAccumulatedOutboundAssociations_Type=Counter32
_ApplAccumulatedOutboundAssociations_Object=MibTableColumn
applAccumulatedOutboundAssociations=_ApplAccumulatedOutboundAssociations_Object((1,3,6,1,2,1,27,1,1,11),_ApplAccumulatedOutboundAssociations_Type())
applAccumulatedOutboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:applAccumulatedOutboundAssociations.setStatus(_B)
_ApplLastInboundActivity_Type=TimeStamp
_ApplLastInboundActivity_Object=MibTableColumn
applLastInboundActivity=_ApplLastInboundActivity_Object((1,3,6,1,2,1,27,1,1,12),_ApplLastInboundActivity_Type())
applLastInboundActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:applLastInboundActivity.setStatus(_B)
_ApplLastOutboundActivity_Type=TimeStamp
_ApplLastOutboundActivity_Object=MibTableColumn
applLastOutboundActivity=_ApplLastOutboundActivity_Object((1,3,6,1,2,1,27,1,1,13),_ApplLastOutboundActivity_Type())
applLastOutboundActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:applLastOutboundActivity.setStatus(_B)
_ApplRejectedInboundAssociations_Type=Counter32
_ApplRejectedInboundAssociations_Object=MibTableColumn
applRejectedInboundAssociations=_ApplRejectedInboundAssociations_Object((1,3,6,1,2,1,27,1,1,14),_ApplRejectedInboundAssociations_Type())
applRejectedInboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:applRejectedInboundAssociations.setStatus(_B)
_ApplFailedOutboundAssociations_Type=Counter32
_ApplFailedOutboundAssociations_Object=MibTableColumn
applFailedOutboundAssociations=_ApplFailedOutboundAssociations_Object((1,3,6,1,2,1,27,1,1,15),_ApplFailedOutboundAssociations_Type())
applFailedOutboundAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:applFailedOutboundAssociations.setStatus(_B)
_ApplDescription_Type=SnmpAdminString
_ApplDescription_Object=MibTableColumn
applDescription=_ApplDescription_Object((1,3,6,1,2,1,27,1,1,16),_ApplDescription_Type())
applDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:applDescription.setStatus(_B)
_ApplURL_Type=URLString
_ApplURL_Object=MibTableColumn
applURL=_ApplURL_Object((1,3,6,1,2,1,27,1,1,17),_ApplURL_Type())
applURL.setMaxAccess(_C)
if mibBuilder.loadTexts:applURL.setStatus(_B)
_AssocTable_Object=MibTable
assocTable=_AssocTable_Object((1,3,6,1,2,1,27,2))
if mibBuilder.loadTexts:assocTable.setStatus(_B)
_AssocEntry_Object=MibTableRow
assocEntry=_AssocEntry_Object((1,3,6,1,2,1,27,2,1))
assocEntry.setIndexNames((0,_A,_X),(0,_A,_e))
if mibBuilder.loadTexts:assocEntry.setStatus(_B)
class _AssocIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AssocIndex_Type.__name__=_D
_AssocIndex_Object=MibTableColumn
assocIndex=_AssocIndex_Object((1,3,6,1,2,1,27,2,1,1),_AssocIndex_Type())
assocIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:assocIndex.setStatus(_B)
_AssocRemoteApplication_Type=SnmpAdminString
_AssocRemoteApplication_Object=MibTableColumn
assocRemoteApplication=_AssocRemoteApplication_Object((1,3,6,1,2,1,27,2,1,2),_AssocRemoteApplication_Type())
assocRemoteApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:assocRemoteApplication.setStatus(_B)
_AssocApplicationProtocol_Type=ObjectIdentifier
_AssocApplicationProtocol_Object=MibTableColumn
assocApplicationProtocol=_AssocApplicationProtocol_Object((1,3,6,1,2,1,27,2,1,3),_AssocApplicationProtocol_Type())
assocApplicationProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:assocApplicationProtocol.setStatus(_B)
class _AssocApplicationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('uainitiator',1),('uaresponder',2),('peerinitiator',3),('peerresponder',4)))
_AssocApplicationType_Type.__name__=_D
_AssocApplicationType_Object=MibTableColumn
assocApplicationType=_AssocApplicationType_Object((1,3,6,1,2,1,27,2,1,4),_AssocApplicationType_Type())
assocApplicationType.setMaxAccess(_C)
if mibBuilder.loadTexts:assocApplicationType.setStatus(_B)
_AssocDuration_Type=TimeStamp
_AssocDuration_Object=MibTableColumn
assocDuration=_AssocDuration_Object((1,3,6,1,2,1,27,2,1,5),_AssocDuration_Type())
assocDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:assocDuration.setStatus(_B)
_ApplConformance_ObjectIdentity=ObjectIdentity
applConformance=_ApplConformance_ObjectIdentity((1,3,6,1,2,1,27,3))
_ApplGroups_ObjectIdentity=ObjectIdentity
applGroups=_ApplGroups_ObjectIdentity((1,3,6,1,2,1,27,3,1))
_ApplCompliances_ObjectIdentity=ObjectIdentity
applCompliances=_ApplCompliances_ObjectIdentity((1,3,6,1,2,1,27,3,2))
_ApplTCPProtoID_ObjectIdentity=ObjectIdentity
applTCPProtoID=_ApplTCPProtoID_ObjectIdentity((1,3,6,1,2,1,27,4))
_ApplUDPProtoID_ObjectIdentity=ObjectIdentity
applUDPProtoID=_ApplUDPProtoID_ObjectIdentity((1,3,6,1,2,1,27,5))
assocRFC1565Group=ObjectGroup((1,3,6,1,2,1,27,3,1,2))
assocRFC1565Group.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:assocRFC1565Group.setStatus(_I)
applRFC2248Group=ObjectGroup((1,3,6,1,2,1,27,3,1,3))
applRFC2248Group.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:applRFC2248Group.setStatus(_W)
assocRFC2248Group=ObjectGroup((1,3,6,1,2,1,27,3,1,4))
assocRFC2248Group.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:assocRFC2248Group.setStatus(_W)
applRFC2788Group=ObjectGroup((1,3,6,1,2,1,27,3,1,5))
applRFC2788Group.setObjects(*((_A,_J),(_A,_f),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:applRFC2788Group.setStatus(_B)
assocRFC2788Group=ObjectGroup((1,3,6,1,2,1,27,3,1,6))
assocRFC2788Group.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:assocRFC2788Group.setStatus(_B)
applRFC1565Group=ObjectGroup((1,3,6,1,2,1,27,3,1,7))
applRFC1565Group.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:applRFC1565Group.setStatus(_I)
applCompliance=ModuleCompliance((1,3,6,1,2,1,27,3,2,1))
applCompliance.setObjects((_A,_a))
if mibBuilder.loadTexts:applCompliance.setStatus(_I)
assocCompliance=ModuleCompliance((1,3,6,1,2,1,27,3,2,2))
assocCompliance.setObjects(*((_A,_a),(_A,_g)))
if mibBuilder.loadTexts:assocCompliance.setStatus(_I)
applRFC2248Compliance=ModuleCompliance((1,3,6,1,2,1,27,3,2,3))
applRFC2248Compliance.setObjects((_A,_b))
if mibBuilder.loadTexts:applRFC2248Compliance.setStatus(_W)
assocRFC2248Compliance=ModuleCompliance((1,3,6,1,2,1,27,3,2,4))
assocRFC2248Compliance.setObjects(*((_A,_b),(_A,_h)))
if mibBuilder.loadTexts:assocRFC2248Compliance.setStatus(_W)
applRFC2788Compliance=ModuleCompliance((1,3,6,1,2,1,27,3,2,5))
applRFC2788Compliance.setObjects((_A,_c))
if mibBuilder.loadTexts:applRFC2788Compliance.setStatus(_B)
assocRFC2788Compliance=ModuleCompliance((1,3,6,1,2,1,27,3,2,6))
assocRFC2788Compliance.setObjects(*((_A,_c),(_A,_i)))
if mibBuilder.loadTexts:assocRFC2788Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DistinguishedName':DistinguishedName,'URLString':URLString,'application':application,'applTable':applTable,'applEntry':applEntry,_X:applIndex,_J:applName,_f:applDirectoryName,_K:applVersion,_L:applUptime,_M:applOperStatus,_N:applLastChange,_O:applInboundAssociations,_P:applOutboundAssociations,_Q:applAccumulatedInboundAssociations,_R:applAccumulatedOutboundAssociations,_S:applLastInboundActivity,_T:applLastOutboundActivity,_U:applRejectedInboundAssociations,_V:applFailedOutboundAssociations,_Y:applDescription,_Z:applURL,'assocTable':assocTable,'assocEntry':assocEntry,_e:assocIndex,_E:assocRemoteApplication,_F:assocApplicationProtocol,_G:assocApplicationType,_H:assocDuration,'applConformance':applConformance,'applGroups':applGroups,_g:assocRFC1565Group,_b:applRFC2248Group,_h:assocRFC2248Group,_c:applRFC2788Group,_i:assocRFC2788Group,_a:applRFC1565Group,'applCompliances':applCompliances,'applCompliance':applCompliance,'assocCompliance':assocCompliance,'applRFC2248Compliance':applRFC2248Compliance,'assocRFC2248Compliance':assocRFC2248Compliance,'applRFC2788Compliance':applRFC2788Compliance,'assocRFC2788Compliance':assocRFC2788Compliance,'applTCPProtoID':applTCPProtoID,'applUDPProtoID':applUDPProtoID})