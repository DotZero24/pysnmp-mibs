_N='myIgmpFilteringProfileMIBGroup'
_M='myIgmpFilteringProfileRangeStatus'
_L='myIgmpFilteringProfieRangeEndAddress'
_K='myIgmpFilteringProfileStatus'
_J='myIgmpFilteringProfileAction'
_I='myIgmpFilteringMaxProfiles'
_H='myIgmpFilteringProfieRangeMyAddress'
_G='myIgmpFilteringProfileRangeIndex'
_F='myIgmpFilteringProfileIndex'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='MY-IGMP-FILTERINGPROFILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
IfIndex,=mibBuilder.importSymbols('MY-TC','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
myIgmpFilteringProfileMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,37))
if mibBuilder.loadTexts:myIgmpFilteringProfileMIB.setRevisions(('2003-12-09 00:00',))
_MyIgmpFilteringProfileMIBObjects_ObjectIdentity=ObjectIdentity
myIgmpFilteringProfileMIBObjects=_MyIgmpFilteringProfileMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,37,1))
_MyIgmpFilteringMaxProfiles_Type=Unsigned32
_MyIgmpFilteringMaxProfiles_Object=MibScalar
myIgmpFilteringMaxProfiles=_MyIgmpFilteringMaxProfiles_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,1),_MyIgmpFilteringMaxProfiles_Type())
myIgmpFilteringMaxProfiles.setMaxAccess(_E)
if mibBuilder.loadTexts:myIgmpFilteringMaxProfiles.setStatus(_A)
_MyIgmpFilteringProfileActionTable_Object=MibTable
myIgmpFilteringProfileActionTable=_MyIgmpFilteringProfileActionTable_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,2))
if mibBuilder.loadTexts:myIgmpFilteringProfileActionTable.setStatus(_A)
_MyIgmpFilteringProfileActionEntry_Object=MibTableRow
myIgmpFilteringProfileActionEntry=_MyIgmpFilteringProfileActionEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,2,1))
myIgmpFilteringProfileActionEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:myIgmpFilteringProfileActionEntry.setStatus(_A)
_MyIgmpFilteringProfileIndex_Type=Unsigned32
_MyIgmpFilteringProfileIndex_Object=MibTableColumn
myIgmpFilteringProfileIndex=_MyIgmpFilteringProfileIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,2,1,1),_MyIgmpFilteringProfileIndex_Type())
myIgmpFilteringProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:myIgmpFilteringProfileIndex.setStatus(_A)
class _MyIgmpFilteringProfileAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_MyIgmpFilteringProfileAction_Type.__name__=_D
_MyIgmpFilteringProfileAction_Object=MibTableColumn
myIgmpFilteringProfileAction=_MyIgmpFilteringProfileAction_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,2,1,2),_MyIgmpFilteringProfileAction_Type())
myIgmpFilteringProfileAction.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpFilteringProfileAction.setStatus(_A)
class _MyIgmpFilteringProfileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_MyIgmpFilteringProfileStatus_Type.__name__=_D
_MyIgmpFilteringProfileStatus_Object=MibTableColumn
myIgmpFilteringProfileStatus=_MyIgmpFilteringProfileStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,2,1,3),_MyIgmpFilteringProfileStatus_Type())
myIgmpFilteringProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpFilteringProfileStatus.setStatus(_A)
_MyIgmpFilteringProfileRangeTable_Object=MibTable
myIgmpFilteringProfileRangeTable=_MyIgmpFilteringProfileRangeTable_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,3))
if mibBuilder.loadTexts:myIgmpFilteringProfileRangeTable.setStatus(_A)
_MyIgmpFilteringProfileRangeEntry_Object=MibTableRow
myIgmpFilteringProfileRangeEntry=_MyIgmpFilteringProfileRangeEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,3,1))
myIgmpFilteringProfileRangeEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:myIgmpFilteringProfileRangeEntry.setStatus(_A)
_MyIgmpFilteringProfileRangeIndex_Type=Unsigned32
_MyIgmpFilteringProfileRangeIndex_Object=MibTableColumn
myIgmpFilteringProfileRangeIndex=_MyIgmpFilteringProfileRangeIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,3,1,1),_MyIgmpFilteringProfileRangeIndex_Type())
myIgmpFilteringProfileRangeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:myIgmpFilteringProfileRangeIndex.setStatus(_A)
_MyIgmpFilteringProfieRangeMyAddress_Type=IpAddress
_MyIgmpFilteringProfieRangeMyAddress_Object=MibTableColumn
myIgmpFilteringProfieRangeMyAddress=_MyIgmpFilteringProfieRangeMyAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,3,1,2),_MyIgmpFilteringProfieRangeMyAddress_Type())
myIgmpFilteringProfieRangeMyAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpFilteringProfieRangeMyAddress.setStatus(_A)
_MyIgmpFilteringProfieRangeEndAddress_Type=IpAddress
_MyIgmpFilteringProfieRangeEndAddress_Object=MibTableColumn
myIgmpFilteringProfieRangeEndAddress=_MyIgmpFilteringProfieRangeEndAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,3,1,3),_MyIgmpFilteringProfieRangeEndAddress_Type())
myIgmpFilteringProfieRangeEndAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpFilteringProfieRangeEndAddress.setStatus(_A)
_MyIgmpFilteringProfileRangeStatus_Type=RowStatus
_MyIgmpFilteringProfileRangeStatus_Object=MibTableColumn
myIgmpFilteringProfileRangeStatus=_MyIgmpFilteringProfileRangeStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,37,1,3,1,4),_MyIgmpFilteringProfileRangeStatus_Type())
myIgmpFilteringProfileRangeStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:myIgmpFilteringProfileRangeStatus.setStatus(_A)
_MyIgmpFilteringProfileMIBConformance_ObjectIdentity=ObjectIdentity
myIgmpFilteringProfileMIBConformance=_MyIgmpFilteringProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,37,2))
_MyIgmpFilteringProfileMIBCompliances_ObjectIdentity=ObjectIdentity
myIgmpFilteringProfileMIBCompliances=_MyIgmpFilteringProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,37,2,1))
_MyIgmpFilteringProfileMIBGroups_ObjectIdentity=ObjectIdentity
myIgmpFilteringProfileMIBGroups=_MyIgmpFilteringProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,37,2,2))
myIgmpFilteringProfileMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,37,2,2,1))
myIgmpFilteringProfileMIBGroup.setObjects(*((_B,_I),(_B,_F),(_B,_J),(_B,_K),(_B,_G),(_B,_H),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:myIgmpFilteringProfileMIBGroup.setStatus(_A)
myIgmpFilteringProfileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,37,2,1,1))
myIgmpFilteringProfileMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:myIgmpFilteringProfileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myIgmpFilteringProfileMIB':myIgmpFilteringProfileMIB,'myIgmpFilteringProfileMIBObjects':myIgmpFilteringProfileMIBObjects,_I:myIgmpFilteringMaxProfiles,'myIgmpFilteringProfileActionTable':myIgmpFilteringProfileActionTable,'myIgmpFilteringProfileActionEntry':myIgmpFilteringProfileActionEntry,_F:myIgmpFilteringProfileIndex,_J:myIgmpFilteringProfileAction,_K:myIgmpFilteringProfileStatus,'myIgmpFilteringProfileRangeTable':myIgmpFilteringProfileRangeTable,'myIgmpFilteringProfileRangeEntry':myIgmpFilteringProfileRangeEntry,_G:myIgmpFilteringProfileRangeIndex,_H:myIgmpFilteringProfieRangeMyAddress,_L:myIgmpFilteringProfieRangeEndAddress,_M:myIgmpFilteringProfileRangeStatus,'myIgmpFilteringProfileMIBConformance':myIgmpFilteringProfileMIBConformance,'myIgmpFilteringProfileMIBCompliances':myIgmpFilteringProfileMIBCompliances,'myIgmpFilteringProfileMIBCompliance':myIgmpFilteringProfileMIBCompliance,'myIgmpFilteringProfileMIBGroups':myIgmpFilteringProfileMIBGroups,_N:myIgmpFilteringProfileMIBGroup})