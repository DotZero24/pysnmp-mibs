_H='nsServiceGrpMemberIndex'
_G='nsServiceGroupIndex'
_F='nsServiceIndex'
_E='NETSCREEN-SERVICE-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenService,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenService')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenServiceMibModule=ModuleIdentity((1,3,6,1,4,1,3224,13,0))
if mibBuilder.loadTexts:netscreenServiceMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2001-09-28 00:00','2001-05-14 00:00'))
_NsServiceTable_Object=MibTable
nsServiceTable=_NsServiceTable_Object((1,3,6,1,4,1,3224,13,1))
if mibBuilder.loadTexts:nsServiceTable.setStatus(_A)
_NsServiceEntry_Object=MibTableRow
nsServiceEntry=_NsServiceEntry_Object((1,3,6,1,4,1,3224,13,1,1))
nsServiceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsServiceEntry.setStatus(_A)
class _NsServiceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsServiceIndex_Type.__name__=_C
_NsServiceIndex_Object=MibTableColumn
nsServiceIndex=_NsServiceIndex_Object((1,3,6,1,4,1,3224,13,1,1,1),_NsServiceIndex_Type())
nsServiceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceIndex.setStatus(_A)
class _NsServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsServiceName_Type.__name__=_D
_NsServiceName_Object=MibTableColumn
nsServiceName=_NsServiceName_Object((1,3,6,1,4,1,3224,13,1,1,2),_NsServiceName_Type())
nsServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceName.setStatus(_A)
class _NsServiceCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('remote',1),('email',2),('infoseek',3),('security',4),('other',5)))
_NsServiceCategory_Type.__name__=_C
_NsServiceCategory_Object=MibTableColumn
nsServiceCategory=_NsServiceCategory_Object((1,3,6,1,4,1,3224,13,1,1,3),_NsServiceCategory_Type())
nsServiceCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceCategory.setStatus(_A)
class _NsServiceTransProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,6,8,9,17,46,47,89)));namedValues=NamedValues(*(('other',0),('icmp',1),('tcp',6),('egp',8),('igp',9),('udp',17),('rsvp',46),('gre',47),('ospf',89)))
_NsServiceTransProto_Type.__name__=_C
_NsServiceTransProto_Object=MibTableColumn
nsServiceTransProto=_NsServiceTransProto_Object((1,3,6,1,4,1,3224,13,1,1,4),_NsServiceTransProto_Type())
nsServiceTransProto.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceTransProto.setStatus(_A)
_NsServiceSrcPortLow_Type=Integer32
_NsServiceSrcPortLow_Object=MibTableColumn
nsServiceSrcPortLow=_NsServiceSrcPortLow_Object((1,3,6,1,4,1,3224,13,1,1,5),_NsServiceSrcPortLow_Type())
nsServiceSrcPortLow.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceSrcPortLow.setStatus(_A)
_NsServiceSrcPortHigh_Type=Integer32
_NsServiceSrcPortHigh_Object=MibTableColumn
nsServiceSrcPortHigh=_NsServiceSrcPortHigh_Object((1,3,6,1,4,1,3224,13,1,1,6),_NsServiceSrcPortHigh_Type())
nsServiceSrcPortHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceSrcPortHigh.setStatus(_A)
_NsServiceDstPortLow_Type=Integer32
_NsServiceDstPortLow_Object=MibTableColumn
nsServiceDstPortLow=_NsServiceDstPortLow_Object((1,3,6,1,4,1,3224,13,1,1,7),_NsServiceDstPortLow_Type())
nsServiceDstPortLow.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceDstPortLow.setStatus(_A)
_NsServiceDstPortHigh_Type=Integer32
_NsServiceDstPortHigh_Object=MibTableColumn
nsServiceDstPortHigh=_NsServiceDstPortHigh_Object((1,3,6,1,4,1,3224,13,1,1,8),_NsServiceDstPortHigh_Type())
nsServiceDstPortHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceDstPortHigh.setStatus(_A)
class _NsServiceFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('pre-define',0),('usr-define',1)))
_NsServiceFlag_Type.__name__=_C
_NsServiceFlag_Object=MibTableColumn
nsServiceFlag=_NsServiceFlag_Object((1,3,6,1,4,1,3224,13,1,1,9),_NsServiceFlag_Type())
nsServiceFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceFlag.setStatus(_A)
_NsServiceVsys_Type=Integer32
_NsServiceVsys_Object=MibTableColumn
nsServiceVsys=_NsServiceVsys_Object((1,3,6,1,4,1,3224,13,1,1,10),_NsServiceVsys_Type())
nsServiceVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceVsys.setStatus(_A)
_NsServiceGroupTable_Object=MibTable
nsServiceGroupTable=_NsServiceGroupTable_Object((1,3,6,1,4,1,3224,13,2))
if mibBuilder.loadTexts:nsServiceGroupTable.setStatus(_A)
_NsServiceGroupEntry_Object=MibTableRow
nsServiceGroupEntry=_NsServiceGroupEntry_Object((1,3,6,1,4,1,3224,13,2,1))
nsServiceGroupEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:nsServiceGroupEntry.setStatus(_A)
class _NsServiceGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsServiceGroupIndex_Type.__name__=_C
_NsServiceGroupIndex_Object=MibTableColumn
nsServiceGroupIndex=_NsServiceGroupIndex_Object((1,3,6,1,4,1,3224,13,2,1,1),_NsServiceGroupIndex_Type())
nsServiceGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceGroupIndex.setStatus(_A)
class _NsServiceGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsServiceGroupName_Type.__name__=_D
_NsServiceGroupName_Object=MibTableColumn
nsServiceGroupName=_NsServiceGroupName_Object((1,3,6,1,4,1,3224,13,2,1,2),_NsServiceGroupName_Type())
nsServiceGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceGroupName.setStatus(_A)
_NsServiceGroupMember_Type=Integer32
_NsServiceGroupMember_Object=MibTableColumn
nsServiceGroupMember=_NsServiceGroupMember_Object((1,3,6,1,4,1,3224,13,2,1,3),_NsServiceGroupMember_Type())
nsServiceGroupMember.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceGroupMember.setStatus(_A)
class _NsServiceGroupComment_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsServiceGroupComment_Type.__name__=_D
_NsServiceGroupComment_Object=MibTableColumn
nsServiceGroupComment=_NsServiceGroupComment_Object((1,3,6,1,4,1,3224,13,2,1,4),_NsServiceGroupComment_Type())
nsServiceGroupComment.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceGroupComment.setStatus(_A)
_NsServiceGroupVsys_Type=Integer32
_NsServiceGroupVsys_Object=MibTableColumn
nsServiceGroupVsys=_NsServiceGroupVsys_Object((1,3,6,1,4,1,3224,13,2,1,5),_NsServiceGroupVsys_Type())
nsServiceGroupVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceGroupVsys.setStatus(_A)
_NsServiceGrpMemberTable_Object=MibTable
nsServiceGrpMemberTable=_NsServiceGrpMemberTable_Object((1,3,6,1,4,1,3224,13,3))
if mibBuilder.loadTexts:nsServiceGrpMemberTable.setStatus(_A)
_NsServiceGrpMemberEntry_Object=MibTableRow
nsServiceGrpMemberEntry=_NsServiceGrpMemberEntry_Object((1,3,6,1,4,1,3224,13,3,1))
nsServiceGrpMemberEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:nsServiceGrpMemberEntry.setStatus(_A)
class _NsServiceGrpMemberIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsServiceGrpMemberIndex_Type.__name__=_C
_NsServiceGrpMemberIndex_Object=MibTableColumn
nsServiceGrpMemberIndex=_NsServiceGrpMemberIndex_Object((1,3,6,1,4,1,3224,13,3,1,1),_NsServiceGrpMemberIndex_Type())
nsServiceGrpMemberIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceGrpMemberIndex.setStatus(_A)
class _NsServiceGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsServiceGrpName_Type.__name__=_D
_NsServiceGrpName_Object=MibTableColumn
nsServiceGrpName=_NsServiceGrpName_Object((1,3,6,1,4,1,3224,13,3,1,2),_NsServiceGrpName_Type())
nsServiceGrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceGrpName.setStatus(_A)
class _NsServiceGroupMemberName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsServiceGroupMemberName_Type.__name__=_D
_NsServiceGroupMemberName_Object=MibTableColumn
nsServiceGroupMemberName=_NsServiceGroupMemberName_Object((1,3,6,1,4,1,3224,13,3,1,3),_NsServiceGroupMemberName_Type())
nsServiceGroupMemberName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceGroupMemberName.setStatus(_A)
_NsServiceGroupMemberVsys_Type=Integer32
_NsServiceGroupMemberVsys_Object=MibTableColumn
nsServiceGroupMemberVsys=_NsServiceGroupMemberVsys_Object((1,3,6,1,4,1,3224,13,3,1,4),_NsServiceGroupMemberVsys_Type())
nsServiceGroupMemberVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsServiceGroupMemberVsys.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenServiceMibModule':netscreenServiceMibModule,'nsServiceTable':nsServiceTable,'nsServiceEntry':nsServiceEntry,_F:nsServiceIndex,'nsServiceName':nsServiceName,'nsServiceCategory':nsServiceCategory,'nsServiceTransProto':nsServiceTransProto,'nsServiceSrcPortLow':nsServiceSrcPortLow,'nsServiceSrcPortHigh':nsServiceSrcPortHigh,'nsServiceDstPortLow':nsServiceDstPortLow,'nsServiceDstPortHigh':nsServiceDstPortHigh,'nsServiceFlag':nsServiceFlag,'nsServiceVsys':nsServiceVsys,'nsServiceGroupTable':nsServiceGroupTable,'nsServiceGroupEntry':nsServiceGroupEntry,_G:nsServiceGroupIndex,'nsServiceGroupName':nsServiceGroupName,'nsServiceGroupMember':nsServiceGroupMember,'nsServiceGroupComment':nsServiceGroupComment,'nsServiceGroupVsys':nsServiceGroupVsys,'nsServiceGrpMemberTable':nsServiceGrpMemberTable,'nsServiceGrpMemberEntry':nsServiceGrpMemberEntry,_H:nsServiceGrpMemberIndex,'nsServiceGrpName':nsServiceGrpName,'nsServiceGroupMemberName':nsServiceGroupMemberName,'nsServiceGroupMemberVsys':nsServiceGroupMemberVsys})