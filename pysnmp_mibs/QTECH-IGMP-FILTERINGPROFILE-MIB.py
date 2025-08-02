_O='qtechIgmpFilteringProfileMIBGroup'
_N='qtechIgmpFilteringProfileRangeStatus'
_M='qtechIgmpFilteringProfieRangeEndAddress'
_L='qtechIgmpFilteringProfileStatus'
_K='qtechIgmpFilteringProfileAction'
_J='qtechIgmpFilteringMaxProfiles'
_I='read-write'
_H='read-create'
_G='qtechIgmpFilteringProfieRangeQtechAddress'
_F='qtechIgmpFilteringProfileRangeIndex'
_E='qtechIgmpFilteringProfileIndex'
_D='read-only'
_C='Integer32'
_B='QTECH-IGMP-FILTERINGPROFILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
qtechIgmpFilteringProfileMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,37))
if mibBuilder.loadTexts:qtechIgmpFilteringProfileMIB.setRevisions(('2003-12-09 00:00',))
_QtechIgmpFilteringProfileMIBObjects_ObjectIdentity=ObjectIdentity
qtechIgmpFilteringProfileMIBObjects=_QtechIgmpFilteringProfileMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,37,1))
_QtechIgmpFilteringMaxProfiles_Type=Unsigned32
_QtechIgmpFilteringMaxProfiles_Object=MibScalar
qtechIgmpFilteringMaxProfiles=_QtechIgmpFilteringMaxProfiles_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,1),_QtechIgmpFilteringMaxProfiles_Type())
qtechIgmpFilteringMaxProfiles.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpFilteringMaxProfiles.setStatus(_A)
_QtechIgmpFilteringProfileActionTable_Object=MibTable
qtechIgmpFilteringProfileActionTable=_QtechIgmpFilteringProfileActionTable_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,2))
if mibBuilder.loadTexts:qtechIgmpFilteringProfileActionTable.setStatus(_A)
_QtechIgmpFilteringProfileActionEntry_Object=MibTableRow
qtechIgmpFilteringProfileActionEntry=_QtechIgmpFilteringProfileActionEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,2,1))
qtechIgmpFilteringProfileActionEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechIgmpFilteringProfileActionEntry.setStatus(_A)
_QtechIgmpFilteringProfileIndex_Type=Unsigned32
_QtechIgmpFilteringProfileIndex_Object=MibTableColumn
qtechIgmpFilteringProfileIndex=_QtechIgmpFilteringProfileIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,2,1,1),_QtechIgmpFilteringProfileIndex_Type())
qtechIgmpFilteringProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpFilteringProfileIndex.setStatus(_A)
class _QtechIgmpFilteringProfileAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_QtechIgmpFilteringProfileAction_Type.__name__=_C
_QtechIgmpFilteringProfileAction_Object=MibTableColumn
qtechIgmpFilteringProfileAction=_QtechIgmpFilteringProfileAction_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,2,1,2),_QtechIgmpFilteringProfileAction_Type())
qtechIgmpFilteringProfileAction.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechIgmpFilteringProfileAction.setStatus(_A)
class _QtechIgmpFilteringProfileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_QtechIgmpFilteringProfileStatus_Type.__name__=_C
_QtechIgmpFilteringProfileStatus_Object=MibTableColumn
qtechIgmpFilteringProfileStatus=_QtechIgmpFilteringProfileStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,2,1,3),_QtechIgmpFilteringProfileStatus_Type())
qtechIgmpFilteringProfileStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechIgmpFilteringProfileStatus.setStatus(_A)
_QtechIgmpFilteringProfileRangeTable_Object=MibTable
qtechIgmpFilteringProfileRangeTable=_QtechIgmpFilteringProfileRangeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,3))
if mibBuilder.loadTexts:qtechIgmpFilteringProfileRangeTable.setStatus(_A)
_QtechIgmpFilteringProfileRangeEntry_Object=MibTableRow
qtechIgmpFilteringProfileRangeEntry=_QtechIgmpFilteringProfileRangeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,3,1))
qtechIgmpFilteringProfileRangeEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:qtechIgmpFilteringProfileRangeEntry.setStatus(_A)
_QtechIgmpFilteringProfileRangeIndex_Type=Unsigned32
_QtechIgmpFilteringProfileRangeIndex_Object=MibTableColumn
qtechIgmpFilteringProfileRangeIndex=_QtechIgmpFilteringProfileRangeIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,3,1,1),_QtechIgmpFilteringProfileRangeIndex_Type())
qtechIgmpFilteringProfileRangeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpFilteringProfileRangeIndex.setStatus(_A)
_QtechIgmpFilteringProfieRangeQtechAddress_Type=IpAddress
_QtechIgmpFilteringProfieRangeQtechAddress_Object=MibTableColumn
qtechIgmpFilteringProfieRangeQtechAddress=_QtechIgmpFilteringProfieRangeQtechAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,3,1,2),_QtechIgmpFilteringProfieRangeQtechAddress_Type())
qtechIgmpFilteringProfieRangeQtechAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechIgmpFilteringProfieRangeQtechAddress.setStatus(_A)
_QtechIgmpFilteringProfieRangeEndAddress_Type=IpAddress
_QtechIgmpFilteringProfieRangeEndAddress_Object=MibTableColumn
qtechIgmpFilteringProfieRangeEndAddress=_QtechIgmpFilteringProfieRangeEndAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,3,1,3),_QtechIgmpFilteringProfieRangeEndAddress_Type())
qtechIgmpFilteringProfieRangeEndAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechIgmpFilteringProfieRangeEndAddress.setStatus(_A)
_QtechIgmpFilteringProfileRangeStatus_Type=RowStatus
_QtechIgmpFilteringProfileRangeStatus_Object=MibTableColumn
qtechIgmpFilteringProfileRangeStatus=_QtechIgmpFilteringProfileRangeStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,37,1,3,1,4),_QtechIgmpFilteringProfileRangeStatus_Type())
qtechIgmpFilteringProfileRangeStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechIgmpFilteringProfileRangeStatus.setStatus(_A)
_QtechIgmpFilteringProfileMIBConformance_ObjectIdentity=ObjectIdentity
qtechIgmpFilteringProfileMIBConformance=_QtechIgmpFilteringProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,37,2))
_QtechIgmpFilteringProfileMIBCompliances_ObjectIdentity=ObjectIdentity
qtechIgmpFilteringProfileMIBCompliances=_QtechIgmpFilteringProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,37,2,1))
_QtechIgmpFilteringProfileMIBGroups_ObjectIdentity=ObjectIdentity
qtechIgmpFilteringProfileMIBGroups=_QtechIgmpFilteringProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,37,2,2))
qtechIgmpFilteringProfileMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,37,2,2,1))
qtechIgmpFilteringProfileMIBGroup.setObjects(*((_B,_J),(_B,_E),(_B,_K),(_B,_L),(_B,_F),(_B,_G),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:qtechIgmpFilteringProfileMIBGroup.setStatus(_A)
qtechIgmpFilteringProfileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,37,2,1,1))
qtechIgmpFilteringProfileMIBCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:qtechIgmpFilteringProfileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechIgmpFilteringProfileMIB':qtechIgmpFilteringProfileMIB,'qtechIgmpFilteringProfileMIBObjects':qtechIgmpFilteringProfileMIBObjects,_J:qtechIgmpFilteringMaxProfiles,'qtechIgmpFilteringProfileActionTable':qtechIgmpFilteringProfileActionTable,'qtechIgmpFilteringProfileActionEntry':qtechIgmpFilteringProfileActionEntry,_E:qtechIgmpFilteringProfileIndex,_K:qtechIgmpFilteringProfileAction,_L:qtechIgmpFilteringProfileStatus,'qtechIgmpFilteringProfileRangeTable':qtechIgmpFilteringProfileRangeTable,'qtechIgmpFilteringProfileRangeEntry':qtechIgmpFilteringProfileRangeEntry,_F:qtechIgmpFilteringProfileRangeIndex,_G:qtechIgmpFilteringProfieRangeQtechAddress,_M:qtechIgmpFilteringProfieRangeEndAddress,_N:qtechIgmpFilteringProfileRangeStatus,'qtechIgmpFilteringProfileMIBConformance':qtechIgmpFilteringProfileMIBConformance,'qtechIgmpFilteringProfileMIBCompliances':qtechIgmpFilteringProfileMIBCompliances,'qtechIgmpFilteringProfileMIBCompliance':qtechIgmpFilteringProfileMIBCompliance,'qtechIgmpFilteringProfileMIBGroups':qtechIgmpFilteringProfileMIBGroups,_O:qtechIgmpFilteringProfileMIBGroup})