_A9='mediaGatewayEndptRepetitionGroup'
_A8='mediaGatewayControllerGroup1'
_A7='mediaGatewayControllerResolutionGroup'
_A6='mediaGatewayControllerGroup'
_A5='mgEndpointRepetition'
_A4='mgDomainNameRowStatus'
_A3='mgDnsResolutionType'
_A2='mgDomainName'
_A1='mgcDnsResolutionFlag'
_A0='channelAssignment'
_z='mgEndpointRowStatus'
_y='mgEndpointChannelMap'
_x='mgEndpointState'
_w='mgEndpointSpeed'
_v='mgEndpointLineNumber'
_u='mgEndpointName'
_t='mgEndpointCreationPolicy'
_s='mgcDnsResolution'
_r='mgProtocolName'
_q='mgShutdownGraceTime'
_p='mgAdministrativeStateControl'
_o='mgAdministrativeState'
_n='mgName'
_m='mgEndpointExtEntry'
_l='mgDomainNameIndex'
_k='mgcResolutionIndex'
_j='lineNumber'
_i='mgEndpointNumber'
_h='seconds'
_g='inService'
_f='TruthValue'
_e='mediaGatewayControllerGroup2'
_d='mgcResolutionRowStatus'
_c='mgcResolutionPreference'
_b='mgcResolutionCommState'
_a='mgcResolutionIpAddress'
_Z='mgcResolutionName'
_Y='mgcProtocolRowStatus'
_X='mgcCommLossUnassociationTimeout'
_W='mgcUnassociationPolicy'
_V='mgcAssociationStateControl'
_U='mgcAssociationState'
_T='mgcNumber'
_S='mgProtocolNumber'
_R='mediaGatewayControllerResolutionGroup1'
_Q='mediaGatewayDomainNameGroup'
_P='mgcRowStatus'
_O='mgcName'
_N='maxConcurrentMgcs'
_M='Unsigned32'
_L='mediaGatewayLineGroup'
_K='mediaGatewayEndpointGroup'
_J='mediaGatewayGroup'
_I='read-write'
_H='not-accessible'
_G='SnmpAdminString'
_F='read-only'
_E='deprecated'
_D='read-create'
_C='Integer32'
_B='current'
_A='CISCO-WAN-MG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_f)
ciscoWanMgMIB=ModuleIdentity((1,3,6,1,4,1,351,150,10))
if mibBuilder.loadTexts:ciscoWanMgMIB.setRevisions(('2005-05-27 00:00','2004-01-20 00:00','2002-06-14 00:00','2001-05-25 00:00','2000-07-19 15:00','2000-03-27 00:00','1999-11-27 00:00'))
_CiscoWanMgMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanMgMIBObjects=_CiscoWanMgMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,10,1))
_MediaGateway_ObjectIdentity=ObjectIdentity
mediaGateway=_MediaGateway_ObjectIdentity((1,3,6,1,4,1,351,150,10,1,1))
class _MgName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MgName_Type.__name__=_G
_MgName_Object=MibScalar
mgName=_MgName_Object((1,3,6,1,4,1,351,150,10,1,1,1),_MgName_Type())
mgName.setMaxAccess(_I)
if mibBuilder.loadTexts:mgName.setStatus(_B)
class _MgAdministrativeState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),('commandedOutOfService',2),('pendingOutOfService',3)))
_MgAdministrativeState_Type.__name__=_C
_MgAdministrativeState_Object=MibScalar
mgAdministrativeState=_MgAdministrativeState_Object((1,3,6,1,4,1,351,150,10,1,1,2),_MgAdministrativeState_Type())
mgAdministrativeState.setMaxAccess(_F)
if mibBuilder.loadTexts:mgAdministrativeState.setStatus(_B)
class _MgAdministrativeStateControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),('forcefulOutOfService',2),('gracefulOutOfService',3)))
_MgAdministrativeStateControl_Type.__name__=_C
_MgAdministrativeStateControl_Object=MibScalar
mgAdministrativeStateControl=_MgAdministrativeStateControl_Object((1,3,6,1,4,1,351,150,10,1,1,3),_MgAdministrativeStateControl_Type())
mgAdministrativeStateControl.setMaxAccess(_I)
if mibBuilder.loadTexts:mgAdministrativeStateControl.setStatus(_B)
class _MgShutdownGraceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_MgShutdownGraceTime_Type.__name__=_C
_MgShutdownGraceTime_Object=MibScalar
mgShutdownGraceTime=_MgShutdownGraceTime_Object((1,3,6,1,4,1,351,150,10,1,1,4),_MgShutdownGraceTime_Type())
mgShutdownGraceTime.setMaxAccess(_I)
if mibBuilder.loadTexts:mgShutdownGraceTime.setStatus(_B)
if mibBuilder.loadTexts:mgShutdownGraceTime.setUnits(_h)
_MgSupportedProtocolTable_Object=MibTable
mgSupportedProtocolTable=_MgSupportedProtocolTable_Object((1,3,6,1,4,1,351,150,10,1,1,7))
if mibBuilder.loadTexts:mgSupportedProtocolTable.setStatus(_B)
_MgSupportedProtocolEntry_Object=MibTableRow
mgSupportedProtocolEntry=_MgSupportedProtocolEntry_Object((1,3,6,1,4,1,351,150,10,1,1,7,1))
mgSupportedProtocolEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:mgSupportedProtocolEntry.setStatus(_B)
class _MgProtocolNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MgProtocolNumber_Type.__name__=_C
_MgProtocolNumber_Object=MibTableColumn
mgProtocolNumber=_MgProtocolNumber_Object((1,3,6,1,4,1,351,150,10,1,1,7,1,1),_MgProtocolNumber_Type())
mgProtocolNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:mgProtocolNumber.setStatus(_B)
class _MgProtocolName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MgProtocolName_Type.__name__=_G
_MgProtocolName_Object=MibTableColumn
mgProtocolName=_MgProtocolName_Object((1,3,6,1,4,1,351,150,10,1,1,7,1,2),_MgProtocolName_Type())
mgProtocolName.setMaxAccess(_F)
if mibBuilder.loadTexts:mgProtocolName.setStatus(_B)
_MediaGatewayController_ObjectIdentity=ObjectIdentity
mediaGatewayController=_MediaGatewayController_ObjectIdentity((1,3,6,1,4,1,351,150,10,1,2))
_MgcTable_Object=MibTable
mgcTable=_MgcTable_Object((1,3,6,1,4,1,351,150,10,1,2,1))
if mibBuilder.loadTexts:mgcTable.setStatus(_B)
_MgcEntry_Object=MibTableRow
mgcEntry=_MgcEntry_Object((1,3,6,1,4,1,351,150,10,1,2,1,1))
mgcEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:mgcEntry.setStatus(_B)
class _MgcNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MgcNumber_Type.__name__=_C
_MgcNumber_Object=MibTableColumn
mgcNumber=_MgcNumber_Object((1,3,6,1,4,1,351,150,10,1,2,1,1,1),_MgcNumber_Type())
mgcNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:mgcNumber.setStatus(_B)
class _MgcName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MgcName_Type.__name__=_G
_MgcName_Object=MibTableColumn
mgcName=_MgcName_Object((1,3,6,1,4,1,351,150,10,1,2,1,1,2),_MgcName_Type())
mgcName.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcName.setStatus(_B)
class _MgcDnsResolution_Type(TruthValue):defaultValue=2
_MgcDnsResolution_Type.__name__=_f
_MgcDnsResolution_Object=MibTableColumn
mgcDnsResolution=_MgcDnsResolution_Object((1,3,6,1,4,1,351,150,10,1,2,1,1,3),_MgcDnsResolution_Type())
mgcDnsResolution.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcDnsResolution.setStatus(_E)
class _MgcAssociationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mgcUnassociated',1),('mgcAssociated',2),('mgcAssociatedCommLoss',3)))
_MgcAssociationState_Type.__name__=_C
_MgcAssociationState_Object=MibTableColumn
mgcAssociationState=_MgcAssociationState_Object((1,3,6,1,4,1,351,150,10,1,2,1,1,4),_MgcAssociationState_Type())
mgcAssociationState.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcAssociationState.setStatus(_E)
class _MgcAssociationStateControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mgcUnassociate',1),('mgcAssociate',2),('mgcClear',3)))
_MgcAssociationStateControl_Type.__name__=_C
_MgcAssociationStateControl_Object=MibTableColumn
mgcAssociationStateControl=_MgcAssociationStateControl_Object((1,3,6,1,4,1,351,150,10,1,2,1,1,5),_MgcAssociationStateControl_Type())
mgcAssociationStateControl.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcAssociationStateControl.setStatus(_E)
class _MgcUnassociationPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mgcNoAction',1),('mgcRelease',2)))
_MgcUnassociationPolicy_Type.__name__=_C
_MgcUnassociationPolicy_Object=MibTableColumn
mgcUnassociationPolicy=_MgcUnassociationPolicy_Object((1,3,6,1,4,1,351,150,10,1,2,1,1,6),_MgcUnassociationPolicy_Type())
mgcUnassociationPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcUnassociationPolicy.setStatus(_E)
class _MgcCommLossUnassociationTimeout_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_MgcCommLossUnassociationTimeout_Type.__name__=_C
_MgcCommLossUnassociationTimeout_Object=MibTableColumn
mgcCommLossUnassociationTimeout=_MgcCommLossUnassociationTimeout_Object((1,3,6,1,4,1,351,150,10,1,2,1,1,7),_MgcCommLossUnassociationTimeout_Type())
mgcCommLossUnassociationTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcCommLossUnassociationTimeout.setStatus(_E)
if mibBuilder.loadTexts:mgcCommLossUnassociationTimeout.setUnits(_h)
_MgcRowStatus_Type=RowStatus
_MgcRowStatus_Object=MibTableColumn
mgcRowStatus=_MgcRowStatus_Object((1,3,6,1,4,1,351,150,10,1,2,1,1,8),_MgcRowStatus_Type())
mgcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcRowStatus.setStatus(_B)
_MgcProtocolTable_Object=MibTable
mgcProtocolTable=_MgcProtocolTable_Object((1,3,6,1,4,1,351,150,10,1,2,2))
if mibBuilder.loadTexts:mgcProtocolTable.setStatus(_E)
_MgcProtocolEntry_Object=MibTableRow
mgcProtocolEntry=_MgcProtocolEntry_Object((1,3,6,1,4,1,351,150,10,1,2,2,1))
mgcProtocolEntry.setIndexNames((0,_A,_T),(0,_A,_S))
if mibBuilder.loadTexts:mgcProtocolEntry.setStatus(_E)
_MgcProtocolRowStatus_Type=RowStatus
_MgcProtocolRowStatus_Object=MibTableColumn
mgcProtocolRowStatus=_MgcProtocolRowStatus_Object((1,3,6,1,4,1,351,150,10,1,2,2,1,1),_MgcProtocolRowStatus_Type())
mgcProtocolRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcProtocolRowStatus.setStatus(_E)
class _MaxConcurrentMgcs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MaxConcurrentMgcs_Type.__name__=_M
_MaxConcurrentMgcs_Object=MibScalar
maxConcurrentMgcs=_MaxConcurrentMgcs_Object((1,3,6,1,4,1,351,150,10,1,2,3),_MaxConcurrentMgcs_Type())
maxConcurrentMgcs.setMaxAccess(_F)
if mibBuilder.loadTexts:maxConcurrentMgcs.setStatus(_B)
if mibBuilder.loadTexts:maxConcurrentMgcs.setUnits('controllers')
_MediaGatewayEndpoint_ObjectIdentity=ObjectIdentity
mediaGatewayEndpoint=_MediaGatewayEndpoint_ObjectIdentity((1,3,6,1,4,1,351,150,10,1,3))
_MgEndpointTable_Object=MibTable
mgEndpointTable=_MgEndpointTable_Object((1,3,6,1,4,1,351,150,10,1,3,1))
if mibBuilder.loadTexts:mgEndpointTable.setStatus(_B)
_MgEndpointEntry_Object=MibTableRow
mgEndpointEntry=_MgEndpointEntry_Object((1,3,6,1,4,1,351,150,10,1,3,1,1))
mgEndpointEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:mgEndpointEntry.setStatus(_B)
class _MgEndpointNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MgEndpointNumber_Type.__name__=_C
_MgEndpointNumber_Object=MibTableColumn
mgEndpointNumber=_MgEndpointNumber_Object((1,3,6,1,4,1,351,150,10,1,3,1,1,1),_MgEndpointNumber_Type())
mgEndpointNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:mgEndpointNumber.setStatus(_B)
class _MgEndpointLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MgEndpointLineNumber_Type.__name__=_C
_MgEndpointLineNumber_Object=MibTableColumn
mgEndpointLineNumber=_MgEndpointLineNumber_Object((1,3,6,1,4,1,351,150,10,1,3,1,1,2),_MgEndpointLineNumber_Type())
mgEndpointLineNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:mgEndpointLineNumber.setStatus(_B)
_MgEndpointName_Type=SnmpAdminString
_MgEndpointName_Object=MibTableColumn
mgEndpointName=_MgEndpointName_Object((1,3,6,1,4,1,351,150,10,1,3,1,1,3),_MgEndpointName_Type())
mgEndpointName.setMaxAccess(_D)
if mibBuilder.loadTexts:mgEndpointName.setStatus(_B)
class _MgEndpointSpeed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MgEndpointSpeed_Type.__name__=_M
_MgEndpointSpeed_Object=MibTableColumn
mgEndpointSpeed=_MgEndpointSpeed_Object((1,3,6,1,4,1,351,150,10,1,3,1,1,4),_MgEndpointSpeed_Type())
mgEndpointSpeed.setMaxAccess(_F)
if mibBuilder.loadTexts:mgEndpointSpeed.setStatus(_B)
if mibBuilder.loadTexts:mgEndpointSpeed.setUnits('Kbps')
class _MgEndpointState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mgEndpointActive',1),('mgEndpointFailed',2),('mgEndpointDegraded',3)))
_MgEndpointState_Type.__name__=_C
_MgEndpointState_Object=MibTableColumn
mgEndpointState=_MgEndpointState_Object((1,3,6,1,4,1,351,150,10,1,3,1,1,5),_MgEndpointState_Type())
mgEndpointState.setMaxAccess(_F)
if mibBuilder.loadTexts:mgEndpointState.setStatus(_B)
class _MgEndpointChannelMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MgEndpointChannelMap_Type.__name__=_C
_MgEndpointChannelMap_Object=MibTableColumn
mgEndpointChannelMap=_MgEndpointChannelMap_Object((1,3,6,1,4,1,351,150,10,1,3,1,1,6),_MgEndpointChannelMap_Type())
mgEndpointChannelMap.setMaxAccess(_D)
if mibBuilder.loadTexts:mgEndpointChannelMap.setStatus(_B)
_MgEndpointRowStatus_Type=RowStatus
_MgEndpointRowStatus_Object=MibTableColumn
mgEndpointRowStatus=_MgEndpointRowStatus_Object((1,3,6,1,4,1,351,150,10,1,3,1,1,7),_MgEndpointRowStatus_Type())
mgEndpointRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgEndpointRowStatus.setStatus(_B)
class _MgEndpointCreationPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('strictDynamic',2),('static',3)))
_MgEndpointCreationPolicy_Type.__name__=_C
_MgEndpointCreationPolicy_Object=MibScalar
mgEndpointCreationPolicy=_MgEndpointCreationPolicy_Object((1,3,6,1,4,1,351,150,10,1,3,2),_MgEndpointCreationPolicy_Type())
mgEndpointCreationPolicy.setMaxAccess(_I)
if mibBuilder.loadTexts:mgEndpointCreationPolicy.setStatus(_B)
_MgEndpointExtTable_Object=MibTable
mgEndpointExtTable=_MgEndpointExtTable_Object((1,3,6,1,4,1,351,150,10,1,3,3))
if mibBuilder.loadTexts:mgEndpointExtTable.setStatus(_B)
_MgEndpointExtEntry_Object=MibTableRow
mgEndpointExtEntry=_MgEndpointExtEntry_Object((1,3,6,1,4,1,351,150,10,1,3,3,1))
if mibBuilder.loadTexts:mgEndpointExtEntry.setStatus(_B)
class _MgEndpointRepetition_Type(Unsigned32):defaultValue=1
_MgEndpointRepetition_Type.__name__=_M
_MgEndpointRepetition_Object=MibTableColumn
mgEndpointRepetition=_MgEndpointRepetition_Object((1,3,6,1,4,1,351,150,10,1,3,3,1,1),_MgEndpointRepetition_Type())
mgEndpointRepetition.setMaxAccess(_D)
if mibBuilder.loadTexts:mgEndpointRepetition.setStatus(_B)
_MediaGatewayLine_ObjectIdentity=ObjectIdentity
mediaGatewayLine=_MediaGatewayLine_ObjectIdentity((1,3,6,1,4,1,351,150,10,1,4))
_LineAssignmentTable_Object=MibTable
lineAssignmentTable=_LineAssignmentTable_Object((1,3,6,1,4,1,351,150,10,1,4,1))
if mibBuilder.loadTexts:lineAssignmentTable.setStatus(_B)
_LineAssignmentEntry_Object=MibTableRow
lineAssignmentEntry=_LineAssignmentEntry_Object((1,3,6,1,4,1,351,150,10,1,4,1,1))
lineAssignmentEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:lineAssignmentEntry.setStatus(_B)
class _LineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LineNumber_Type.__name__=_C
_LineNumber_Object=MibTableColumn
lineNumber=_LineNumber_Object((1,3,6,1,4,1,351,150,10,1,4,1,1,1),_LineNumber_Type())
lineNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:lineNumber.setStatus(_B)
class _ChannelAssignment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ChannelAssignment_Type.__name__=_C
_ChannelAssignment_Object=MibTableColumn
channelAssignment=_ChannelAssignment_Object((1,3,6,1,4,1,351,150,10,1,4,1,1,2),_ChannelAssignment_Type())
channelAssignment.setMaxAccess(_F)
if mibBuilder.loadTexts:channelAssignment.setStatus(_B)
class _LineName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_LineName_Type.__name__=_G
_LineName_Object=MibTableColumn
lineName=_LineName_Object((1,3,6,1,4,1,351,150,10,1,4,1,1,3),_LineName_Type())
lineName.setMaxAccess(_I)
if mibBuilder.loadTexts:lineName.setStatus(_B)
_MediaGatewayControllerResolution_ObjectIdentity=ObjectIdentity
mediaGatewayControllerResolution=_MediaGatewayControllerResolution_ObjectIdentity((1,3,6,1,4,1,351,150,10,1,5))
_MgcResolutionTable_Object=MibTable
mgcResolutionTable=_MgcResolutionTable_Object((1,3,6,1,4,1,351,150,10,1,5,1))
if mibBuilder.loadTexts:mgcResolutionTable.setStatus(_B)
_MgcResolutionEntry_Object=MibTableRow
mgcResolutionEntry=_MgcResolutionEntry_Object((1,3,6,1,4,1,351,150,10,1,5,1,1))
mgcResolutionEntry.setIndexNames((0,_A,_k))
if mibBuilder.loadTexts:mgcResolutionEntry.setStatus(_B)
class _MgcResolutionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MgcResolutionIndex_Type.__name__=_C
_MgcResolutionIndex_Object=MibTableColumn
mgcResolutionIndex=_MgcResolutionIndex_Object((1,3,6,1,4,1,351,150,10,1,5,1,1,1),_MgcResolutionIndex_Type())
mgcResolutionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mgcResolutionIndex.setStatus(_B)
class _MgcResolutionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MgcResolutionName_Type.__name__=_G
_MgcResolutionName_Object=MibTableColumn
mgcResolutionName=_MgcResolutionName_Object((1,3,6,1,4,1,351,150,10,1,5,1,1,2),_MgcResolutionName_Type())
mgcResolutionName.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcResolutionName.setStatus(_B)
_MgcResolutionIpAddress_Type=IpAddress
_MgcResolutionIpAddress_Object=MibTableColumn
mgcResolutionIpAddress=_MgcResolutionIpAddress_Object((1,3,6,1,4,1,351,150,10,1,5,1,1,3),_MgcResolutionIpAddress_Type())
mgcResolutionIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcResolutionIpAddress.setStatus(_B)
class _MgcResolutionCommState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('csActive',1),('csInactive',2)))
_MgcResolutionCommState_Type.__name__=_C
_MgcResolutionCommState_Object=MibTableColumn
mgcResolutionCommState=_MgcResolutionCommState_Object((1,3,6,1,4,1,351,150,10,1,5,1,1,4),_MgcResolutionCommState_Type())
mgcResolutionCommState.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcResolutionCommState.setStatus(_B)
class _MgcResolutionPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MgcResolutionPreference_Type.__name__=_C
_MgcResolutionPreference_Object=MibTableColumn
mgcResolutionPreference=_MgcResolutionPreference_Object((1,3,6,1,4,1,351,150,10,1,5,1,1,5),_MgcResolutionPreference_Type())
mgcResolutionPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcResolutionPreference.setStatus(_B)
_MgcResolutionRowStatus_Type=RowStatus
_MgcResolutionRowStatus_Object=MibTableColumn
mgcResolutionRowStatus=_MgcResolutionRowStatus_Object((1,3,6,1,4,1,351,150,10,1,5,1,1,6),_MgcResolutionRowStatus_Type())
mgcResolutionRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgcResolutionRowStatus.setStatus(_B)
class _MgcDnsResolutionFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_MgcDnsResolutionFlag_Type.__name__=_C
_MgcDnsResolutionFlag_Object=MibTableColumn
mgcDnsResolutionFlag=_MgcDnsResolutionFlag_Object((1,3,6,1,4,1,351,150,10,1,5,1,1,7),_MgcDnsResolutionFlag_Type())
mgcDnsResolutionFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcDnsResolutionFlag.setStatus(_B)
_MediaGatewayDomainName_ObjectIdentity=ObjectIdentity
mediaGatewayDomainName=_MediaGatewayDomainName_ObjectIdentity((1,3,6,1,4,1,351,150,10,1,6))
_MgDomainNameTable_Object=MibTable
mgDomainNameTable=_MgDomainNameTable_Object((1,3,6,1,4,1,351,150,10,1,6,1))
if mibBuilder.loadTexts:mgDomainNameTable.setStatus(_B)
_MgDomainNameEntry_Object=MibTableRow
mgDomainNameEntry=_MgDomainNameEntry_Object((1,3,6,1,4,1,351,150,10,1,6,1,1))
mgDomainNameEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:mgDomainNameEntry.setStatus(_B)
class _MgDomainNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MgDomainNameIndex_Type.__name__=_C
_MgDomainNameIndex_Object=MibTableColumn
mgDomainNameIndex=_MgDomainNameIndex_Object((1,3,6,1,4,1,351,150,10,1,6,1,1,1),_MgDomainNameIndex_Type())
mgDomainNameIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mgDomainNameIndex.setStatus(_B)
class _MgDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MgDomainName_Type.__name__=_G
_MgDomainName_Object=MibTableColumn
mgDomainName=_MgDomainName_Object((1,3,6,1,4,1,351,150,10,1,6,1,1,2),_MgDomainName_Type())
mgDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:mgDomainName.setStatus(_B)
class _MgDnsResolutionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('internalOnly',1),('externalOnly',2),('internalFirst',3),('externalFirst',4)))
_MgDnsResolutionType_Type.__name__=_C
_MgDnsResolutionType_Object=MibTableColumn
mgDnsResolutionType=_MgDnsResolutionType_Object((1,3,6,1,4,1,351,150,10,1,6,1,1,3),_MgDnsResolutionType_Type())
mgDnsResolutionType.setMaxAccess(_D)
if mibBuilder.loadTexts:mgDnsResolutionType.setStatus(_B)
_MgDomainNameRowStatus_Type=RowStatus
_MgDomainNameRowStatus_Object=MibTableColumn
mgDomainNameRowStatus=_MgDomainNameRowStatus_Object((1,3,6,1,4,1,351,150,10,1,6,1,1,4),_MgDomainNameRowStatus_Type())
mgDomainNameRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgDomainNameRowStatus.setStatus(_B)
_MgMIBConformance_ObjectIdentity=ObjectIdentity
mgMIBConformance=_MgMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,10,3))
_MgMIBCompliances_ObjectIdentity=ObjectIdentity
mgMIBCompliances=_MgMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,10,3,1))
_MgMIBGroups_ObjectIdentity=ObjectIdentity
mgMIBGroups=_MgMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,10,3,2))
mgEndpointEntry.registerAugmentions((_A,_m))
mgEndpointExtEntry.setIndexNames(*mgEndpointEntry.getIndexNames())
mediaGatewayGroup=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,1))
mediaGatewayGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:mediaGatewayGroup.setStatus(_B)
mediaGatewayControllerGroup=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,2))
mediaGatewayControllerGroup.setObjects(*((_A,_N),(_A,_O),(_A,_s),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_P),(_A,_Y)))
if mibBuilder.loadTexts:mediaGatewayControllerGroup.setStatus(_E)
mediaGatewayEndpointGroup=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,3))
mediaGatewayEndpointGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:mediaGatewayEndpointGroup.setStatus(_B)
mediaGatewayLineGroup=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,4))
mediaGatewayLineGroup.setObjects(*((_A,_A0),(_A,'lineName')))
if mibBuilder.loadTexts:mediaGatewayLineGroup.setStatus(_B)
mediaGatewayControllerResolutionGroup=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,5))
mediaGatewayControllerResolutionGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:mediaGatewayControllerResolutionGroup.setStatus(_E)
mediaGatewayControllerGroup1=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,6))
mediaGatewayControllerGroup1.setObjects(*((_A,_N),(_A,_O),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_P),(_A,_Y)))
if mibBuilder.loadTexts:mediaGatewayControllerGroup1.setStatus(_E)
mediaGatewayControllerResolutionGroup1=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,7))
mediaGatewayControllerResolutionGroup1.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_A1)))
if mibBuilder.loadTexts:mediaGatewayControllerResolutionGroup1.setStatus(_B)
mediaGatewayDomainNameGroup=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,8))
mediaGatewayDomainNameGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:mediaGatewayDomainNameGroup.setStatus(_B)
mediaGatewayControllerGroup2=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,9))
mediaGatewayControllerGroup2.setObjects(*((_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:mediaGatewayControllerGroup2.setStatus(_B)
mediaGatewayEndptRepetitionGroup=ObjectGroup((1,3,6,1,4,1,351,150,10,3,2,10))
mediaGatewayEndptRepetitionGroup.setObjects((_A,_A5))
if mibBuilder.loadTexts:mediaGatewayEndptRepetitionGroup.setStatus(_B)
mgMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,10,3,1,1))
mgMIBCompliance.setObjects(*((_A,_J),(_A,_A6),(_A,_K),(_A,_L),(_A,_A7)))
if mibBuilder.loadTexts:mgMIBCompliance.setStatus(_E)
mgMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,351,150,10,3,1,2))
mgMIBCompliance1.setObjects(*((_A,_J),(_A,_A8),(_A,_K),(_A,_L),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:mgMIBCompliance1.setStatus(_E)
mgMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,351,150,10,3,1,3))
mgMIBCompliance2.setObjects(*((_A,_J),(_A,_e),(_A,_K),(_A,_L),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:mgMIBCompliance2.setStatus(_E)
mgMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,351,150,10,3,1,4))
mgMIBCompliance3.setObjects(*((_A,_J),(_A,_e),(_A,_K),(_A,_L),(_A,_Q),(_A,_R),(_A,_A9)))
if mibBuilder.loadTexts:mgMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoWanMgMIB':ciscoWanMgMIB,'ciscoWanMgMIBObjects':ciscoWanMgMIBObjects,'mediaGateway':mediaGateway,_n:mgName,_o:mgAdministrativeState,_p:mgAdministrativeStateControl,_q:mgShutdownGraceTime,'mgSupportedProtocolTable':mgSupportedProtocolTable,'mgSupportedProtocolEntry':mgSupportedProtocolEntry,_S:mgProtocolNumber,_r:mgProtocolName,'mediaGatewayController':mediaGatewayController,'mgcTable':mgcTable,'mgcEntry':mgcEntry,_T:mgcNumber,_O:mgcName,_s:mgcDnsResolution,_U:mgcAssociationState,_V:mgcAssociationStateControl,_W:mgcUnassociationPolicy,_X:mgcCommLossUnassociationTimeout,_P:mgcRowStatus,'mgcProtocolTable':mgcProtocolTable,'mgcProtocolEntry':mgcProtocolEntry,_Y:mgcProtocolRowStatus,_N:maxConcurrentMgcs,'mediaGatewayEndpoint':mediaGatewayEndpoint,'mgEndpointTable':mgEndpointTable,'mgEndpointEntry':mgEndpointEntry,_i:mgEndpointNumber,_v:mgEndpointLineNumber,_u:mgEndpointName,_w:mgEndpointSpeed,_x:mgEndpointState,_y:mgEndpointChannelMap,_z:mgEndpointRowStatus,_t:mgEndpointCreationPolicy,'mgEndpointExtTable':mgEndpointExtTable,_m:mgEndpointExtEntry,_A5:mgEndpointRepetition,'mediaGatewayLine':mediaGatewayLine,'lineAssignmentTable':lineAssignmentTable,'lineAssignmentEntry':lineAssignmentEntry,_j:lineNumber,_A0:channelAssignment,'lineName':lineName,'mediaGatewayControllerResolution':mediaGatewayControllerResolution,'mgcResolutionTable':mgcResolutionTable,'mgcResolutionEntry':mgcResolutionEntry,_k:mgcResolutionIndex,_Z:mgcResolutionName,_a:mgcResolutionIpAddress,_b:mgcResolutionCommState,_c:mgcResolutionPreference,_d:mgcResolutionRowStatus,_A1:mgcDnsResolutionFlag,'mediaGatewayDomainName':mediaGatewayDomainName,'mgDomainNameTable':mgDomainNameTable,'mgDomainNameEntry':mgDomainNameEntry,_l:mgDomainNameIndex,_A2:mgDomainName,_A3:mgDnsResolutionType,_A4:mgDomainNameRowStatus,'mgMIBConformance':mgMIBConformance,'mgMIBCompliances':mgMIBCompliances,'mgMIBCompliance':mgMIBCompliance,'mgMIBCompliance1':mgMIBCompliance1,'mgMIBCompliance2':mgMIBCompliance2,'mgMIBCompliance3':mgMIBCompliance3,'mgMIBGroups':mgMIBGroups,_J:mediaGatewayGroup,_A6:mediaGatewayControllerGroup,_K:mediaGatewayEndpointGroup,_L:mediaGatewayLineGroup,_A7:mediaGatewayControllerResolutionGroup,_A8:mediaGatewayControllerGroup1,_R:mediaGatewayControllerResolutionGroup1,_Q:mediaGatewayDomainNameGroup,_e:mediaGatewayControllerGroup2,_A9:mediaGatewayEndptRepetitionGroup})