_T='cvDnisNotificationGroup'
_S='cvDnisGroup'
_R='cvDnisMappingUrlInaccessible'
_Q='cvDnisNodeStatus'
_P='cvDnisNodeModifiable'
_O='cvDnisNodeUrl'
_N='cvDnisMappingStatus'
_M='cvDnisMappingRefresh'
_L='cvDnisNumber'
_K='read-only'
_J='not-accessible'
_I='DnisMapname'
_H='Integer32'
_G='cvDnisMappingUrlAccessError'
_F='cvDnisMappingUrl'
_E='cvDnisMappingName'
_D='DisplayString'
_C='read-create'
_B='CISCO-VOICE-DNIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoVoiceDnisMIB=ModuleIdentity((1,3,6,1,4,1,9,9,219))
class DnisMapname(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class CvE164String(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CvDnisMIBObjects_ObjectIdentity=ObjectIdentity
cvDnisMIBObjects=_CvDnisMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,219,1))
_CvDnisMap_ObjectIdentity=ObjectIdentity
cvDnisMap=_CvDnisMap_ObjectIdentity((1,3,6,1,4,1,9,9,219,1,1))
_CvDnisMappingTable_Object=MibTable
cvDnisMappingTable=_CvDnisMappingTable_Object((1,3,6,1,4,1,9,9,219,1,1,1))
if mibBuilder.loadTexts:cvDnisMappingTable.setStatus(_A)
_CvDnisMappingEntry_Object=MibTableRow
cvDnisMappingEntry=_CvDnisMappingEntry_Object((1,3,6,1,4,1,9,9,219,1,1,1,1))
cvDnisMappingEntry.setIndexNames((1,_B,_E))
if mibBuilder.loadTexts:cvDnisMappingEntry.setStatus(_A)
class _CvDnisMappingName_Type(DnisMapname):subtypeSpec=DnisMapname.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CvDnisMappingName_Type.__name__=_I
_CvDnisMappingName_Object=MibTableColumn
cvDnisMappingName=_CvDnisMappingName_Object((1,3,6,1,4,1,9,9,219,1,1,1,1,1),_CvDnisMappingName_Type())
cvDnisMappingName.setMaxAccess(_J)
if mibBuilder.loadTexts:cvDnisMappingName.setStatus(_A)
class _CvDnisMappingUrl_Type(DisplayString):defaultValue=OctetString('')
_CvDnisMappingUrl_Type.__name__=_D
_CvDnisMappingUrl_Object=MibTableColumn
cvDnisMappingUrl=_CvDnisMappingUrl_Object((1,3,6,1,4,1,9,9,219,1,1,1,1,2),_CvDnisMappingUrl_Type())
cvDnisMappingUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:cvDnisMappingUrl.setStatus(_A)
class _CvDnisMappingRefresh_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('refresh',2)))
_CvDnisMappingRefresh_Type.__name__=_H
_CvDnisMappingRefresh_Object=MibTableColumn
cvDnisMappingRefresh=_CvDnisMappingRefresh_Object((1,3,6,1,4,1,9,9,219,1,1,1,1,3),_CvDnisMappingRefresh_Type())
cvDnisMappingRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cvDnisMappingRefresh.setStatus(_A)
class _CvDnisMappingUrlAccessError_Type(DisplayString):defaultValue=OctetString('')
_CvDnisMappingUrlAccessError_Type.__name__=_D
_CvDnisMappingUrlAccessError_Object=MibTableColumn
cvDnisMappingUrlAccessError=_CvDnisMappingUrlAccessError_Object((1,3,6,1,4,1,9,9,219,1,1,1,1,4),_CvDnisMappingUrlAccessError_Type())
cvDnisMappingUrlAccessError.setMaxAccess(_K)
if mibBuilder.loadTexts:cvDnisMappingUrlAccessError.setStatus(_A)
_CvDnisMappingStatus_Type=RowStatus
_CvDnisMappingStatus_Object=MibTableColumn
cvDnisMappingStatus=_CvDnisMappingStatus_Object((1,3,6,1,4,1,9,9,219,1,1,1,1,5),_CvDnisMappingStatus_Type())
cvDnisMappingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvDnisMappingStatus.setStatus(_A)
_CvDnisNodeTable_Object=MibTable
cvDnisNodeTable=_CvDnisNodeTable_Object((1,3,6,1,4,1,9,9,219,1,1,2))
if mibBuilder.loadTexts:cvDnisNodeTable.setStatus(_A)
_CvDnisNodeEntry_Object=MibTableRow
cvDnisNodeEntry=_CvDnisNodeEntry_Object((1,3,6,1,4,1,9,9,219,1,1,2,1))
cvDnisNodeEntry.setIndexNames((0,_B,_E),(1,_B,_L))
if mibBuilder.loadTexts:cvDnisNodeEntry.setStatus(_A)
_CvDnisNumber_Type=CvE164String
_CvDnisNumber_Object=MibTableColumn
cvDnisNumber=_CvDnisNumber_Object((1,3,6,1,4,1,9,9,219,1,1,2,1,1),_CvDnisNumber_Type())
cvDnisNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:cvDnisNumber.setStatus(_A)
class _CvDnisNodeUrl_Type(DisplayString):defaultValue=OctetString('')
_CvDnisNodeUrl_Type.__name__=_D
_CvDnisNodeUrl_Object=MibTableColumn
cvDnisNodeUrl=_CvDnisNodeUrl_Object((1,3,6,1,4,1,9,9,219,1,1,2,1,2),_CvDnisNodeUrl_Type())
cvDnisNodeUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:cvDnisNodeUrl.setStatus(_A)
_CvDnisNodeModifiable_Type=TruthValue
_CvDnisNodeModifiable_Object=MibTableColumn
cvDnisNodeModifiable=_CvDnisNodeModifiable_Object((1,3,6,1,4,1,9,9,219,1,1,2,1,3),_CvDnisNodeModifiable_Type())
cvDnisNodeModifiable.setMaxAccess(_K)
if mibBuilder.loadTexts:cvDnisNodeModifiable.setStatus(_A)
_CvDnisNodeStatus_Type=RowStatus
_CvDnisNodeStatus_Object=MibTableColumn
cvDnisNodeStatus=_CvDnisNodeStatus_Object((1,3,6,1,4,1,9,9,219,1,1,2,1,4),_CvDnisNodeStatus_Type())
cvDnisNodeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvDnisNodeStatus.setStatus(_A)
_CvDnisMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cvDnisMIBNotificationPrefix=_CvDnisMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,219,2))
_CvDnisMIBNotifications_ObjectIdentity=ObjectIdentity
cvDnisMIBNotifications=_CvDnisMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,219,2,0))
_CvDnisMIBConformance_ObjectIdentity=ObjectIdentity
cvDnisMIBConformance=_CvDnisMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,219,3))
_CvDnisMIBCompliances_ObjectIdentity=ObjectIdentity
cvDnisMIBCompliances=_CvDnisMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,219,3,1))
_CvDnisMIBGroups_ObjectIdentity=ObjectIdentity
cvDnisMIBGroups=_CvDnisMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,219,3,2))
cvDnisGroup=ObjectGroup((1,3,6,1,4,1,9,9,219,3,2,1))
cvDnisGroup.setObjects(*((_B,_F),(_B,_M),(_B,_G),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cvDnisGroup.setStatus(_A)
cvDnisMappingUrlInaccessible=NotificationType((1,3,6,1,4,1,9,9,219,2,0,1))
cvDnisMappingUrlInaccessible.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:cvDnisMappingUrlInaccessible.setStatus(_A)
cvDnisNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,219,3,2,2))
cvDnisNotificationGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:cvDnisNotificationGroup.setStatus(_A)
cvDnisMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,219,3,1,1))
cvDnisMIBCompliance.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cvDnisMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_I:DnisMapname,'CvE164String':CvE164String,'ciscoVoiceDnisMIB':ciscoVoiceDnisMIB,'cvDnisMIBObjects':cvDnisMIBObjects,'cvDnisMap':cvDnisMap,'cvDnisMappingTable':cvDnisMappingTable,'cvDnisMappingEntry':cvDnisMappingEntry,_E:cvDnisMappingName,_F:cvDnisMappingUrl,_M:cvDnisMappingRefresh,_G:cvDnisMappingUrlAccessError,_N:cvDnisMappingStatus,'cvDnisNodeTable':cvDnisNodeTable,'cvDnisNodeEntry':cvDnisNodeEntry,_L:cvDnisNumber,_O:cvDnisNodeUrl,_P:cvDnisNodeModifiable,_Q:cvDnisNodeStatus,'cvDnisMIBNotificationPrefix':cvDnisMIBNotificationPrefix,'cvDnisMIBNotifications':cvDnisMIBNotifications,_R:cvDnisMappingUrlInaccessible,'cvDnisMIBConformance':cvDnisMIBConformance,'cvDnisMIBCompliances':cvDnisMIBCompliances,'cvDnisMIBCompliance':cvDnisMIBCompliance,'cvDnisMIBGroups':cvDnisMIBGroups,_S:cvDnisGroup,_T:cvDnisNotificationGroup})