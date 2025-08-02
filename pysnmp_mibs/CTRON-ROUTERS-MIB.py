_Y='nwRtrIfFwdCtrIfIndex'
_X='nwComponentIfInstance'
_W='nwComponentIfRtrInstance'
_V='nwComponentIfIndex'
_U='nwComponentInstance'
_T='nwComponentRtrInstance'
_S='nwRtgProtocolIfInstance'
_R='nwRtgProtocolIfRtrInstance'
_Q='nwRtgProtocolIfIndex'
_P='nwRtgProtocolInstance'
_O='nwRtgProtocolRtrInstance'
_N='nwRouterIfInstance'
_M='nwRouterIfIndex'
_L='nwRouterInstance'
_K='nwRtrStdMibIndex'
_J='invalid-config'
_I='pending-enable'
_H='pending-disable'
_G='enabled'
_F='disabled'
_E='other'
_D='Integer32'
_C='CTRON-ROUTERS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nwRouter,nwRtrHighLevelView,nwRtrMibs,nwRtrProtoSuites=mibBuilder.importSymbols('ROUTER-OIDS','nwRouter','nwRtrHighLevelView','nwRtrMibs','nwRtrProtoSuites')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_NwRtrMibRevision_ObjectIdentity=ObjectIdentity
nwRtrMibRevision=_NwRtrMibRevision_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,1,1))
_NwRtrMibRevText_Type=DisplayString
_NwRtrMibRevText_Object=MibScalar
nwRtrMibRevText=_NwRtrMibRevText_Object((1,3,6,1,4,1,52,4,2,2,2,1,1,1),_NwRtrMibRevText_Type())
nwRtrMibRevText.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrMibRevText.setStatus(_A)
_NwRtrStandardMibs_ObjectIdentity=ObjectIdentity
nwRtrStandardMibs=_NwRtrStandardMibs_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,1,2))
_NwRtrStdMibTable_Object=MibTable
nwRtrStdMibTable=_NwRtrStdMibTable_Object((1,3,6,1,4,1,52,4,2,2,2,1,2,1))
if mibBuilder.loadTexts:nwRtrStdMibTable.setStatus(_A)
_NwRtrStdMibEntry_Object=MibTableRow
nwRtrStdMibEntry=_NwRtrStdMibEntry_Object((1,3,6,1,4,1,52,4,2,2,2,1,2,1,1))
nwRtrStdMibEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:nwRtrStdMibEntry.setStatus(_A)
_NwRtrStdMibIndex_Type=Integer32
_NwRtrStdMibIndex_Object=MibTableColumn
nwRtrStdMibIndex=_NwRtrStdMibIndex_Object((1,3,6,1,4,1,52,4,2,2,2,1,2,1,1,1),_NwRtrStdMibIndex_Type())
nwRtrStdMibIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrStdMibIndex.setStatus(_A)
_NwRtrStdMibIdentifier_Type=ObjectIdentifier
_NwRtrStdMibIdentifier_Object=MibTableColumn
nwRtrStdMibIdentifier=_NwRtrStdMibIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,1,2,1,1,2),_NwRtrStdMibIdentifier_Type())
nwRtrStdMibIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrStdMibIdentifier.setStatus(_A)
_NwRtrApplicationView_ObjectIdentity=ObjectIdentity
nwRtrApplicationView=_NwRtrApplicationView_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,1))
_NwRtrApplicationSystem_ObjectIdentity=ObjectIdentity
nwRtrApplicationSystem=_NwRtrApplicationSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,1,1))
_NwRtrAdminChanges_Type=Counter32
_NwRtrAdminChanges_Object=MibScalar
nwRtrAdminChanges=_NwRtrAdminChanges_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,1),_NwRtrAdminChanges_Type())
nwRtrAdminChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrAdminChanges.setStatus(_A)
_NwRouterSystemTable_Object=MibTable
nwRouterSystemTable=_NwRouterSystemTable_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2))
if mibBuilder.loadTexts:nwRouterSystemTable.setStatus(_A)
_NwRouterEntry_Object=MibTableRow
nwRouterEntry=_NwRouterEntry_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2,1))
nwRouterEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:nwRouterEntry.setStatus(_A)
_NwRouterInstance_Type=Integer32
_NwRouterInstance_Object=MibTableColumn
nwRouterInstance=_NwRouterInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2,1,1),_NwRouterInstance_Type())
nwRouterInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterInstance.setStatus(_A)
class _NwRouterAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwRouterAdminStatus_Type.__name__=_D
_NwRouterAdminStatus_Object=MibTableColumn
nwRouterAdminStatus=_NwRouterAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2,1,2),_NwRouterAdminStatus_Type())
nwRouterAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterAdminStatus.setStatus(_A)
class _NwRouterOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_NwRouterOperStatus_Type.__name__=_D
_NwRouterOperStatus_Object=MibTableColumn
nwRouterOperStatus=_NwRouterOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2,1,3),_NwRouterOperStatus_Type())
nwRouterOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterOperStatus.setStatus(_A)
_NwRouterOperationalTime_Type=TimeTicks
_NwRouterOperationalTime_Object=MibTableColumn
nwRouterOperationalTime=_NwRouterOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2,1,4),_NwRouterOperationalTime_Type())
nwRouterOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterOperationalTime.setStatus(_A)
_NwRouterEntMibGroup_Type=ObjectIdentifier
_NwRouterEntMibGroup_Object=MibTableColumn
nwRouterEntMibGroup=_NwRouterEntMibGroup_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2,1,5),_NwRouterEntMibGroup_Type())
nwRouterEntMibGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterEntMibGroup.setStatus(_A)
_NwRouterName_Type=DisplayString
_NwRouterName_Object=MibTableColumn
nwRouterName=_NwRouterName_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2,1,6),_NwRouterName_Type())
nwRouterName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterName.setStatus(_A)
_NwRouterVersion_Type=DisplayString
_NwRouterVersion_Object=MibTableColumn
nwRouterVersion=_NwRouterVersion_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2,1,7),_NwRouterVersion_Type())
nwRouterVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterVersion.setStatus(_A)
_NwRouterIdentifier_Type=ObjectIdentifier
_NwRouterIdentifier_Object=MibTableColumn
nwRouterIdentifier=_NwRouterIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,2,1,8),_NwRouterIdentifier_Type())
nwRouterIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterIdentifier.setStatus(_A)
_NwRtrVersion_Type=DisplayString
_NwRtrVersion_Object=MibScalar
nwRtrVersion=_NwRtrVersion_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,1,3),_NwRtrVersion_Type())
nwRtrVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrVersion.setStatus(_A)
_NwRtrApplicationInterfaces_ObjectIdentity=ObjectIdentity
nwRtrApplicationInterfaces=_NwRtrApplicationInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,1,2))
_NwRouterIfTable_Object=MibTable
nwRouterIfTable=_NwRouterIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,2,1))
if mibBuilder.loadTexts:nwRouterIfTable.setStatus(_A)
_NwRouterIfEntry_Object=MibTableRow
nwRouterIfEntry=_NwRouterIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,2,1,1))
nwRouterIfEntry.setIndexNames((0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:nwRouterIfEntry.setStatus(_A)
_NwRouterIfIndex_Type=Integer32
_NwRouterIfIndex_Object=MibTableColumn
nwRouterIfIndex=_NwRouterIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,2,1,1,1),_NwRouterIfIndex_Type())
nwRouterIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterIfIndex.setStatus(_A)
_NwRouterIfInstance_Type=Integer32
_NwRouterIfInstance_Object=MibTableColumn
nwRouterIfInstance=_NwRouterIfInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,2,1,1,2),_NwRouterIfInstance_Type())
nwRouterIfInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterIfInstance.setStatus(_A)
class _NwRouterIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwRouterIfAdminStatus_Type.__name__=_D
_NwRouterIfAdminStatus_Object=MibTableColumn
nwRouterIfAdminStatus=_NwRouterIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,2,1,1,3),_NwRouterIfAdminStatus_Type())
nwRouterIfAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterIfAdminStatus.setStatus(_A)
class _NwRouterIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_NwRouterIfOperStatus_Type.__name__=_D
_NwRouterIfOperStatus_Object=MibTableColumn
nwRouterIfOperStatus=_NwRouterIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,2,1,1,4),_NwRouterIfOperStatus_Type())
nwRouterIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterIfOperStatus.setStatus(_A)
_NwRouterIfOperationalTime_Type=TimeTicks
_NwRouterIfOperationalTime_Object=MibTableColumn
nwRouterIfOperationalTime=_NwRouterIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,2,1,1,5),_NwRouterIfOperationalTime_Type())
nwRouterIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterIfOperationalTime.setStatus(_A)
_NwRouterIfName_Type=DisplayString
_NwRouterIfName_Object=MibTableColumn
nwRouterIfName=_NwRouterIfName_Object((1,3,6,1,4,1,52,4,2,2,2,2,1,2,1,1,6),_NwRouterIfName_Type())
nwRouterIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRouterIfName.setStatus(_A)
_NwRtrRoutingView_ObjectIdentity=ObjectIdentity
nwRtrRoutingView=_NwRtrRoutingView_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,2))
_NwRtrRoutingSystem_ObjectIdentity=ObjectIdentity
nwRtrRoutingSystem=_NwRtrRoutingSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,2,1))
_NwRtgProtocolTable_Object=MibTable
nwRtgProtocolTable=_NwRtgProtocolTable_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1))
if mibBuilder.loadTexts:nwRtgProtocolTable.setStatus(_A)
_NwRtgProtocolEntry_Object=MibTableRow
nwRtgProtocolEntry=_NwRtgProtocolEntry_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1))
nwRtgProtocolEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:nwRtgProtocolEntry.setStatus(_A)
_NwRtgProtocolRtrInstance_Type=Integer32
_NwRtgProtocolRtrInstance_Object=MibTableColumn
nwRtgProtocolRtrInstance=_NwRtgProtocolRtrInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1,1),_NwRtgProtocolRtrInstance_Type())
nwRtgProtocolRtrInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolRtrInstance.setStatus(_A)
_NwRtgProtocolInstance_Type=Integer32
_NwRtgProtocolInstance_Object=MibTableColumn
nwRtgProtocolInstance=_NwRtgProtocolInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1,2),_NwRtgProtocolInstance_Type())
nwRtgProtocolInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolInstance.setStatus(_A)
class _NwRtgProtocolAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwRtgProtocolAdminStatus_Type.__name__=_D
_NwRtgProtocolAdminStatus_Object=MibTableColumn
nwRtgProtocolAdminStatus=_NwRtgProtocolAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1,3),_NwRtgProtocolAdminStatus_Type())
nwRtgProtocolAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolAdminStatus.setStatus(_A)
class _NwRtgProtocolOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_NwRtgProtocolOperStatus_Type.__name__=_D
_NwRtgProtocolOperStatus_Object=MibTableColumn
nwRtgProtocolOperStatus=_NwRtgProtocolOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1,4),_NwRtgProtocolOperStatus_Type())
nwRtgProtocolOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolOperStatus.setStatus(_A)
_NwRtgProtocolOperationalTime_Type=TimeTicks
_NwRtgProtocolOperationalTime_Object=MibTableColumn
nwRtgProtocolOperationalTime=_NwRtgProtocolOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1,5),_NwRtgProtocolOperationalTime_Type())
nwRtgProtocolOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolOperationalTime.setStatus(_A)
_NwRtgProtocolEntMibGroup_Type=ObjectIdentifier
_NwRtgProtocolEntMibGroup_Object=MibTableColumn
nwRtgProtocolEntMibGroup=_NwRtgProtocolEntMibGroup_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1,6),_NwRtgProtocolEntMibGroup_Type())
nwRtgProtocolEntMibGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolEntMibGroup.setStatus(_A)
_NwRtgProtocolName_Type=DisplayString
_NwRtgProtocolName_Object=MibTableColumn
nwRtgProtocolName=_NwRtgProtocolName_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1,7),_NwRtgProtocolName_Type())
nwRtgProtocolName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolName.setStatus(_A)
_NwRtgProtocolVersion_Type=DisplayString
_NwRtgProtocolVersion_Object=MibTableColumn
nwRtgProtocolVersion=_NwRtgProtocolVersion_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1,8),_NwRtgProtocolVersion_Type())
nwRtgProtocolVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolVersion.setStatus(_A)
_NwRtgProtocolIdentifier_Type=ObjectIdentifier
_NwRtgProtocolIdentifier_Object=MibTableColumn
nwRtgProtocolIdentifier=_NwRtgProtocolIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,1,1,1,9),_NwRtgProtocolIdentifier_Type())
nwRtgProtocolIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolIdentifier.setStatus(_A)
_NwRtrRoutingInterfaces_ObjectIdentity=ObjectIdentity
nwRtrRoutingInterfaces=_NwRtrRoutingInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,2,2))
_NwRtgProtocolIfTable_Object=MibTable
nwRtgProtocolIfTable=_NwRtgProtocolIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,2,1))
if mibBuilder.loadTexts:nwRtgProtocolIfTable.setStatus(_A)
_NwRtgProtocolIfEntry_Object=MibTableRow
nwRtgProtocolIfEntry=_NwRtgProtocolIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,2,1,1))
nwRtgProtocolIfEntry.setIndexNames((0,_C,_Q),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:nwRtgProtocolIfEntry.setStatus(_A)
_NwRtgProtocolIfIndex_Type=Integer32
_NwRtgProtocolIfIndex_Object=MibTableColumn
nwRtgProtocolIfIndex=_NwRtgProtocolIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,2,1,1,1),_NwRtgProtocolIfIndex_Type())
nwRtgProtocolIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolIfIndex.setStatus(_A)
_NwRtgProtocolIfRtrInstance_Type=Integer32
_NwRtgProtocolIfRtrInstance_Object=MibTableColumn
nwRtgProtocolIfRtrInstance=_NwRtgProtocolIfRtrInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,2,1,1,2),_NwRtgProtocolIfRtrInstance_Type())
nwRtgProtocolIfRtrInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolIfRtrInstance.setStatus(_A)
_NwRtgProtocolIfInstance_Type=Integer32
_NwRtgProtocolIfInstance_Object=MibTableColumn
nwRtgProtocolIfInstance=_NwRtgProtocolIfInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,2,1,1,3),_NwRtgProtocolIfInstance_Type())
nwRtgProtocolIfInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolIfInstance.setStatus(_A)
class _NwRtgProtocolIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwRtgProtocolIfAdminStatus_Type.__name__=_D
_NwRtgProtocolIfAdminStatus_Object=MibTableColumn
nwRtgProtocolIfAdminStatus=_NwRtgProtocolIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,2,1,1,4),_NwRtgProtocolIfAdminStatus_Type())
nwRtgProtocolIfAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolIfAdminStatus.setStatus(_A)
class _NwRtgProtocolIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_NwRtgProtocolIfOperStatus_Type.__name__=_D
_NwRtgProtocolIfOperStatus_Object=MibTableColumn
nwRtgProtocolIfOperStatus=_NwRtgProtocolIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,2,1,1,5),_NwRtgProtocolIfOperStatus_Type())
nwRtgProtocolIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolIfOperStatus.setStatus(_A)
_NwRtgProtocolIfOperationalTime_Type=TimeTicks
_NwRtgProtocolIfOperationalTime_Object=MibTableColumn
nwRtgProtocolIfOperationalTime=_NwRtgProtocolIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,2,1,1,6),_NwRtgProtocolIfOperationalTime_Type())
nwRtgProtocolIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolIfOperationalTime.setStatus(_A)
_NwRtgProtocolIfName_Type=DisplayString
_NwRtgProtocolIfName_Object=MibTableColumn
nwRtgProtocolIfName=_NwRtgProtocolIfName_Object((1,3,6,1,4,1,52,4,2,2,2,2,2,2,1,1,7),_NwRtgProtocolIfName_Type())
nwRtgProtocolIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtgProtocolIfName.setStatus(_A)
_NwRtrComponentView_ObjectIdentity=ObjectIdentity
nwRtrComponentView=_NwRtrComponentView_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,3))
_NwRtrComponentSystem_ObjectIdentity=ObjectIdentity
nwRtrComponentSystem=_NwRtrComponentSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,3,1))
_NwComponentTable_Object=MibTable
nwComponentTable=_NwComponentTable_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1))
if mibBuilder.loadTexts:nwComponentTable.setStatus(_A)
_NwComponentEntry_Object=MibTableRow
nwComponentEntry=_NwComponentEntry_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1))
nwComponentEntry.setIndexNames((0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:nwComponentEntry.setStatus(_A)
_NwComponentRtrInstance_Type=Integer32
_NwComponentRtrInstance_Object=MibTableColumn
nwComponentRtrInstance=_NwComponentRtrInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1,1),_NwComponentRtrInstance_Type())
nwComponentRtrInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentRtrInstance.setStatus(_A)
_NwComponentInstance_Type=Integer32
_NwComponentInstance_Object=MibTableColumn
nwComponentInstance=_NwComponentInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1,2),_NwComponentInstance_Type())
nwComponentInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentInstance.setStatus(_A)
class _NwComponentAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwComponentAdminStatus_Type.__name__=_D
_NwComponentAdminStatus_Object=MibTableColumn
nwComponentAdminStatus=_NwComponentAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1,3),_NwComponentAdminStatus_Type())
nwComponentAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentAdminStatus.setStatus(_A)
class _NwComponentOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_NwComponentOperStatus_Type.__name__=_D
_NwComponentOperStatus_Object=MibTableColumn
nwComponentOperStatus=_NwComponentOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1,4),_NwComponentOperStatus_Type())
nwComponentOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentOperStatus.setStatus(_A)
_NwComponentOperationalTime_Type=TimeTicks
_NwComponentOperationalTime_Object=MibTableColumn
nwComponentOperationalTime=_NwComponentOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1,5),_NwComponentOperationalTime_Type())
nwComponentOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentOperationalTime.setStatus(_A)
_NwComponentEntMibGroup_Type=ObjectIdentifier
_NwComponentEntMibGroup_Object=MibTableColumn
nwComponentEntMibGroup=_NwComponentEntMibGroup_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1,6),_NwComponentEntMibGroup_Type())
nwComponentEntMibGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentEntMibGroup.setStatus(_A)
_NwComponentName_Type=DisplayString
_NwComponentName_Object=MibTableColumn
nwComponentName=_NwComponentName_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1,7),_NwComponentName_Type())
nwComponentName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentName.setStatus(_A)
_NwComponentVersion_Type=DisplayString
_NwComponentVersion_Object=MibTableColumn
nwComponentVersion=_NwComponentVersion_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1,8),_NwComponentVersion_Type())
nwComponentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentVersion.setStatus(_A)
_NwComponentIdentifier_Type=ObjectIdentifier
_NwComponentIdentifier_Object=MibTableColumn
nwComponentIdentifier=_NwComponentIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,1,1,1,9),_NwComponentIdentifier_Type())
nwComponentIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentIdentifier.setStatus(_A)
_NwRtrComponentInterfaces_ObjectIdentity=ObjectIdentity
nwRtrComponentInterfaces=_NwRtrComponentInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,3,2))
_NwComponentIfTable_Object=MibTable
nwComponentIfTable=_NwComponentIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,2,1))
if mibBuilder.loadTexts:nwComponentIfTable.setStatus(_A)
_NwComponentIfEntry_Object=MibTableRow
nwComponentIfEntry=_NwComponentIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,2,1,1))
nwComponentIfEntry.setIndexNames((0,_C,_V),(0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:nwComponentIfEntry.setStatus(_A)
_NwComponentIfIndex_Type=Integer32
_NwComponentIfIndex_Object=MibTableColumn
nwComponentIfIndex=_NwComponentIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,2,1,1,1),_NwComponentIfIndex_Type())
nwComponentIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentIfIndex.setStatus(_A)
_NwComponentIfRtrInstance_Type=Integer32
_NwComponentIfRtrInstance_Object=MibTableColumn
nwComponentIfRtrInstance=_NwComponentIfRtrInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,2,1,1,2),_NwComponentIfRtrInstance_Type())
nwComponentIfRtrInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentIfRtrInstance.setStatus(_A)
_NwComponentIfInstance_Type=Integer32
_NwComponentIfInstance_Object=MibTableColumn
nwComponentIfInstance=_NwComponentIfInstance_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,2,1,1,3),_NwComponentIfInstance_Type())
nwComponentIfInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentIfInstance.setStatus(_A)
class _NwComponentIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwComponentIfAdminStatus_Type.__name__=_D
_NwComponentIfAdminStatus_Object=MibTableColumn
nwComponentIfAdminStatus=_NwComponentIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,2,1,1,4),_NwComponentIfAdminStatus_Type())
nwComponentIfAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentIfAdminStatus.setStatus(_A)
class _NwComponentIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_NwComponentIfOperStatus_Type.__name__=_D
_NwComponentIfOperStatus_Object=MibTableColumn
nwComponentIfOperStatus=_NwComponentIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,2,1,1,5),_NwComponentIfOperStatus_Type())
nwComponentIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentIfOperStatus.setStatus(_A)
_NwComponentIfOperationalTime_Type=TimeTicks
_NwComponentIfOperationalTime_Object=MibTableColumn
nwComponentIfOperationalTime=_NwComponentIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,2,1,1,6),_NwComponentIfOperationalTime_Type())
nwComponentIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentIfOperationalTime.setStatus(_A)
_NwComponentIfName_Type=DisplayString
_NwComponentIfName_Object=MibTableColumn
nwComponentIfName=_NwComponentIfName_Object((1,3,6,1,4,1,52,4,2,2,2,2,3,2,1,1,7),_NwComponentIfName_Type())
nwComponentIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwComponentIfName.setStatus(_A)
_NwRtrCountersView_ObjectIdentity=ObjectIdentity
nwRtrCountersView=_NwRtrCountersView_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,4))
_NwRtrCountersControl_ObjectIdentity=ObjectIdentity
nwRtrCountersControl=_NwRtrCountersControl_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,4,1))
_NwRtrInterfaceCounters_ObjectIdentity=ObjectIdentity
nwRtrInterfaceCounters=_NwRtrInterfaceCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,2,4,2))
_NwRtrIfFwdCtrTable_Object=MibTable
nwRtrIfFwdCtrTable=_NwRtrIfFwdCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1))
if mibBuilder.loadTexts:nwRtrIfFwdCtrTable.setStatus(_A)
_NwRtrIfFwdCtrEntry_Object=MibTableRow
nwRtrIfFwdCtrEntry=_NwRtrIfFwdCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1))
nwRtrIfFwdCtrEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:nwRtrIfFwdCtrEntry.setStatus(_A)
_NwRtrIfFwdCtrIfIndex_Type=Integer32
_NwRtrIfFwdCtrIfIndex_Object=MibTableColumn
nwRtrIfFwdCtrIfIndex=_NwRtrIfFwdCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,1),_NwRtrIfFwdCtrIfIndex_Type())
nwRtrIfFwdCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrIfIndex.setStatus(_A)
class _NwRtrIfFwdCtrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwRtrIfFwdCtrOperStatus_Type.__name__=_D
_NwRtrIfFwdCtrOperStatus_Object=MibTableColumn
nwRtrIfFwdCtrOperStatus=_NwRtrIfFwdCtrOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,2),_NwRtrIfFwdCtrOperStatus_Type())
nwRtrIfFwdCtrOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrOperStatus.setStatus(_A)
_NwRtrIfFwdCtrInPkts_Type=Counter32
_NwRtrIfFwdCtrInPkts_Object=MibTableColumn
nwRtrIfFwdCtrInPkts=_NwRtrIfFwdCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,3),_NwRtrIfFwdCtrInPkts_Type())
nwRtrIfFwdCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrInPkts.setStatus(_A)
_NwRtrIfFwdCtrOutPkts_Type=Counter32
_NwRtrIfFwdCtrOutPkts_Object=MibTableColumn
nwRtrIfFwdCtrOutPkts=_NwRtrIfFwdCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,4),_NwRtrIfFwdCtrOutPkts_Type())
nwRtrIfFwdCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrOutPkts.setStatus(_A)
_NwRtrIfFwdCtrFwdPkts_Type=Counter32
_NwRtrIfFwdCtrFwdPkts_Object=MibTableColumn
nwRtrIfFwdCtrFwdPkts=_NwRtrIfFwdCtrFwdPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,5),_NwRtrIfFwdCtrFwdPkts_Type())
nwRtrIfFwdCtrFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrFwdPkts.setStatus(_A)
_NwRtrIfFwdCtrFilteredPkts_Type=Counter32
_NwRtrIfFwdCtrFilteredPkts_Object=MibTableColumn
nwRtrIfFwdCtrFilteredPkts=_NwRtrIfFwdCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,6),_NwRtrIfFwdCtrFilteredPkts_Type())
nwRtrIfFwdCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrFilteredPkts.setStatus(_A)
_NwRtrIfFwdCtrDiscardPkts_Type=Counter32
_NwRtrIfFwdCtrDiscardPkts_Object=MibTableColumn
nwRtrIfFwdCtrDiscardPkts=_NwRtrIfFwdCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,7),_NwRtrIfFwdCtrDiscardPkts_Type())
nwRtrIfFwdCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrDiscardPkts.setStatus(_A)
_NwRtrIfFwdCtrAddrErrPkts_Type=Counter32
_NwRtrIfFwdCtrAddrErrPkts_Object=MibTableColumn
nwRtrIfFwdCtrAddrErrPkts=_NwRtrIfFwdCtrAddrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,8),_NwRtrIfFwdCtrAddrErrPkts_Type())
nwRtrIfFwdCtrAddrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrAddrErrPkts.setStatus(_A)
_NwRtrIfFwdCtrLenErrPkts_Type=Counter32
_NwRtrIfFwdCtrLenErrPkts_Object=MibTableColumn
nwRtrIfFwdCtrLenErrPkts=_NwRtrIfFwdCtrLenErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,9),_NwRtrIfFwdCtrLenErrPkts_Type())
nwRtrIfFwdCtrLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrLenErrPkts.setStatus(_A)
_NwRtrIfFwdCtrHdrErrPkts_Type=Counter32
_NwRtrIfFwdCtrHdrErrPkts_Object=MibTableColumn
nwRtrIfFwdCtrHdrErrPkts=_NwRtrIfFwdCtrHdrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,10),_NwRtrIfFwdCtrHdrErrPkts_Type())
nwRtrIfFwdCtrHdrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrHdrErrPkts.setStatus(_A)
_NwRtrIfFwdCtrInBytes_Type=Counter32
_NwRtrIfFwdCtrInBytes_Object=MibTableColumn
nwRtrIfFwdCtrInBytes=_NwRtrIfFwdCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,11),_NwRtrIfFwdCtrInBytes_Type())
nwRtrIfFwdCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrInBytes.setStatus(_A)
_NwRtrIfFwdCtrOutBytes_Type=Counter32
_NwRtrIfFwdCtrOutBytes_Object=MibTableColumn
nwRtrIfFwdCtrOutBytes=_NwRtrIfFwdCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,12),_NwRtrIfFwdCtrOutBytes_Type())
nwRtrIfFwdCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrOutBytes.setStatus(_A)
_NwRtrIfFwdCtrFwdBytes_Type=Counter32
_NwRtrIfFwdCtrFwdBytes_Object=MibTableColumn
nwRtrIfFwdCtrFwdBytes=_NwRtrIfFwdCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,13),_NwRtrIfFwdCtrFwdBytes_Type())
nwRtrIfFwdCtrFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrFwdBytes.setStatus(_A)
_NwRtrIfFwdCtrFilteredBytes_Type=Counter32
_NwRtrIfFwdCtrFilteredBytes_Object=MibTableColumn
nwRtrIfFwdCtrFilteredBytes=_NwRtrIfFwdCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,14),_NwRtrIfFwdCtrFilteredBytes_Type())
nwRtrIfFwdCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrFilteredBytes.setStatus(_A)
_NwRtrIfFwdCtrDiscardBytes_Type=Counter32
_NwRtrIfFwdCtrDiscardBytes_Object=MibTableColumn
nwRtrIfFwdCtrDiscardBytes=_NwRtrIfFwdCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,15),_NwRtrIfFwdCtrDiscardBytes_Type())
nwRtrIfFwdCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrDiscardBytes.setStatus(_A)
_NwRtrIfFwdCtrHostInPkts_Type=Counter32
_NwRtrIfFwdCtrHostInPkts_Object=MibTableColumn
nwRtrIfFwdCtrHostInPkts=_NwRtrIfFwdCtrHostInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,16),_NwRtrIfFwdCtrHostInPkts_Type())
nwRtrIfFwdCtrHostInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrHostInPkts.setStatus(_A)
_NwRtrIfFwdCtrHostOutPkts_Type=Counter32
_NwRtrIfFwdCtrHostOutPkts_Object=MibTableColumn
nwRtrIfFwdCtrHostOutPkts=_NwRtrIfFwdCtrHostOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,17),_NwRtrIfFwdCtrHostOutPkts_Type())
nwRtrIfFwdCtrHostOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrHostOutPkts.setStatus(_A)
_NwRtrIfFwdCtrHostDiscardPkts_Type=Counter32
_NwRtrIfFwdCtrHostDiscardPkts_Object=MibTableColumn
nwRtrIfFwdCtrHostDiscardPkts=_NwRtrIfFwdCtrHostDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,18),_NwRtrIfFwdCtrHostDiscardPkts_Type())
nwRtrIfFwdCtrHostDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrHostDiscardPkts.setStatus(_A)
_NwRtrIfFwdCtrHostInBytes_Type=Counter32
_NwRtrIfFwdCtrHostInBytes_Object=MibTableColumn
nwRtrIfFwdCtrHostInBytes=_NwRtrIfFwdCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,19),_NwRtrIfFwdCtrHostInBytes_Type())
nwRtrIfFwdCtrHostInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrHostInBytes.setStatus(_A)
_NwRtrIfFwdCtrHostOutBytes_Type=Counter32
_NwRtrIfFwdCtrHostOutBytes_Object=MibTableColumn
nwRtrIfFwdCtrHostOutBytes=_NwRtrIfFwdCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,20),_NwRtrIfFwdCtrHostOutBytes_Type())
nwRtrIfFwdCtrHostOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrHostOutBytes.setStatus(_A)
_NwRtrIfFwdCtrHostDiscardBytes_Type=Counter32
_NwRtrIfFwdCtrHostDiscardBytes_Object=MibTableColumn
nwRtrIfFwdCtrHostDiscardBytes=_NwRtrIfFwdCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,2,4,2,1,1,21),_NwRtrIfFwdCtrHostDiscardBytes_Type())
nwRtrIfFwdCtrHostDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwRtrIfFwdCtrHostDiscardBytes.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nwRtrMibRevision':nwRtrMibRevision,'nwRtrMibRevText':nwRtrMibRevText,'nwRtrStandardMibs':nwRtrStandardMibs,'nwRtrStdMibTable':nwRtrStdMibTable,'nwRtrStdMibEntry':nwRtrStdMibEntry,_K:nwRtrStdMibIndex,'nwRtrStdMibIdentifier':nwRtrStdMibIdentifier,'nwRtrApplicationView':nwRtrApplicationView,'nwRtrApplicationSystem':nwRtrApplicationSystem,'nwRtrAdminChanges':nwRtrAdminChanges,'nwRouterSystemTable':nwRouterSystemTable,'nwRouterEntry':nwRouterEntry,_L:nwRouterInstance,'nwRouterAdminStatus':nwRouterAdminStatus,'nwRouterOperStatus':nwRouterOperStatus,'nwRouterOperationalTime':nwRouterOperationalTime,'nwRouterEntMibGroup':nwRouterEntMibGroup,'nwRouterName':nwRouterName,'nwRouterVersion':nwRouterVersion,'nwRouterIdentifier':nwRouterIdentifier,'nwRtrVersion':nwRtrVersion,'nwRtrApplicationInterfaces':nwRtrApplicationInterfaces,'nwRouterIfTable':nwRouterIfTable,'nwRouterIfEntry':nwRouterIfEntry,_M:nwRouterIfIndex,_N:nwRouterIfInstance,'nwRouterIfAdminStatus':nwRouterIfAdminStatus,'nwRouterIfOperStatus':nwRouterIfOperStatus,'nwRouterIfOperationalTime':nwRouterIfOperationalTime,'nwRouterIfName':nwRouterIfName,'nwRtrRoutingView':nwRtrRoutingView,'nwRtrRoutingSystem':nwRtrRoutingSystem,'nwRtgProtocolTable':nwRtgProtocolTable,'nwRtgProtocolEntry':nwRtgProtocolEntry,_O:nwRtgProtocolRtrInstance,_P:nwRtgProtocolInstance,'nwRtgProtocolAdminStatus':nwRtgProtocolAdminStatus,'nwRtgProtocolOperStatus':nwRtgProtocolOperStatus,'nwRtgProtocolOperationalTime':nwRtgProtocolOperationalTime,'nwRtgProtocolEntMibGroup':nwRtgProtocolEntMibGroup,'nwRtgProtocolName':nwRtgProtocolName,'nwRtgProtocolVersion':nwRtgProtocolVersion,'nwRtgProtocolIdentifier':nwRtgProtocolIdentifier,'nwRtrRoutingInterfaces':nwRtrRoutingInterfaces,'nwRtgProtocolIfTable':nwRtgProtocolIfTable,'nwRtgProtocolIfEntry':nwRtgProtocolIfEntry,_Q:nwRtgProtocolIfIndex,_R:nwRtgProtocolIfRtrInstance,_S:nwRtgProtocolIfInstance,'nwRtgProtocolIfAdminStatus':nwRtgProtocolIfAdminStatus,'nwRtgProtocolIfOperStatus':nwRtgProtocolIfOperStatus,'nwRtgProtocolIfOperationalTime':nwRtgProtocolIfOperationalTime,'nwRtgProtocolIfName':nwRtgProtocolIfName,'nwRtrComponentView':nwRtrComponentView,'nwRtrComponentSystem':nwRtrComponentSystem,'nwComponentTable':nwComponentTable,'nwComponentEntry':nwComponentEntry,_T:nwComponentRtrInstance,_U:nwComponentInstance,'nwComponentAdminStatus':nwComponentAdminStatus,'nwComponentOperStatus':nwComponentOperStatus,'nwComponentOperationalTime':nwComponentOperationalTime,'nwComponentEntMibGroup':nwComponentEntMibGroup,'nwComponentName':nwComponentName,'nwComponentVersion':nwComponentVersion,'nwComponentIdentifier':nwComponentIdentifier,'nwRtrComponentInterfaces':nwRtrComponentInterfaces,'nwComponentIfTable':nwComponentIfTable,'nwComponentIfEntry':nwComponentIfEntry,_V:nwComponentIfIndex,_W:nwComponentIfRtrInstance,_X:nwComponentIfInstance,'nwComponentIfAdminStatus':nwComponentIfAdminStatus,'nwComponentIfOperStatus':nwComponentIfOperStatus,'nwComponentIfOperationalTime':nwComponentIfOperationalTime,'nwComponentIfName':nwComponentIfName,'nwRtrCountersView':nwRtrCountersView,'nwRtrCountersControl':nwRtrCountersControl,'nwRtrInterfaceCounters':nwRtrInterfaceCounters,'nwRtrIfFwdCtrTable':nwRtrIfFwdCtrTable,'nwRtrIfFwdCtrEntry':nwRtrIfFwdCtrEntry,_Y:nwRtrIfFwdCtrIfIndex,'nwRtrIfFwdCtrOperStatus':nwRtrIfFwdCtrOperStatus,'nwRtrIfFwdCtrInPkts':nwRtrIfFwdCtrInPkts,'nwRtrIfFwdCtrOutPkts':nwRtrIfFwdCtrOutPkts,'nwRtrIfFwdCtrFwdPkts':nwRtrIfFwdCtrFwdPkts,'nwRtrIfFwdCtrFilteredPkts':nwRtrIfFwdCtrFilteredPkts,'nwRtrIfFwdCtrDiscardPkts':nwRtrIfFwdCtrDiscardPkts,'nwRtrIfFwdCtrAddrErrPkts':nwRtrIfFwdCtrAddrErrPkts,'nwRtrIfFwdCtrLenErrPkts':nwRtrIfFwdCtrLenErrPkts,'nwRtrIfFwdCtrHdrErrPkts':nwRtrIfFwdCtrHdrErrPkts,'nwRtrIfFwdCtrInBytes':nwRtrIfFwdCtrInBytes,'nwRtrIfFwdCtrOutBytes':nwRtrIfFwdCtrOutBytes,'nwRtrIfFwdCtrFwdBytes':nwRtrIfFwdCtrFwdBytes,'nwRtrIfFwdCtrFilteredBytes':nwRtrIfFwdCtrFilteredBytes,'nwRtrIfFwdCtrDiscardBytes':nwRtrIfFwdCtrDiscardBytes,'nwRtrIfFwdCtrHostInPkts':nwRtrIfFwdCtrHostInPkts,'nwRtrIfFwdCtrHostOutPkts':nwRtrIfFwdCtrHostOutPkts,'nwRtrIfFwdCtrHostDiscardPkts':nwRtrIfFwdCtrHostDiscardPkts,'nwRtrIfFwdCtrHostInBytes':nwRtrIfFwdCtrHostInBytes,'nwRtrIfFwdCtrHostOutBytes':nwRtrIfFwdCtrHostOutBytes,'nwRtrIfFwdCtrHostDiscardBytes':nwRtrIfFwdCtrHostDiscardBytes})