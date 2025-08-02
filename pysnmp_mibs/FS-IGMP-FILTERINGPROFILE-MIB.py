_O='fsIgmpFilteringProfileMIBGroup'
_N='fsIgmpFilteringProfileRangeStatus'
_M='fsIgmpFilteringProfieRangeEndAddress'
_L='fsIgmpFilteringProfileStatus'
_K='fsIgmpFilteringProfileAction'
_J='fsIgmpFilteringMaxProfiles'
_I='read-write'
_H='read-create'
_G='fsIgmpFilteringProfieRangeFSAddress'
_F='fsIgmpFilteringProfileRangeIndex'
_E='fsIgmpFilteringProfileIndex'
_D='read-only'
_C='Integer32'
_B='FS-IGMP-FILTERINGPROFILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsIgmpFilteringProfileMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,37))
if mibBuilder.loadTexts:fsIgmpFilteringProfileMIB.setRevisions(('2003-12-09 00:00',))
_FsIgmpFilteringProfileMIBObjects_ObjectIdentity=ObjectIdentity
fsIgmpFilteringProfileMIBObjects=_FsIgmpFilteringProfileMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,37,1))
_FsIgmpFilteringMaxProfiles_Type=Unsigned32
_FsIgmpFilteringMaxProfiles_Object=MibScalar
fsIgmpFilteringMaxProfiles=_FsIgmpFilteringMaxProfiles_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,1),_FsIgmpFilteringMaxProfiles_Type())
fsIgmpFilteringMaxProfiles.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpFilteringMaxProfiles.setStatus(_A)
_FsIgmpFilteringProfileActionTable_Object=MibTable
fsIgmpFilteringProfileActionTable=_FsIgmpFilteringProfileActionTable_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,2))
if mibBuilder.loadTexts:fsIgmpFilteringProfileActionTable.setStatus(_A)
_FsIgmpFilteringProfileActionEntry_Object=MibTableRow
fsIgmpFilteringProfileActionEntry=_FsIgmpFilteringProfileActionEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,2,1))
fsIgmpFilteringProfileActionEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsIgmpFilteringProfileActionEntry.setStatus(_A)
_FsIgmpFilteringProfileIndex_Type=Unsigned32
_FsIgmpFilteringProfileIndex_Object=MibTableColumn
fsIgmpFilteringProfileIndex=_FsIgmpFilteringProfileIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,2,1,1),_FsIgmpFilteringProfileIndex_Type())
fsIgmpFilteringProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpFilteringProfileIndex.setStatus(_A)
class _FsIgmpFilteringProfileAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_FsIgmpFilteringProfileAction_Type.__name__=_C
_FsIgmpFilteringProfileAction_Object=MibTableColumn
fsIgmpFilteringProfileAction=_FsIgmpFilteringProfileAction_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,2,1,2),_FsIgmpFilteringProfileAction_Type())
fsIgmpFilteringProfileAction.setMaxAccess(_I)
if mibBuilder.loadTexts:fsIgmpFilteringProfileAction.setStatus(_A)
class _FsIgmpFilteringProfileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_FsIgmpFilteringProfileStatus_Type.__name__=_C
_FsIgmpFilteringProfileStatus_Object=MibTableColumn
fsIgmpFilteringProfileStatus=_FsIgmpFilteringProfileStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,2,1,3),_FsIgmpFilteringProfileStatus_Type())
fsIgmpFilteringProfileStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsIgmpFilteringProfileStatus.setStatus(_A)
_FsIgmpFilteringProfileRangeTable_Object=MibTable
fsIgmpFilteringProfileRangeTable=_FsIgmpFilteringProfileRangeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,3))
if mibBuilder.loadTexts:fsIgmpFilteringProfileRangeTable.setStatus(_A)
_FsIgmpFilteringProfileRangeEntry_Object=MibTableRow
fsIgmpFilteringProfileRangeEntry=_FsIgmpFilteringProfileRangeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,3,1))
fsIgmpFilteringProfileRangeEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:fsIgmpFilteringProfileRangeEntry.setStatus(_A)
_FsIgmpFilteringProfileRangeIndex_Type=Unsigned32
_FsIgmpFilteringProfileRangeIndex_Object=MibTableColumn
fsIgmpFilteringProfileRangeIndex=_FsIgmpFilteringProfileRangeIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,3,1,1),_FsIgmpFilteringProfileRangeIndex_Type())
fsIgmpFilteringProfileRangeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpFilteringProfileRangeIndex.setStatus(_A)
_FsIgmpFilteringProfieRangeFSAddress_Type=IpAddress
_FsIgmpFilteringProfieRangeFSAddress_Object=MibTableColumn
fsIgmpFilteringProfieRangeFSAddress=_FsIgmpFilteringProfieRangeFSAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,3,1,2),_FsIgmpFilteringProfieRangeFSAddress_Type())
fsIgmpFilteringProfieRangeFSAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:fsIgmpFilteringProfieRangeFSAddress.setStatus(_A)
_FsIgmpFilteringProfieRangeEndAddress_Type=IpAddress
_FsIgmpFilteringProfieRangeEndAddress_Object=MibTableColumn
fsIgmpFilteringProfieRangeEndAddress=_FsIgmpFilteringProfieRangeEndAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,3,1,3),_FsIgmpFilteringProfieRangeEndAddress_Type())
fsIgmpFilteringProfieRangeEndAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:fsIgmpFilteringProfieRangeEndAddress.setStatus(_A)
_FsIgmpFilteringProfileRangeStatus_Type=RowStatus
_FsIgmpFilteringProfileRangeStatus_Object=MibTableColumn
fsIgmpFilteringProfileRangeStatus=_FsIgmpFilteringProfileRangeStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,37,1,3,1,4),_FsIgmpFilteringProfileRangeStatus_Type())
fsIgmpFilteringProfileRangeStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsIgmpFilteringProfileRangeStatus.setStatus(_A)
_FsIgmpFilteringProfileMIBConformance_ObjectIdentity=ObjectIdentity
fsIgmpFilteringProfileMIBConformance=_FsIgmpFilteringProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,37,2))
_FsIgmpFilteringProfileMIBCompliances_ObjectIdentity=ObjectIdentity
fsIgmpFilteringProfileMIBCompliances=_FsIgmpFilteringProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,37,2,1))
_FsIgmpFilteringProfileMIBGroups_ObjectIdentity=ObjectIdentity
fsIgmpFilteringProfileMIBGroups=_FsIgmpFilteringProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,37,2,2))
fsIgmpFilteringProfileMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,37,2,2,1))
fsIgmpFilteringProfileMIBGroup.setObjects(*((_B,_J),(_B,_E),(_B,_K),(_B,_L),(_B,_F),(_B,_G),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:fsIgmpFilteringProfileMIBGroup.setStatus(_A)
fsIgmpFilteringProfileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,37,2,1,1))
fsIgmpFilteringProfileMIBCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:fsIgmpFilteringProfileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsIgmpFilteringProfileMIB':fsIgmpFilteringProfileMIB,'fsIgmpFilteringProfileMIBObjects':fsIgmpFilteringProfileMIBObjects,_J:fsIgmpFilteringMaxProfiles,'fsIgmpFilteringProfileActionTable':fsIgmpFilteringProfileActionTable,'fsIgmpFilteringProfileActionEntry':fsIgmpFilteringProfileActionEntry,_E:fsIgmpFilteringProfileIndex,_K:fsIgmpFilteringProfileAction,_L:fsIgmpFilteringProfileStatus,'fsIgmpFilteringProfileRangeTable':fsIgmpFilteringProfileRangeTable,'fsIgmpFilteringProfileRangeEntry':fsIgmpFilteringProfileRangeEntry,_F:fsIgmpFilteringProfileRangeIndex,_G:fsIgmpFilteringProfieRangeFSAddress,_M:fsIgmpFilteringProfieRangeEndAddress,_N:fsIgmpFilteringProfileRangeStatus,'fsIgmpFilteringProfileMIBConformance':fsIgmpFilteringProfileMIBConformance,'fsIgmpFilteringProfileMIBCompliances':fsIgmpFilteringProfileMIBCompliances,'fsIgmpFilteringProfileMIBCompliance':fsIgmpFilteringProfileMIBCompliance,'fsIgmpFilteringProfileMIBGroups':fsIgmpFilteringProfileMIBGroups,_O:fsIgmpFilteringProfileMIBGroup})