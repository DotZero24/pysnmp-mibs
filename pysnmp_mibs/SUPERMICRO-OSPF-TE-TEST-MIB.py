_I='fsOspfTeSasCspfPathType'
_H='fsOspfTeSasCspfPathConstraintId'
_G='fsOspfTeSasConstraintId'
_F='not-accessible'
_E='read-only'
_D='SUPERMICRO-OSPF-TE-TEST-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsOspfTeSasGroup=ModuleIdentity((1,3,6,1,4,1,10876,101,1,72,20))
if mibBuilder.loadTexts:fsOspfTeSasGroup.setRevisions(('2012-09-05 00:00',))
_FsOspfTeSas_ObjectIdentity=ObjectIdentity
fsOspfTeSas=_FsOspfTeSas_ObjectIdentity((1,3,6,1,4,1,10876,101,1,72,20,1))
_FsOspfTeSasTable_ObjectIdentity=ObjectIdentity
fsOspfTeSasTable=_FsOspfTeSasTable_ObjectIdentity((1,3,6,1,4,1,10876,101,1,72,20,2))
_FsOspfTeSasConstraintTable_Object=MibTable
fsOspfTeSasConstraintTable=_FsOspfTeSasConstraintTable_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1))
if mibBuilder.loadTexts:fsOspfTeSasConstraintTable.setStatus(_A)
_FsOspfTeSasConstraintEntry_Object=MibTableRow
fsOspfTeSasConstraintEntry=_FsOspfTeSasConstraintEntry_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1))
fsOspfTeSasConstraintEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsOspfTeSasConstraintEntry.setStatus(_A)
class _FsOspfTeSasConstraintId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsOspfTeSasConstraintId_Type.__name__=_C
_FsOspfTeSasConstraintId_Object=MibTableColumn
fsOspfTeSasConstraintId=_FsOspfTeSasConstraintId_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,1),_FsOspfTeSasConstraintId_Type())
fsOspfTeSasConstraintId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsOspfTeSasConstraintId.setStatus(_A)
_FsOspfTeSasConstraintSourceIpAddr_Type=IpAddress
_FsOspfTeSasConstraintSourceIpAddr_Object=MibTableColumn
fsOspfTeSasConstraintSourceIpAddr=_FsOspfTeSasConstraintSourceIpAddr_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,2),_FsOspfTeSasConstraintSourceIpAddr_Type())
fsOspfTeSasConstraintSourceIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintSourceIpAddr.setStatus(_A)
_FsOspfTeSasConstraintDestinationIpAddr_Type=IpAddress
_FsOspfTeSasConstraintDestinationIpAddr_Object=MibTableColumn
fsOspfTeSasConstraintDestinationIpAddr=_FsOspfTeSasConstraintDestinationIpAddr_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,3),_FsOspfTeSasConstraintDestinationIpAddr_Type())
fsOspfTeSasConstraintDestinationIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintDestinationIpAddr.setStatus(_A)
_FsOspfTeSasConstraintWPSourceIpAddr_Type=IpAddress
_FsOspfTeSasConstraintWPSourceIpAddr_Object=MibTableColumn
fsOspfTeSasConstraintWPSourceIpAddr=_FsOspfTeSasConstraintWPSourceIpAddr_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,4),_FsOspfTeSasConstraintWPSourceIpAddr_Type())
fsOspfTeSasConstraintWPSourceIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintWPSourceIpAddr.setStatus(_A)
_FsOspfTeSasConstraintWPDestinationIpAddr_Type=IpAddress
_FsOspfTeSasConstraintWPDestinationIpAddr_Object=MibTableColumn
fsOspfTeSasConstraintWPDestinationIpAddr=_FsOspfTeSasConstraintWPDestinationIpAddr_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,5),_FsOspfTeSasConstraintWPDestinationIpAddr_Type())
fsOspfTeSasConstraintWPDestinationIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintWPDestinationIpAddr.setStatus(_A)
_FsOspfTeSasConstraintMaxPathMetric_Type=Integer32
_FsOspfTeSasConstraintMaxPathMetric_Object=MibTableColumn
fsOspfTeSasConstraintMaxPathMetric=_FsOspfTeSasConstraintMaxPathMetric_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,6),_FsOspfTeSasConstraintMaxPathMetric_Type())
fsOspfTeSasConstraintMaxPathMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintMaxPathMetric.setStatus(_A)
_FsOspfTeSasConstraintMaxHopsInPath_Type=Integer32
_FsOspfTeSasConstraintMaxHopsInPath_Object=MibTableColumn
fsOspfTeSasConstraintMaxHopsInPath=_FsOspfTeSasConstraintMaxHopsInPath_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,7),_FsOspfTeSasConstraintMaxHopsInPath_Type())
fsOspfTeSasConstraintMaxHopsInPath.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintMaxHopsInPath.setStatus(_A)
class _FsOspfTeSasConstraintBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsOspfTeSasConstraintBw_Type.__name__=_C
_FsOspfTeSasConstraintBw_Object=MibTableColumn
fsOspfTeSasConstraintBw=_FsOspfTeSasConstraintBw_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,8),_FsOspfTeSasConstraintBw_Type())
fsOspfTeSasConstraintBw.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintBw.setStatus(_A)
_FsOspfTeSasConstraintIncludeAllSet_Type=Integer32
_FsOspfTeSasConstraintIncludeAllSet_Object=MibTableColumn
fsOspfTeSasConstraintIncludeAllSet=_FsOspfTeSasConstraintIncludeAllSet_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,9),_FsOspfTeSasConstraintIncludeAllSet_Type())
fsOspfTeSasConstraintIncludeAllSet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintIncludeAllSet.setStatus(_A)
_FsOspfTeSasConstraintIncludeAnySet_Type=Integer32
_FsOspfTeSasConstraintIncludeAnySet_Object=MibTableColumn
fsOspfTeSasConstraintIncludeAnySet=_FsOspfTeSasConstraintIncludeAnySet_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,10),_FsOspfTeSasConstraintIncludeAnySet_Type())
fsOspfTeSasConstraintIncludeAnySet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintIncludeAnySet.setStatus(_A)
_FsOspfTeSasConstraintExcludeAnySet_Type=Integer32
_FsOspfTeSasConstraintExcludeAnySet_Object=MibTableColumn
fsOspfTeSasConstraintExcludeAnySet=_FsOspfTeSasConstraintExcludeAnySet_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,11),_FsOspfTeSasConstraintExcludeAnySet_Type())
fsOspfTeSasConstraintExcludeAnySet.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintExcludeAnySet.setStatus(_A)
_FsOspfTeSasConstraintPriority_Type=Integer32
_FsOspfTeSasConstraintPriority_Object=MibTableColumn
fsOspfTeSasConstraintPriority=_FsOspfTeSasConstraintPriority_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,12),_FsOspfTeSasConstraintPriority_Type())
fsOspfTeSasConstraintPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintPriority.setStatus(_A)
_FsOspfTeSasConstraintExplicitRoute_Type=OctetString
_FsOspfTeSasConstraintExplicitRoute_Object=MibTableColumn
fsOspfTeSasConstraintExplicitRoute=_FsOspfTeSasConstraintExplicitRoute_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,13),_FsOspfTeSasConstraintExplicitRoute_Type())
fsOspfTeSasConstraintExplicitRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintExplicitRoute.setStatus(_A)
_FsOspfTeSasConstraintSwitchingCapability_Type=Integer32
_FsOspfTeSasConstraintSwitchingCapability_Object=MibTableColumn
fsOspfTeSasConstraintSwitchingCapability=_FsOspfTeSasConstraintSwitchingCapability_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,14),_FsOspfTeSasConstraintSwitchingCapability_Type())
fsOspfTeSasConstraintSwitchingCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintSwitchingCapability.setStatus(_A)
_FsOspfTeSasConstraintEncodingType_Type=Integer32
_FsOspfTeSasConstraintEncodingType_Object=MibTableColumn
fsOspfTeSasConstraintEncodingType=_FsOspfTeSasConstraintEncodingType_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,15),_FsOspfTeSasConstraintEncodingType_Type())
fsOspfTeSasConstraintEncodingType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintEncodingType.setStatus(_A)
_FsOspfTeSasConstraintLinkProtectionType_Type=Integer32
_FsOspfTeSasConstraintLinkProtectionType_Object=MibTableColumn
fsOspfTeSasConstraintLinkProtectionType=_FsOspfTeSasConstraintLinkProtectionType_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,16),_FsOspfTeSasConstraintLinkProtectionType_Type())
fsOspfTeSasConstraintLinkProtectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintLinkProtectionType.setStatus(_A)
class _FsOspfTeSasConstraintDiversity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('nodeDisjoint',1),('linkDisjoint',2),('sRLGDisjoint',4)))
_FsOspfTeSasConstraintDiversity_Type.__name__=_C
_FsOspfTeSasConstraintDiversity_Object=MibTableColumn
fsOspfTeSasConstraintDiversity=_FsOspfTeSasConstraintDiversity_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,17),_FsOspfTeSasConstraintDiversity_Type())
fsOspfTeSasConstraintDiversity.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintDiversity.setStatus(_A)
_FsOspfTeSasConstraintIndication_Type=Integer32
_FsOspfTeSasConstraintIndication_Object=MibTableColumn
fsOspfTeSasConstraintIndication=_FsOspfTeSasConstraintIndication_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,18),_FsOspfTeSasConstraintIndication_Type())
fsOspfTeSasConstraintIndication.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintIndication.setStatus(_A)
_FsOspfTeSasConstraintFlag_Type=Integer32
_FsOspfTeSasConstraintFlag_Object=MibTableColumn
fsOspfTeSasConstraintFlag=_FsOspfTeSasConstraintFlag_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,19),_FsOspfTeSasConstraintFlag_Type())
fsOspfTeSasConstraintFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOspfTeSasConstraintFlag.setStatus(_A)
_FsOspfTeSasConstraintStatus_Type=RowStatus
_FsOspfTeSasConstraintStatus_Object=MibTableColumn
fsOspfTeSasConstraintStatus=_FsOspfTeSasConstraintStatus_Object((1,3,6,1,4,1,10876,101,1,72,20,2,1,1,20),_FsOspfTeSasConstraintStatus_Type())
fsOspfTeSasConstraintStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsOspfTeSasConstraintStatus.setStatus(_A)
_FsOspfTeSasCspfPathTable_Object=MibTable
fsOspfTeSasCspfPathTable=_FsOspfTeSasCspfPathTable_Object((1,3,6,1,4,1,10876,101,1,72,20,2,2))
if mibBuilder.loadTexts:fsOspfTeSasCspfPathTable.setStatus(_A)
_FsOspfTeSasCspfPathEntry_Object=MibTableRow
fsOspfTeSasCspfPathEntry=_FsOspfTeSasCspfPathEntry_Object((1,3,6,1,4,1,10876,101,1,72,20,2,2,1))
fsOspfTeSasCspfPathEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:fsOspfTeSasCspfPathEntry.setStatus(_A)
class _FsOspfTeSasCspfPathConstraintId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsOspfTeSasCspfPathConstraintId_Type.__name__=_C
_FsOspfTeSasCspfPathConstraintId_Object=MibTableColumn
fsOspfTeSasCspfPathConstraintId=_FsOspfTeSasCspfPathConstraintId_Object((1,3,6,1,4,1,10876,101,1,72,20,2,2,1,1),_FsOspfTeSasCspfPathConstraintId_Type())
fsOspfTeSasCspfPathConstraintId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsOspfTeSasCspfPathConstraintId.setStatus(_A)
class _FsOspfTeSasCspfPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('backup',2)))
_FsOspfTeSasCspfPathType_Type.__name__=_C
_FsOspfTeSasCspfPathType_Object=MibTableColumn
fsOspfTeSasCspfPathType=_FsOspfTeSasCspfPathType_Object((1,3,6,1,4,1,10876,101,1,72,20,2,2,1,2),_FsOspfTeSasCspfPathType_Type())
fsOspfTeSasCspfPathType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsOspfTeSasCspfPathType.setStatus(_A)
_FsOspfTeSasCspfPathNumHops_Type=Integer32
_FsOspfTeSasCspfPathNumHops_Object=MibTableColumn
fsOspfTeSasCspfPathNumHops=_FsOspfTeSasCspfPathNumHops_Object((1,3,6,1,4,1,10876,101,1,72,20,2,2,1,3),_FsOspfTeSasCspfPathNumHops_Type())
fsOspfTeSasCspfPathNumHops.setMaxAccess(_E)
if mibBuilder.loadTexts:fsOspfTeSasCspfPathNumHops.setStatus(_A)
_FsOspfTeSasCspfPathRouterId_Type=OctetString
_FsOspfTeSasCspfPathRouterId_Object=MibTableColumn
fsOspfTeSasCspfPathRouterId=_FsOspfTeSasCspfPathRouterId_Object((1,3,6,1,4,1,10876,101,1,72,20,2,2,1,4),_FsOspfTeSasCspfPathRouterId_Type())
fsOspfTeSasCspfPathRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsOspfTeSasCspfPathRouterId.setStatus(_A)
_FsOspfTeSasCspfPathNextHopIpAddress_Type=OctetString
_FsOspfTeSasCspfPathNextHopIpAddress_Object=MibTableColumn
fsOspfTeSasCspfPathNextHopIpAddress=_FsOspfTeSasCspfPathNextHopIpAddress_Object((1,3,6,1,4,1,10876,101,1,72,20,2,2,1,5),_FsOspfTeSasCspfPathNextHopIpAddress_Type())
fsOspfTeSasCspfPathNextHopIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsOspfTeSasCspfPathNextHopIpAddress.setStatus(_A)
_FsOspfTeSasCspfPathLocalIdentifier_Type=OctetString
_FsOspfTeSasCspfPathLocalIdentifier_Object=MibTableColumn
fsOspfTeSasCspfPathLocalIdentifier=_FsOspfTeSasCspfPathLocalIdentifier_Object((1,3,6,1,4,1,10876,101,1,72,20,2,2,1,6),_FsOspfTeSasCspfPathLocalIdentifier_Type())
fsOspfTeSasCspfPathLocalIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:fsOspfTeSasCspfPathLocalIdentifier.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsOspfTeSasGroup':fsOspfTeSasGroup,'fsOspfTeSas':fsOspfTeSas,'fsOspfTeSasTable':fsOspfTeSasTable,'fsOspfTeSasConstraintTable':fsOspfTeSasConstraintTable,'fsOspfTeSasConstraintEntry':fsOspfTeSasConstraintEntry,_G:fsOspfTeSasConstraintId,'fsOspfTeSasConstraintSourceIpAddr':fsOspfTeSasConstraintSourceIpAddr,'fsOspfTeSasConstraintDestinationIpAddr':fsOspfTeSasConstraintDestinationIpAddr,'fsOspfTeSasConstraintWPSourceIpAddr':fsOspfTeSasConstraintWPSourceIpAddr,'fsOspfTeSasConstraintWPDestinationIpAddr':fsOspfTeSasConstraintWPDestinationIpAddr,'fsOspfTeSasConstraintMaxPathMetric':fsOspfTeSasConstraintMaxPathMetric,'fsOspfTeSasConstraintMaxHopsInPath':fsOspfTeSasConstraintMaxHopsInPath,'fsOspfTeSasConstraintBw':fsOspfTeSasConstraintBw,'fsOspfTeSasConstraintIncludeAllSet':fsOspfTeSasConstraintIncludeAllSet,'fsOspfTeSasConstraintIncludeAnySet':fsOspfTeSasConstraintIncludeAnySet,'fsOspfTeSasConstraintExcludeAnySet':fsOspfTeSasConstraintExcludeAnySet,'fsOspfTeSasConstraintPriority':fsOspfTeSasConstraintPriority,'fsOspfTeSasConstraintExplicitRoute':fsOspfTeSasConstraintExplicitRoute,'fsOspfTeSasConstraintSwitchingCapability':fsOspfTeSasConstraintSwitchingCapability,'fsOspfTeSasConstraintEncodingType':fsOspfTeSasConstraintEncodingType,'fsOspfTeSasConstraintLinkProtectionType':fsOspfTeSasConstraintLinkProtectionType,'fsOspfTeSasConstraintDiversity':fsOspfTeSasConstraintDiversity,'fsOspfTeSasConstraintIndication':fsOspfTeSasConstraintIndication,'fsOspfTeSasConstraintFlag':fsOspfTeSasConstraintFlag,'fsOspfTeSasConstraintStatus':fsOspfTeSasConstraintStatus,'fsOspfTeSasCspfPathTable':fsOspfTeSasCspfPathTable,'fsOspfTeSasCspfPathEntry':fsOspfTeSasCspfPathEntry,_H:fsOspfTeSasCspfPathConstraintId,_I:fsOspfTeSasCspfPathType,'fsOspfTeSasCspfPathNumHops':fsOspfTeSasCspfPathNumHops,'fsOspfTeSasCspfPathRouterId':fsOspfTeSasCspfPathRouterId,'fsOspfTeSasCspfPathNextHopIpAddress':fsOspfTeSasCspfPathNextHopIpAddress,'fsOspfTeSasCspfPathLocalIdentifier':fsOspfTeSasCspfPathLocalIdentifier})