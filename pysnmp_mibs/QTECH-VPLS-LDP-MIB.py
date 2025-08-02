_J='qtechvplsLdpNotificationGroup'
_I='qtechvplsLdpGroup'
_H='qtechvplsLdpPwIndex'
_G='Unsigned32'
_F='Integer32'
_E='qtechvplsConfigIndex'
_D='QTECH-VPLS-GENERIC-MIB'
_C='read-create'
_B='QTECH-VPLS-LDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAPwCapabilities,IANAPwPsnTypeTC,IANAPwTypeTC=mibBuilder.importSymbols('IANA-PWE3-MIB','IANAPwCapabilities','IANAPwPsnTypeTC','IANAPwTypeTC')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
qtechvplsConfigIndex,qtechvplsPwBindIndex=mibBuilder.importSymbols(_D,_E,'qtechvplsPwBindIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechvplsLdpDraft01MIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,78))
if mibBuilder.loadTexts:qtechvplsLdpDraft01MIB.setRevisions(('2010-04-28 12:00',))
_QtechvplsLdpNotifications_ObjectIdentity=ObjectIdentity
qtechvplsLdpNotifications=_QtechvplsLdpNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,78,0))
_QtechvplsLdpObjects_ObjectIdentity=ObjectIdentity
qtechvplsLdpObjects=_QtechvplsLdpObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,78,1))
_QtechvplsLdpConfigTable_Object=MibTable
qtechvplsLdpConfigTable=_QtechvplsLdpConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,78,1,1))
if mibBuilder.loadTexts:qtechvplsLdpConfigTable.setStatus(_A)
_QtechvplsLdpConfigEntry_Object=MibTableRow
qtechvplsLdpConfigEntry=_QtechvplsLdpConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,78,1,1,1))
qtechvplsLdpConfigEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:qtechvplsLdpConfigEntry.setStatus(_A)
_QtechvplsLdpPwIndex_Type=Unsigned32
_QtechvplsLdpPwIndex_Object=MibTableColumn
qtechvplsLdpPwIndex=_QtechvplsLdpPwIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,78,1,1,1,1),_QtechvplsLdpPwIndex_Type())
qtechvplsLdpPwIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechvplsLdpPwIndex.setStatus(_A)
_QtechvplsLdpPeerAddr_Type=InetAddress
_QtechvplsLdpPeerAddr_Object=MibTableColumn
qtechvplsLdpPeerAddr=_QtechvplsLdpPeerAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,78,1,1,1,2),_QtechvplsLdpPeerAddr_Type())
qtechvplsLdpPeerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsLdpPeerAddr.setStatus(_A)
class _QtechvplsLdpPwId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechvplsLdpPwId_Type.__name__=_G
_QtechvplsLdpPwId_Object=MibTableColumn
qtechvplsLdpPwId=_QtechvplsLdpPwId_Object((1,3,6,1,4,1,27514,1,1,10,2,78,1,1,1,3),_QtechvplsLdpPwId_Type())
qtechvplsLdpPwId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsLdpPwId.setStatus(_A)
class _QtechvplsPwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mesh',1),('spoke',2)))
_QtechvplsPwType_Type.__name__=_F
_QtechvplsPwType_Object=MibTableColumn
qtechvplsPwType=_QtechvplsPwType_Object((1,3,6,1,4,1,27514,1,1,10,2,78,1,1,1,4),_QtechvplsPwType_Type())
qtechvplsPwType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsPwType.setStatus(_A)
_QtechvplsPwEncapType_Type=IANAPwTypeTC
_QtechvplsPwEncapType_Object=MibTableColumn
qtechvplsPwEncapType=_QtechvplsPwEncapType_Object((1,3,6,1,4,1,27514,1,1,10,2,78,1,1,1,5),_QtechvplsPwEncapType_Type())
qtechvplsPwEncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsPwEncapType.setStatus(_A)
_QtechvplsLdpNeighborRowStatus_Type=RowStatus
_QtechvplsLdpNeighborRowStatus_Object=MibTableColumn
qtechvplsLdpNeighborRowStatus=_QtechvplsLdpNeighborRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,78,1,1,1,6),_QtechvplsLdpNeighborRowStatus_Type())
qtechvplsLdpNeighborRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsLdpNeighborRowStatus.setStatus(_A)
_QtechvplsLdpConformance_ObjectIdentity=ObjectIdentity
qtechvplsLdpConformance=_QtechvplsLdpConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,78,2))
_QtechvplsLdpCompliances_ObjectIdentity=ObjectIdentity
qtechvplsLdpCompliances=_QtechvplsLdpCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,78,2,1))
_QtechvplsLdpGroups_ObjectIdentity=ObjectIdentity
qtechvplsLdpGroups=_QtechvplsLdpGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,78,2,2))
qtechvplsLdpModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,78,2,1,1))
qtechvplsLdpModuleFullCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:qtechvplsLdpModuleFullCompliance.setStatus(_A)
qtechvplsLdpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,78,2,1,2))
qtechvplsLdpModuleReadOnlyCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:qtechvplsLdpModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechvplsLdpDraft01MIB':qtechvplsLdpDraft01MIB,'qtechvplsLdpNotifications':qtechvplsLdpNotifications,'qtechvplsLdpObjects':qtechvplsLdpObjects,'qtechvplsLdpConfigTable':qtechvplsLdpConfigTable,'qtechvplsLdpConfigEntry':qtechvplsLdpConfigEntry,_H:qtechvplsLdpPwIndex,'qtechvplsLdpPeerAddr':qtechvplsLdpPeerAddr,'qtechvplsLdpPwId':qtechvplsLdpPwId,'qtechvplsPwType':qtechvplsPwType,'qtechvplsPwEncapType':qtechvplsPwEncapType,'qtechvplsLdpNeighborRowStatus':qtechvplsLdpNeighborRowStatus,'qtechvplsLdpConformance':qtechvplsLdpConformance,'qtechvplsLdpCompliances':qtechvplsLdpCompliances,'qtechvplsLdpModuleFullCompliance':qtechvplsLdpModuleFullCompliance,'qtechvplsLdpModuleReadOnlyCompliance':qtechvplsLdpModuleReadOnlyCompliance,'qtechvplsLdpGroups':qtechvplsLdpGroups})