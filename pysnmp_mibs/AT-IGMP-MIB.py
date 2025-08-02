_J='igmpSnoopHostMAC'
_I='Unsigned32'
_H='igmpSnoopPortNumber'
_G='Integer32'
_F='igmpSnoopGroupAddress'
_E='igmpInterface'
_D='igmpSnoopVID'
_C='AT-IGMP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
igmp=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,139))
if mibBuilder.loadTexts:igmp.setRevisions(('2007-08-08 00:00',))
_IgmpIntInfo_ObjectIdentity=ObjectIdentity
igmpIntInfo=_IgmpIntInfo_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,139,1))
_IgmpInterfaceTable_Object=MibTable
igmpInterfaceTable=_IgmpInterfaceTable_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,1))
if mibBuilder.loadTexts:igmpInterfaceTable.setStatus(_A)
_IgmpInterfaceEntry_Object=MibTableRow
igmpInterfaceEntry=_IgmpInterfaceEntry_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,1,1))
igmpInterfaceEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:igmpInterfaceEntry.setStatus(_A)
_IgmpInterface_Type=Integer32
_IgmpInterface_Object=MibTableColumn
igmpInterface=_IgmpInterface_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,1,1,1),_IgmpInterface_Type())
igmpInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpInterface.setStatus(_A)
_IgmpInterfaceName_Type=DisplayString
_IgmpInterfaceName_Object=MibTableColumn
igmpInterfaceName=_IgmpInterfaceName_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,1,1,2),_IgmpInterfaceName_Type())
igmpInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpInterfaceName.setStatus(_A)
class _IgmpQueryTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IgmpQueryTimeout_Type.__name__=_I
_IgmpQueryTimeout_Object=MibTableColumn
igmpQueryTimeout=_IgmpQueryTimeout_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,1,1,3),_IgmpQueryTimeout_Type())
igmpQueryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpQueryTimeout.setStatus(_A)
class _IgmpProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('upstream',1),('downstream',2)))
_IgmpProxy_Type.__name__=_G
_IgmpProxy_Object=MibTableColumn
igmpProxy=_IgmpProxy_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,1,1,4),_IgmpProxy_Type())
igmpProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpProxy.setStatus(_A)
_IgmpIntStatsTable_Object=MibTable
igmpIntStatsTable=_IgmpIntStatsTable_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2))
if mibBuilder.loadTexts:igmpIntStatsTable.setStatus(_A)
_IgmpIntStatsEntry_Object=MibTableRow
igmpIntStatsEntry=_IgmpIntStatsEntry_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1))
igmpIntStatsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:igmpIntStatsEntry.setStatus(_A)
_IgmpInQuery_Type=Unsigned32
_IgmpInQuery_Object=MibTableColumn
igmpInQuery=_IgmpInQuery_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,1),_IgmpInQuery_Type())
igmpInQuery.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpInQuery.setStatus(_A)
_IgmpInReportV1_Type=Unsigned32
_IgmpInReportV1_Object=MibTableColumn
igmpInReportV1=_IgmpInReportV1_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,2),_IgmpInReportV1_Type())
igmpInReportV1.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpInReportV1.setStatus(_A)
_IgmpInReportV2_Type=Unsigned32
_IgmpInReportV2_Object=MibTableColumn
igmpInReportV2=_IgmpInReportV2_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,3),_IgmpInReportV2_Type())
igmpInReportV2.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpInReportV2.setStatus(_A)
_IgmpInLeave_Type=Unsigned32
_IgmpInLeave_Object=MibTableColumn
igmpInLeave=_IgmpInLeave_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,4),_IgmpInLeave_Type())
igmpInLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpInLeave.setStatus(_A)
_IgmpInTotal_Type=Unsigned32
_IgmpInTotal_Object=MibTableColumn
igmpInTotal=_IgmpInTotal_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,5),_IgmpInTotal_Type())
igmpInTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpInTotal.setStatus(_A)
_IgmpOutQuery_Type=Unsigned32
_IgmpOutQuery_Object=MibTableColumn
igmpOutQuery=_IgmpOutQuery_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,6),_IgmpOutQuery_Type())
igmpOutQuery.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpOutQuery.setStatus(_A)
_IgmpOutTotal_Type=Unsigned32
_IgmpOutTotal_Object=MibTableColumn
igmpOutTotal=_IgmpOutTotal_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,7),_IgmpOutTotal_Type())
igmpOutTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpOutTotal.setStatus(_A)
_IgmpBadQuery_Type=Unsigned32
_IgmpBadQuery_Object=MibTableColumn
igmpBadQuery=_IgmpBadQuery_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,8),_IgmpBadQuery_Type())
igmpBadQuery.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpBadQuery.setStatus(_A)
_IgmpBadReportV1_Type=Unsigned32
_IgmpBadReportV1_Object=MibTableColumn
igmpBadReportV1=_IgmpBadReportV1_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,9),_IgmpBadReportV1_Type())
igmpBadReportV1.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpBadReportV1.setStatus(_A)
_IgmpBadReportV2_Type=Unsigned32
_IgmpBadReportV2_Object=MibTableColumn
igmpBadReportV2=_IgmpBadReportV2_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,10),_IgmpBadReportV2_Type())
igmpBadReportV2.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpBadReportV2.setStatus(_A)
_IgmpBadLeave_Type=Unsigned32
_IgmpBadLeave_Object=MibTableColumn
igmpBadLeave=_IgmpBadLeave_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,11),_IgmpBadLeave_Type())
igmpBadLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpBadLeave.setStatus(_A)
_IgmpBadTotal_Type=Unsigned32
_IgmpBadTotal_Object=MibTableColumn
igmpBadTotal=_IgmpBadTotal_Object((1,3,6,1,4,1,207,8,4,4,4,139,1,2,1,12),_IgmpBadTotal_Type())
igmpBadTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpBadTotal.setStatus(_A)
_IgmpIntMember_ObjectIdentity=ObjectIdentity
igmpIntMember=_IgmpIntMember_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,139,9))
_IgmpIntGroupTable_Object=MibTable
igmpIntGroupTable=_IgmpIntGroupTable_Object((1,3,6,1,4,1,207,8,4,4,4,139,9,1))
if mibBuilder.loadTexts:igmpIntGroupTable.setStatus(_A)
_IgmpIntGroupEntry_Object=MibTableRow
igmpIntGroupEntry=_IgmpIntGroupEntry_Object((1,3,6,1,4,1,207,8,4,4,4,139,9,1,1))
igmpIntGroupEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:igmpIntGroupEntry.setStatus(_A)
_IgmpIntGroupAddress_Type=IpAddress
_IgmpIntGroupAddress_Object=MibTableColumn
igmpIntGroupAddress=_IgmpIntGroupAddress_Object((1,3,6,1,4,1,207,8,4,4,4,139,9,1,1,1),_IgmpIntGroupAddress_Type())
igmpIntGroupAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpIntGroupAddress.setStatus(_A)
_IgmpLastHost_Type=IpAddress
_IgmpLastHost_Object=MibTableColumn
igmpLastHost=_IgmpLastHost_Object((1,3,6,1,4,1,207,8,4,4,4,139,9,1,1,2),_IgmpLastHost_Type())
igmpLastHost.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpLastHost.setStatus(_A)
_IgmpRefreshTime_Type=Unsigned32
_IgmpRefreshTime_Object=MibTableColumn
igmpRefreshTime=_IgmpRefreshTime_Object((1,3,6,1,4,1,207,8,4,4,4,139,9,1,1,3),_IgmpRefreshTime_Type())
igmpRefreshTime.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpRefreshTime.setStatus(_A)
_IgmpSnooping_ObjectIdentity=ObjectIdentity
igmpSnooping=_IgmpSnooping_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,139,10))
_IgmpSnoopAdminInfo_ObjectIdentity=ObjectIdentity
igmpSnoopAdminInfo=_IgmpSnoopAdminInfo_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,139,10,1))
_IgmpSnoopAdminEnabled_Type=TruthValue
_IgmpSnoopAdminEnabled_Object=MibScalar
igmpSnoopAdminEnabled=_IgmpSnoopAdminEnabled_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,1,1),_IgmpSnoopAdminEnabled_Type())
igmpSnoopAdminEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopAdminEnabled.setStatus(_A)
_IgmpSnoopVlanTable_Object=MibTable
igmpSnoopVlanTable=_IgmpSnoopVlanTable_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,2))
if mibBuilder.loadTexts:igmpSnoopVlanTable.setStatus(_A)
_IgmpSnoopVlanEntry_Object=MibTableRow
igmpSnoopVlanEntry=_IgmpSnoopVlanEntry_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,2,1))
igmpSnoopVlanEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:igmpSnoopVlanEntry.setStatus(_A)
_IgmpSnoopVID_Type=Integer32
_IgmpSnoopVID_Object=MibTableColumn
igmpSnoopVID=_IgmpSnoopVID_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,2,1,1),_IgmpSnoopVID_Type())
igmpSnoopVID.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopVID.setStatus(_A)
_IgmpSnoopVlanName_Type=DisplayString
_IgmpSnoopVlanName_Object=MibTableColumn
igmpSnoopVlanName=_IgmpSnoopVlanName_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,2,1,2),_IgmpSnoopVlanName_Type())
igmpSnoopVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopVlanName.setStatus(_A)
class _IgmpSnoopFastLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('single',1),('multi',2)))
_IgmpSnoopFastLeave_Type.__name__=_G
_IgmpSnoopFastLeave_Object=MibTableColumn
igmpSnoopFastLeave=_IgmpSnoopFastLeave_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,2,1,3),_IgmpSnoopFastLeave_Type())
igmpSnoopFastLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopFastLeave.setStatus(_A)
_IgmpSnoopQuerySolicit_Type=TruthValue
_IgmpSnoopQuerySolicit_Object=MibTableColumn
igmpSnoopQuerySolicit=_IgmpSnoopQuerySolicit_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,2,1,4),_IgmpSnoopQuerySolicit_Type())
igmpSnoopQuerySolicit.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopQuerySolicit.setStatus(_A)
_IgmpSnoopStaticRouterPorts_Type=DisplayString
_IgmpSnoopStaticRouterPorts_Object=MibTableColumn
igmpSnoopStaticRouterPorts=_IgmpSnoopStaticRouterPorts_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,2,1,5),_IgmpSnoopStaticRouterPorts_Type())
igmpSnoopStaticRouterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopStaticRouterPorts.setStatus(_A)
_IgmpSnoopGroupTable_Object=MibTable
igmpSnoopGroupTable=_IgmpSnoopGroupTable_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,3))
if mibBuilder.loadTexts:igmpSnoopGroupTable.setStatus(_A)
_IgmpSnoopGroupEntry_Object=MibTableRow
igmpSnoopGroupEntry=_IgmpSnoopGroupEntry_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,3,1))
igmpSnoopGroupEntry.setIndexNames((0,_C,_D),(0,_C,_F))
if mibBuilder.loadTexts:igmpSnoopGroupEntry.setStatus(_A)
_IgmpSnoopGroupAddress_Type=IpAddress
_IgmpSnoopGroupAddress_Object=MibTableColumn
igmpSnoopGroupAddress=_IgmpSnoopGroupAddress_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,3,1,1),_IgmpSnoopGroupAddress_Type())
igmpSnoopGroupAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopGroupAddress.setStatus(_A)
_IgmpSnoopGroupTimer_Type=Unsigned32
_IgmpSnoopGroupTimer_Object=MibTableColumn
igmpSnoopGroupTimer=_IgmpSnoopGroupTimer_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,3,1,2),_IgmpSnoopGroupTimer_Type())
igmpSnoopGroupTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopGroupTimer.setStatus(_A)
_IgmpSnoopPortTable_Object=MibTable
igmpSnoopPortTable=_IgmpSnoopPortTable_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,4))
if mibBuilder.loadTexts:igmpSnoopPortTable.setStatus(_A)
_IgmpSnoopPortEntry_Object=MibTableRow
igmpSnoopPortEntry=_IgmpSnoopPortEntry_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,4,1))
igmpSnoopPortEntry.setIndexNames((0,_C,_D),(0,_C,_F),(0,_C,_H))
if mibBuilder.loadTexts:igmpSnoopPortEntry.setStatus(_A)
_IgmpSnoopPortNumber_Type=Integer32
_IgmpSnoopPortNumber_Object=MibTableColumn
igmpSnoopPortNumber=_IgmpSnoopPortNumber_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,4,1,1),_IgmpSnoopPortNumber_Type())
igmpSnoopPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopPortNumber.setStatus(_A)
_IgmpSnoopPortIsStatic_Type=TruthValue
_IgmpSnoopPortIsStatic_Object=MibTableColumn
igmpSnoopPortIsStatic=_IgmpSnoopPortIsStatic_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,4,1,2),_IgmpSnoopPortIsStatic_Type())
igmpSnoopPortIsStatic.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopPortIsStatic.setStatus(_A)
_IgmpSnoopPortTimer_Type=Unsigned32
_IgmpSnoopPortTimer_Object=MibTableColumn
igmpSnoopPortTimer=_IgmpSnoopPortTimer_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,4,1,3),_IgmpSnoopPortTimer_Type())
igmpSnoopPortTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopPortTimer.setStatus(_A)
_IgmpSnoopHostTable_Object=MibTable
igmpSnoopHostTable=_IgmpSnoopHostTable_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,5))
if mibBuilder.loadTexts:igmpSnoopHostTable.setStatus(_A)
_IgmpSnoopHostEntry_Object=MibTableRow
igmpSnoopHostEntry=_IgmpSnoopHostEntry_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,5,1))
igmpSnoopHostEntry.setIndexNames((0,_C,_D),(0,_C,_F),(0,_C,_H),(0,_C,_J))
if mibBuilder.loadTexts:igmpSnoopHostEntry.setStatus(_A)
_IgmpSnoopHostMAC_Type=MacAddress
_IgmpSnoopHostMAC_Object=MibTableColumn
igmpSnoopHostMAC=_IgmpSnoopHostMAC_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,5,1,1),_IgmpSnoopHostMAC_Type())
igmpSnoopHostMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopHostMAC.setStatus(_A)
_IgmpSnoopHostIpAddress_Type=IpAddress
_IgmpSnoopHostIpAddress_Object=MibTableColumn
igmpSnoopHostIpAddress=_IgmpSnoopHostIpAddress_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,5,1,2),_IgmpSnoopHostIpAddress_Type())
igmpSnoopHostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopHostIpAddress.setStatus(_A)
_IgmpSnoopHostTimer_Type=Unsigned32
_IgmpSnoopHostTimer_Object=MibTableColumn
igmpSnoopHostTimer=_IgmpSnoopHostTimer_Object((1,3,6,1,4,1,207,8,4,4,4,139,10,5,1,3),_IgmpSnoopHostTimer_Type())
igmpSnoopHostTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpSnoopHostTimer.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'igmp':igmp,'igmpIntInfo':igmpIntInfo,'igmpInterfaceTable':igmpInterfaceTable,'igmpInterfaceEntry':igmpInterfaceEntry,_E:igmpInterface,'igmpInterfaceName':igmpInterfaceName,'igmpQueryTimeout':igmpQueryTimeout,'igmpProxy':igmpProxy,'igmpIntStatsTable':igmpIntStatsTable,'igmpIntStatsEntry':igmpIntStatsEntry,'igmpInQuery':igmpInQuery,'igmpInReportV1':igmpInReportV1,'igmpInReportV2':igmpInReportV2,'igmpInLeave':igmpInLeave,'igmpInTotal':igmpInTotal,'igmpOutQuery':igmpOutQuery,'igmpOutTotal':igmpOutTotal,'igmpBadQuery':igmpBadQuery,'igmpBadReportV1':igmpBadReportV1,'igmpBadReportV2':igmpBadReportV2,'igmpBadLeave':igmpBadLeave,'igmpBadTotal':igmpBadTotal,'igmpIntMember':igmpIntMember,'igmpIntGroupTable':igmpIntGroupTable,'igmpIntGroupEntry':igmpIntGroupEntry,'igmpIntGroupAddress':igmpIntGroupAddress,'igmpLastHost':igmpLastHost,'igmpRefreshTime':igmpRefreshTime,'igmpSnooping':igmpSnooping,'igmpSnoopAdminInfo':igmpSnoopAdminInfo,'igmpSnoopAdminEnabled':igmpSnoopAdminEnabled,'igmpSnoopVlanTable':igmpSnoopVlanTable,'igmpSnoopVlanEntry':igmpSnoopVlanEntry,_D:igmpSnoopVID,'igmpSnoopVlanName':igmpSnoopVlanName,'igmpSnoopFastLeave':igmpSnoopFastLeave,'igmpSnoopQuerySolicit':igmpSnoopQuerySolicit,'igmpSnoopStaticRouterPorts':igmpSnoopStaticRouterPorts,'igmpSnoopGroupTable':igmpSnoopGroupTable,'igmpSnoopGroupEntry':igmpSnoopGroupEntry,_F:igmpSnoopGroupAddress,'igmpSnoopGroupTimer':igmpSnoopGroupTimer,'igmpSnoopPortTable':igmpSnoopPortTable,'igmpSnoopPortEntry':igmpSnoopPortEntry,_H:igmpSnoopPortNumber,'igmpSnoopPortIsStatic':igmpSnoopPortIsStatic,'igmpSnoopPortTimer':igmpSnoopPortTimer,'igmpSnoopHostTable':igmpSnoopHostTable,'igmpSnoopHostEntry':igmpSnoopHostEntry,_J:igmpSnoopHostMAC,'igmpSnoopHostIpAddress':igmpSnoopHostIpAddress,'igmpSnoopHostTimer':igmpSnoopHostTimer})