_G='cienaOme6500OptmonsProtGroupProtIfIndex'
_F='cienaOme6500OptmonsProtGroupWrkgIfIndex'
_E='cienaOme6500OptmonsIfIndex'
_D='CIENA-OME6500-OPTMONS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGenericMIBs,=mibBuilder.importSymbols('CIENA-SMI','cienaGenericMIBs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaOme6500OptmonsMIB=ModuleIdentity((1,3,6,1,4,1,1271,29,7))
if mibBuilder.loadTexts:cienaOme6500OptmonsMIB.setRevisions(('2017-12-13 00:00','2018-04-23 00:00','2018-06-20 00:00'))
_CienaOme6500OptmonsTable_Object=MibTable
cienaOme6500OptmonsTable=_CienaOme6500OptmonsTable_Object((1,3,6,1,4,1,1271,29,7,1))
if mibBuilder.loadTexts:cienaOme6500OptmonsTable.setStatus(_A)
_CienaOme6500OptmonsEntry_Object=MibTableRow
cienaOme6500OptmonsEntry=_CienaOme6500OptmonsEntry_Object((1,3,6,1,4,1,1271,29,7,1,1))
cienaOme6500OptmonsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cienaOme6500OptmonsEntry.setStatus(_A)
_CienaOme6500OptmonsIfIndex_Type=InterfaceIndex
_CienaOme6500OptmonsIfIndex_Object=MibTableColumn
cienaOme6500OptmonsIfIndex=_CienaOme6500OptmonsIfIndex_Object((1,3,6,1,4,1,1271,29,7,1,1,1),_CienaOme6500OptmonsIfIndex_Type())
cienaOme6500OptmonsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsIfIndex.setStatus(_A)
_CienaOme6500OptmonsIfDescr_Type=DisplayString
_CienaOme6500OptmonsIfDescr_Object=MibTableColumn
cienaOme6500OptmonsIfDescr=_CienaOme6500OptmonsIfDescr_Object((1,3,6,1,4,1,1271,29,7,1,1,2),_CienaOme6500OptmonsIfDescr_Type())
cienaOme6500OptmonsIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsIfDescr.setStatus(_A)
_CienaOme6500OptmonsSst_Type=DisplayString
_CienaOme6500OptmonsSst_Object=MibTableColumn
cienaOme6500OptmonsSst=_CienaOme6500OptmonsSst_Object((1,3,6,1,4,1,1271,29,7,1,1,3),_CienaOme6500OptmonsSst_Type())
cienaOme6500OptmonsSst.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsSst.setStatus(_A)
class _CienaOme6500OptmonsPst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('is',0),('oosMa',1),('isAnr',2),('oosAu',3),('oosAuma',4),('oosMaanr',5)))
_CienaOme6500OptmonsPst_Type.__name__=_C
_CienaOme6500OptmonsPst_Object=MibTableColumn
cienaOme6500OptmonsPst=_CienaOme6500OptmonsPst_Object((1,3,6,1,4,1,1271,29,7,1,1,4),_CienaOme6500OptmonsPst_Type())
cienaOme6500OptmonsPst.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsPst.setStatus(_A)
_CienaOme6500OptmonsAinsTimeLeft_Type=DisplayString
_CienaOme6500OptmonsAinsTimeLeft_Object=MibTableColumn
cienaOme6500OptmonsAinsTimeLeft=_CienaOme6500OptmonsAinsTimeLeft_Object((1,3,6,1,4,1,1271,29,7,1,1,5),_CienaOme6500OptmonsAinsTimeLeft_Type())
cienaOme6500OptmonsAinsTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsAinsTimeLeft.setStatus(_A)
_CienaOme6500OptmonsLosThres_Type=DisplayString
_CienaOme6500OptmonsLosThres_Object=MibTableColumn
cienaOme6500OptmonsLosThres=_CienaOme6500OptmonsLosThres_Object((1,3,6,1,4,1,1271,29,7,1,1,6),_CienaOme6500OptmonsLosThres_Type())
cienaOme6500OptmonsLosThres.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsLosThres.setStatus(_A)
_CienaOme6500OptmonsPortLabel_Type=DisplayString
_CienaOme6500OptmonsPortLabel_Object=MibTableColumn
cienaOme6500OptmonsPortLabel=_CienaOme6500OptmonsPortLabel_Object((1,3,6,1,4,1,1271,29,7,1,1,7),_CienaOme6500OptmonsPortLabel_Type())
cienaOme6500OptmonsPortLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsPortLabel.setStatus(_A)
_CienaOme6500OptmonsAlsoDisabled_Type=DisplayString
_CienaOme6500OptmonsAlsoDisabled_Object=MibTableColumn
cienaOme6500OptmonsAlsoDisabled=_CienaOme6500OptmonsAlsoDisabled_Object((1,3,6,1,4,1,1271,29,7,1,1,8),_CienaOme6500OptmonsAlsoDisabled_Type())
cienaOme6500OptmonsAlsoDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsAlsoDisabled.setStatus(_A)
_CienaOme6500OptmonsProtNswSwStatus_Type=DisplayString
_CienaOme6500OptmonsProtNswSwStatus_Object=MibTableColumn
cienaOme6500OptmonsProtNswSwStatus=_CienaOme6500OptmonsProtNswSwStatus_Object((1,3,6,1,4,1,1271,29,7,1,1,9),_CienaOme6500OptmonsProtNswSwStatus_Type())
cienaOme6500OptmonsProtNswSwStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtNswSwStatus.setStatus(_A)
_CienaOme6500OptmonsProtNswSwEnd_Type=DisplayString
_CienaOme6500OptmonsProtNswSwEnd_Object=MibTableColumn
cienaOme6500OptmonsProtNswSwEnd=_CienaOme6500OptmonsProtNswSwEnd_Object((1,3,6,1,4,1,1271,29,7,1,1,10),_CienaOme6500OptmonsProtNswSwEnd_Type())
cienaOme6500OptmonsProtNswSwEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtNswSwEnd.setStatus(_A)
_CienaOme6500OptmonsProtNswSwReason_Type=DisplayString
_CienaOme6500OptmonsProtNswSwReason_Object=MibTableColumn
cienaOme6500OptmonsProtNswSwReason=_CienaOme6500OptmonsProtNswSwReason_Object((1,3,6,1,4,1,1271,29,7,1,1,11),_CienaOme6500OptmonsProtNswSwReason_Type())
cienaOme6500OptmonsProtNswSwReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtNswSwReason.setStatus(_A)
_CienaOme6500OptmonsProtGroupTable_Object=MibTable
cienaOme6500OptmonsProtGroupTable=_CienaOme6500OptmonsProtGroupTable_Object((1,3,6,1,4,1,1271,29,7,2))
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupTable.setStatus(_A)
_CienaOme6500OptmonsProtGroupEntry_Object=MibTableRow
cienaOme6500OptmonsProtGroupEntry=_CienaOme6500OptmonsProtGroupEntry_Object((1,3,6,1,4,1,1271,29,7,2,1))
cienaOme6500OptmonsProtGroupEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupEntry.setStatus(_A)
_CienaOme6500OptmonsProtGroupWrkgIfIndex_Type=InterfaceIndex
_CienaOme6500OptmonsProtGroupWrkgIfIndex_Object=MibTableColumn
cienaOme6500OptmonsProtGroupWrkgIfIndex=_CienaOme6500OptmonsProtGroupWrkgIfIndex_Object((1,3,6,1,4,1,1271,29,7,2,1,1),_CienaOme6500OptmonsProtGroupWrkgIfIndex_Type())
cienaOme6500OptmonsProtGroupWrkgIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupWrkgIfIndex.setStatus(_A)
_CienaOme6500OptmonsProtGroupWrkgIfDescr_Type=DisplayString
_CienaOme6500OptmonsProtGroupWrkgIfDescr_Object=MibTableColumn
cienaOme6500OptmonsProtGroupWrkgIfDescr=_CienaOme6500OptmonsProtGroupWrkgIfDescr_Object((1,3,6,1,4,1,1271,29,7,2,1,2),_CienaOme6500OptmonsProtGroupWrkgIfDescr_Type())
cienaOme6500OptmonsProtGroupWrkgIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupWrkgIfDescr.setStatus(_A)
_CienaOme6500OptmonsProtGroupWrkgSst_Type=DisplayString
_CienaOme6500OptmonsProtGroupWrkgSst_Object=MibTableColumn
cienaOme6500OptmonsProtGroupWrkgSst=_CienaOme6500OptmonsProtGroupWrkgSst_Object((1,3,6,1,4,1,1271,29,7,2,1,3),_CienaOme6500OptmonsProtGroupWrkgSst_Type())
cienaOme6500OptmonsProtGroupWrkgSst.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupWrkgSst.setStatus(_A)
_CienaOme6500OptmonsProtGroupProtIfIndex_Type=InterfaceIndex
_CienaOme6500OptmonsProtGroupProtIfIndex_Object=MibTableColumn
cienaOme6500OptmonsProtGroupProtIfIndex=_CienaOme6500OptmonsProtGroupProtIfIndex_Object((1,3,6,1,4,1,1271,29,7,2,1,4),_CienaOme6500OptmonsProtGroupProtIfIndex_Type())
cienaOme6500OptmonsProtGroupProtIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupProtIfIndex.setStatus(_A)
_CienaOme6500OptmonsProtGroupProtIfDescr_Type=DisplayString
_CienaOme6500OptmonsProtGroupProtIfDescr_Object=MibTableColumn
cienaOme6500OptmonsProtGroupProtIfDescr=_CienaOme6500OptmonsProtGroupProtIfDescr_Object((1,3,6,1,4,1,1271,29,7,2,1,5),_CienaOme6500OptmonsProtGroupProtIfDescr_Type())
cienaOme6500OptmonsProtGroupProtIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupProtIfDescr.setStatus(_A)
_CienaOme6500OptmonsProtGroupProtSst_Type=DisplayString
_CienaOme6500OptmonsProtGroupProtSst_Object=MibTableColumn
cienaOme6500OptmonsProtGroupProtSst=_CienaOme6500OptmonsProtGroupProtSst_Object((1,3,6,1,4,1,1271,29,7,2,1,6),_CienaOme6500OptmonsProtGroupProtSst_Type())
cienaOme6500OptmonsProtGroupProtSst.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupProtSst.setStatus(_A)
_CienaOme6500OptmonsProtGroupProtScheme_Type=DisplayString
_CienaOme6500OptmonsProtGroupProtScheme_Object=MibTableColumn
cienaOme6500OptmonsProtGroupProtScheme=_CienaOme6500OptmonsProtGroupProtScheme_Object((1,3,6,1,4,1,1271,29,7,2,1,7),_CienaOme6500OptmonsProtGroupProtScheme_Type())
cienaOme6500OptmonsProtGroupProtScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupProtScheme.setStatus(_A)
_CienaOme6500OptmonsProtGroupWaitToRestore_Type=DisplayString
_CienaOme6500OptmonsProtGroupWaitToRestore_Object=MibTableColumn
cienaOme6500OptmonsProtGroupWaitToRestore=_CienaOme6500OptmonsProtGroupWaitToRestore_Object((1,3,6,1,4,1,1271,29,7,2,1,8),_CienaOme6500OptmonsProtGroupWaitToRestore_Type())
cienaOme6500OptmonsProtGroupWaitToRestore.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupWaitToRestore.setStatus(_A)
_CienaOme6500OptmonsProtGroupDetectGuardTime_Type=DisplayString
_CienaOme6500OptmonsProtGroupDetectGuardTime_Object=MibTableColumn
cienaOme6500OptmonsProtGroupDetectGuardTime=_CienaOme6500OptmonsProtGroupDetectGuardTime_Object((1,3,6,1,4,1,1271,29,7,2,1,9),_CienaOme6500OptmonsProtGroupDetectGuardTime_Type())
cienaOme6500OptmonsProtGroupDetectGuardTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupDetectGuardTime.setStatus(_A)
_CienaOme6500OptmonsProtGroupRevertive_Type=DisplayString
_CienaOme6500OptmonsProtGroupRevertive_Object=MibTableColumn
cienaOme6500OptmonsProtGroupRevertive=_CienaOme6500OptmonsProtGroupRevertive_Object((1,3,6,1,4,1,1271,29,7,2,1,10),_CienaOme6500OptmonsProtGroupRevertive_Type())
cienaOme6500OptmonsProtGroupRevertive.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupRevertive.setStatus(_A)
_CienaOme6500OptmonsProtGroupRemStandard_Type=DisplayString
_CienaOme6500OptmonsProtGroupRemStandard_Object=MibTableColumn
cienaOme6500OptmonsProtGroupRemStandard=_CienaOme6500OptmonsProtGroupRemStandard_Object((1,3,6,1,4,1,1271,29,7,2,1,11),_CienaOme6500OptmonsProtGroupRemStandard_Type())
cienaOme6500OptmonsProtGroupRemStandard.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupRemStandard.setStatus(_A)
class _CienaOme6500OptmonsProtGroupLossPwr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('n',0),('y',1)))
_CienaOme6500OptmonsProtGroupLossPwr_Type.__name__=_C
_CienaOme6500OptmonsProtGroupLossPwr_Object=MibTableColumn
cienaOme6500OptmonsProtGroupLossPwr=_CienaOme6500OptmonsProtGroupLossPwr_Object((1,3,6,1,4,1,1271,29,7,2,1,12),_CienaOme6500OptmonsProtGroupLossPwr_Type())
cienaOme6500OptmonsProtGroupLossPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupLossPwr.setStatus(_A)
class _CienaOme6500OptmonsProtGroupTtops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('n',0),('y',1)))
_CienaOme6500OptmonsProtGroupTtops_Type.__name__=_C
_CienaOme6500OptmonsProtGroupTtops_Object=MibTableColumn
cienaOme6500OptmonsProtGroupTtops=_CienaOme6500OptmonsProtGroupTtops_Object((1,3,6,1,4,1,1271,29,7,2,1,13),_CienaOme6500OptmonsProtGroupTtops_Type())
cienaOme6500OptmonsProtGroupTtops.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupTtops.setStatus(_A)
class _CienaOme6500OptmonsProtGroupPsDirn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('uni',0),('bi',1)))
_CienaOme6500OptmonsProtGroupPsDirn_Type.__name__=_C
_CienaOme6500OptmonsProtGroupPsDirn_Object=MibTableColumn
cienaOme6500OptmonsProtGroupPsDirn=_CienaOme6500OptmonsProtGroupPsDirn_Object((1,3,6,1,4,1,1271,29,7,2,1,14),_CienaOme6500OptmonsProtGroupPsDirn_Type())
cienaOme6500OptmonsProtGroupPsDirn.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaOme6500OptmonsProtGroupPsDirn.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cienaOme6500OptmonsMIB':cienaOme6500OptmonsMIB,'cienaOme6500OptmonsTable':cienaOme6500OptmonsTable,'cienaOme6500OptmonsEntry':cienaOme6500OptmonsEntry,_E:cienaOme6500OptmonsIfIndex,'cienaOme6500OptmonsIfDescr':cienaOme6500OptmonsIfDescr,'cienaOme6500OptmonsSst':cienaOme6500OptmonsSst,'cienaOme6500OptmonsPst':cienaOme6500OptmonsPst,'cienaOme6500OptmonsAinsTimeLeft':cienaOme6500OptmonsAinsTimeLeft,'cienaOme6500OptmonsLosThres':cienaOme6500OptmonsLosThres,'cienaOme6500OptmonsPortLabel':cienaOme6500OptmonsPortLabel,'cienaOme6500OptmonsAlsoDisabled':cienaOme6500OptmonsAlsoDisabled,'cienaOme6500OptmonsProtNswSwStatus':cienaOme6500OptmonsProtNswSwStatus,'cienaOme6500OptmonsProtNswSwEnd':cienaOme6500OptmonsProtNswSwEnd,'cienaOme6500OptmonsProtNswSwReason':cienaOme6500OptmonsProtNswSwReason,'cienaOme6500OptmonsProtGroupTable':cienaOme6500OptmonsProtGroupTable,'cienaOme6500OptmonsProtGroupEntry':cienaOme6500OptmonsProtGroupEntry,_F:cienaOme6500OptmonsProtGroupWrkgIfIndex,'cienaOme6500OptmonsProtGroupWrkgIfDescr':cienaOme6500OptmonsProtGroupWrkgIfDescr,'cienaOme6500OptmonsProtGroupWrkgSst':cienaOme6500OptmonsProtGroupWrkgSst,_G:cienaOme6500OptmonsProtGroupProtIfIndex,'cienaOme6500OptmonsProtGroupProtIfDescr':cienaOme6500OptmonsProtGroupProtIfDescr,'cienaOme6500OptmonsProtGroupProtSst':cienaOme6500OptmonsProtGroupProtSst,'cienaOme6500OptmonsProtGroupProtScheme':cienaOme6500OptmonsProtGroupProtScheme,'cienaOme6500OptmonsProtGroupWaitToRestore':cienaOme6500OptmonsProtGroupWaitToRestore,'cienaOme6500OptmonsProtGroupDetectGuardTime':cienaOme6500OptmonsProtGroupDetectGuardTime,'cienaOme6500OptmonsProtGroupRevertive':cienaOme6500OptmonsProtGroupRevertive,'cienaOme6500OptmonsProtGroupRemStandard':cienaOme6500OptmonsProtGroupRemStandard,'cienaOme6500OptmonsProtGroupLossPwr':cienaOme6500OptmonsProtGroupLossPwr,'cienaOme6500OptmonsProtGroupTtops':cienaOme6500OptmonsProtGroupTtops,'cienaOme6500OptmonsProtGroupPsDirn':cienaOme6500OptmonsProtGroupPsDirn})