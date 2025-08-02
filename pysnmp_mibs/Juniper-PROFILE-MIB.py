_e='juniProfileIfGroup2'
_d='juniProfileIfGroup'
_c='juniProfAssignIfRangeProfileId'
_b='juniProfAssignIfRangeRowStatus'
_a='juniProfileIdName'
_Z='juniProfileNameId'
_Y='juniProfileNameRowStatus'
_X='juniProfToIfRangeMapRangeId'
_W='juniProfToIfRangeMapIndex'
_V='juniProfToIfRangeMapProfileId'
_U='juniProfAssignIfRangeRangeId'
_T='juniProfAssignIfRangeEncaps'
_S='juniProfAssignIfRangeIndex'
_R='juniProfToIfMapIndex'
_Q='juniProfToIfMapProfileId'
_P='juniProfAssignIfEncaps'
_O='juniProfAssignIfIndex'
_N='juniProfileIdId'
_M='obsolete'
_L='juniProfAssignIfProfileId'
_K='juniProfAssignIfRowStatus'
_J='juniProfToIfRangeMapEncaps'
_I='juniProfileNameName'
_H='DisplayString'
_G='juniProfileGroup'
_F='juniProfToIfMapEncaps'
_E='read-create'
_D='read-only'
_C='not-accessible'
_B='Juniper-PROFILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
juniProfileMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,25))
if mibBuilder.loadTexts:juniProfileMIB.setRevisions(('2003-01-31 21:18','2003-01-31 21:03','2002-11-19 20:47','2001-04-04 12:50','2000-04-20 00:00','1999-06-01 00:00'))
class JuniProfileIfEncaps(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,11,17,19,127)));namedValues=NamedValues(*(('ip',0),('ppp',1),('atm1483',11),('pppoe',17),('bridgedEthernet',19),('any',127)))
class JuniProfileRangeId(TextualConvention,Unsigned32):status=_A
_JuniProfileObjects_ObjectIdentity=ObjectIdentity
juniProfileObjects=_JuniProfileObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,25,1))
_JuniProfileName_ObjectIdentity=ObjectIdentity
juniProfileName=_JuniProfileName_ObjectIdentity((1,3,6,1,4,1,4874,2,2,25,1,1))
_JuniProfileNameTable_Object=MibTable
juniProfileNameTable=_JuniProfileNameTable_Object((1,3,6,1,4,1,4874,2,2,25,1,1,1))
if mibBuilder.loadTexts:juniProfileNameTable.setStatus(_A)
_JuniProfileNameEntry_Object=MibTableRow
juniProfileNameEntry=_JuniProfileNameEntry_Object((1,3,6,1,4,1,4874,2,2,25,1,1,1,1))
juniProfileNameEntry.setIndexNames((1,_B,_I))
if mibBuilder.loadTexts:juniProfileNameEntry.setStatus(_A)
class _JuniProfileNameName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_JuniProfileNameName_Type.__name__=_H
_JuniProfileNameName_Object=MibTableColumn
juniProfileNameName=_JuniProfileNameName_Object((1,3,6,1,4,1,4874,2,2,25,1,1,1,1,1),_JuniProfileNameName_Type())
juniProfileNameName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniProfileNameName.setStatus(_A)
_JuniProfileNameRowStatus_Type=RowStatus
_JuniProfileNameRowStatus_Object=MibTableColumn
juniProfileNameRowStatus=_JuniProfileNameRowStatus_Object((1,3,6,1,4,1,4874,2,2,25,1,1,1,1,2),_JuniProfileNameRowStatus_Type())
juniProfileNameRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniProfileNameRowStatus.setStatus(_A)
_JuniProfileNameId_Type=Unsigned32
_JuniProfileNameId_Object=MibTableColumn
juniProfileNameId=_JuniProfileNameId_Object((1,3,6,1,4,1,4874,2,2,25,1,1,1,1,3),_JuniProfileNameId_Type())
juniProfileNameId.setMaxAccess(_D)
if mibBuilder.loadTexts:juniProfileNameId.setStatus(_A)
_JuniProfileIdTable_Object=MibTable
juniProfileIdTable=_JuniProfileIdTable_Object((1,3,6,1,4,1,4874,2,2,25,1,1,2))
if mibBuilder.loadTexts:juniProfileIdTable.setStatus(_A)
_JuniProfileIdEntry_Object=MibTableRow
juniProfileIdEntry=_JuniProfileIdEntry_Object((1,3,6,1,4,1,4874,2,2,25,1,1,2,1))
juniProfileIdEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:juniProfileIdEntry.setStatus(_A)
_JuniProfileIdId_Type=Unsigned32
_JuniProfileIdId_Object=MibTableColumn
juniProfileIdId=_JuniProfileIdId_Object((1,3,6,1,4,1,4874,2,2,25,1,1,2,1,1),_JuniProfileIdId_Type())
juniProfileIdId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfileIdId.setStatus(_A)
class _JuniProfileIdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_JuniProfileIdName_Type.__name__=_H
_JuniProfileIdName_Object=MibTableColumn
juniProfileIdName=_JuniProfileIdName_Object((1,3,6,1,4,1,4874,2,2,25,1,1,2,1,2),_JuniProfileIdName_Type())
juniProfileIdName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniProfileIdName.setStatus(_A)
_JuniProfileAssign_ObjectIdentity=ObjectIdentity
juniProfileAssign=_JuniProfileAssign_ObjectIdentity((1,3,6,1,4,1,4874,2,2,25,1,2))
_JuniProfAssignIf_ObjectIdentity=ObjectIdentity
juniProfAssignIf=_JuniProfAssignIf_ObjectIdentity((1,3,6,1,4,1,4874,2,2,25,1,2,1))
_JuniProfAssignIfTable_Object=MibTable
juniProfAssignIfTable=_JuniProfAssignIfTable_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,1))
if mibBuilder.loadTexts:juniProfAssignIfTable.setStatus(_A)
_JuniProfAssignIfEntry_Object=MibTableRow
juniProfAssignIfEntry=_JuniProfAssignIfEntry_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,1,1))
juniProfAssignIfEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:juniProfAssignIfEntry.setStatus(_A)
_JuniProfAssignIfIndex_Type=InterfaceIndex
_JuniProfAssignIfIndex_Object=MibTableColumn
juniProfAssignIfIndex=_JuniProfAssignIfIndex_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,1,1,1),_JuniProfAssignIfIndex_Type())
juniProfAssignIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfAssignIfIndex.setStatus(_A)
_JuniProfAssignIfEncaps_Type=JuniProfileIfEncaps
_JuniProfAssignIfEncaps_Object=MibTableColumn
juniProfAssignIfEncaps=_JuniProfAssignIfEncaps_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,1,1,2),_JuniProfAssignIfEncaps_Type())
juniProfAssignIfEncaps.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfAssignIfEncaps.setStatus(_A)
_JuniProfAssignIfRowStatus_Type=RowStatus
_JuniProfAssignIfRowStatus_Object=MibTableColumn
juniProfAssignIfRowStatus=_JuniProfAssignIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,1,1,3),_JuniProfAssignIfRowStatus_Type())
juniProfAssignIfRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniProfAssignIfRowStatus.setStatus(_A)
_JuniProfAssignIfProfileId_Type=Unsigned32
_JuniProfAssignIfProfileId_Object=MibTableColumn
juniProfAssignIfProfileId=_JuniProfAssignIfProfileId_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,1,1,4),_JuniProfAssignIfProfileId_Type())
juniProfAssignIfProfileId.setMaxAccess(_E)
if mibBuilder.loadTexts:juniProfAssignIfProfileId.setStatus(_A)
_JuniProfToIfMapTable_Object=MibTable
juniProfToIfMapTable=_JuniProfToIfMapTable_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,2))
if mibBuilder.loadTexts:juniProfToIfMapTable.setStatus(_A)
_JuniProfToIfMapEntry_Object=MibTableRow
juniProfToIfMapEntry=_JuniProfToIfMapEntry_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,2,1))
juniProfToIfMapEntry.setIndexNames((0,_B,_Q),(0,_B,_R),(0,_B,_F))
if mibBuilder.loadTexts:juniProfToIfMapEntry.setStatus(_A)
_JuniProfToIfMapProfileId_Type=Unsigned32
_JuniProfToIfMapProfileId_Object=MibTableColumn
juniProfToIfMapProfileId=_JuniProfToIfMapProfileId_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,2,1,1),_JuniProfToIfMapProfileId_Type())
juniProfToIfMapProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfToIfMapProfileId.setStatus(_A)
_JuniProfToIfMapIndex_Type=InterfaceIndex
_JuniProfToIfMapIndex_Object=MibTableColumn
juniProfToIfMapIndex=_JuniProfToIfMapIndex_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,2,1,2),_JuniProfToIfMapIndex_Type())
juniProfToIfMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfToIfMapIndex.setStatus(_A)
_JuniProfToIfMapEncaps_Type=JuniProfileIfEncaps
_JuniProfToIfMapEncaps_Object=MibTableColumn
juniProfToIfMapEncaps=_JuniProfToIfMapEncaps_Object((1,3,6,1,4,1,4874,2,2,25,1,2,1,2,1,3),_JuniProfToIfMapEncaps_Type())
juniProfToIfMapEncaps.setMaxAccess(_D)
if mibBuilder.loadTexts:juniProfToIfMapEncaps.setStatus(_A)
_JuniProfAssignIfRange_ObjectIdentity=ObjectIdentity
juniProfAssignIfRange=_JuniProfAssignIfRange_ObjectIdentity((1,3,6,1,4,1,4874,2,2,25,1,2,2))
_JuniProfAssignIfRangeTable_Object=MibTable
juniProfAssignIfRangeTable=_JuniProfAssignIfRangeTable_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,1))
if mibBuilder.loadTexts:juniProfAssignIfRangeTable.setStatus(_A)
_JuniProfAssignIfRangeEntry_Object=MibTableRow
juniProfAssignIfRangeEntry=_JuniProfAssignIfRangeEntry_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,1,1))
juniProfAssignIfRangeEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:juniProfAssignIfRangeEntry.setStatus(_A)
_JuniProfAssignIfRangeIndex_Type=InterfaceIndex
_JuniProfAssignIfRangeIndex_Object=MibTableColumn
juniProfAssignIfRangeIndex=_JuniProfAssignIfRangeIndex_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,1,1,1),_JuniProfAssignIfRangeIndex_Type())
juniProfAssignIfRangeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfAssignIfRangeIndex.setStatus(_A)
_JuniProfAssignIfRangeEncaps_Type=JuniProfileIfEncaps
_JuniProfAssignIfRangeEncaps_Object=MibTableColumn
juniProfAssignIfRangeEncaps=_JuniProfAssignIfRangeEncaps_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,1,1,2),_JuniProfAssignIfRangeEncaps_Type())
juniProfAssignIfRangeEncaps.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfAssignIfRangeEncaps.setStatus(_A)
_JuniProfAssignIfRangeRangeId_Type=JuniProfileRangeId
_JuniProfAssignIfRangeRangeId_Object=MibTableColumn
juniProfAssignIfRangeRangeId=_JuniProfAssignIfRangeRangeId_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,1,1,3),_JuniProfAssignIfRangeRangeId_Type())
juniProfAssignIfRangeRangeId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfAssignIfRangeRangeId.setStatus(_A)
_JuniProfAssignIfRangeRowStatus_Type=RowStatus
_JuniProfAssignIfRangeRowStatus_Object=MibTableColumn
juniProfAssignIfRangeRowStatus=_JuniProfAssignIfRangeRowStatus_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,1,1,4),_JuniProfAssignIfRangeRowStatus_Type())
juniProfAssignIfRangeRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniProfAssignIfRangeRowStatus.setStatus(_A)
_JuniProfAssignIfRangeProfileId_Type=Unsigned32
_JuniProfAssignIfRangeProfileId_Object=MibTableColumn
juniProfAssignIfRangeProfileId=_JuniProfAssignIfRangeProfileId_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,1,1,5),_JuniProfAssignIfRangeProfileId_Type())
juniProfAssignIfRangeProfileId.setMaxAccess(_E)
if mibBuilder.loadTexts:juniProfAssignIfRangeProfileId.setStatus(_A)
_JuniProfToIfRangeMapTable_Object=MibTable
juniProfToIfRangeMapTable=_JuniProfToIfRangeMapTable_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,2))
if mibBuilder.loadTexts:juniProfToIfRangeMapTable.setStatus(_A)
_JuniProfToIfRangeMapEntry_Object=MibTableRow
juniProfToIfRangeMapEntry=_JuniProfToIfRangeMapEntry_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,2,1))
juniProfToIfRangeMapEntry.setIndexNames((0,_B,_V),(0,_B,_W),(0,_B,_J),(0,_B,_X))
if mibBuilder.loadTexts:juniProfToIfRangeMapEntry.setStatus(_A)
_JuniProfToIfRangeMapProfileId_Type=Unsigned32
_JuniProfToIfRangeMapProfileId_Object=MibTableColumn
juniProfToIfRangeMapProfileId=_JuniProfToIfRangeMapProfileId_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,2,1,1),_JuniProfToIfRangeMapProfileId_Type())
juniProfToIfRangeMapProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfToIfRangeMapProfileId.setStatus(_A)
_JuniProfToIfRangeMapIndex_Type=InterfaceIndex
_JuniProfToIfRangeMapIndex_Object=MibTableColumn
juniProfToIfRangeMapIndex=_JuniProfToIfRangeMapIndex_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,2,1,2),_JuniProfToIfRangeMapIndex_Type())
juniProfToIfRangeMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfToIfRangeMapIndex.setStatus(_A)
_JuniProfToIfRangeMapEncaps_Type=JuniProfileIfEncaps
_JuniProfToIfRangeMapEncaps_Object=MibTableColumn
juniProfToIfRangeMapEncaps=_JuniProfToIfRangeMapEncaps_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,2,1,3),_JuniProfToIfRangeMapEncaps_Type())
juniProfToIfRangeMapEncaps.setMaxAccess(_D)
if mibBuilder.loadTexts:juniProfToIfRangeMapEncaps.setStatus(_A)
_JuniProfToIfRangeMapRangeId_Type=JuniProfileRangeId
_JuniProfToIfRangeMapRangeId_Object=MibTableColumn
juniProfToIfRangeMapRangeId=_JuniProfToIfRangeMapRangeId_Object((1,3,6,1,4,1,4874,2,2,25,1,2,2,2,1,4),_JuniProfToIfRangeMapRangeId_Type())
juniProfToIfRangeMapRangeId.setMaxAccess(_C)
if mibBuilder.loadTexts:juniProfToIfRangeMapRangeId.setStatus(_A)
_JuniProfileMIBConformance_ObjectIdentity=ObjectIdentity
juniProfileMIBConformance=_JuniProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,25,4))
_JuniProfileMIBCompliances_ObjectIdentity=ObjectIdentity
juniProfileMIBCompliances=_JuniProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,25,4,1))
_JuniProfileMIBGroups_ObjectIdentity=ObjectIdentity
juniProfileMIBGroups=_JuniProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,25,4,2))
juniProfileGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,25,4,2,1))
juniProfileGroup.setObjects(*((_B,_I),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:juniProfileGroup.setStatus(_A)
juniProfileIfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,25,4,2,2))
juniProfileIfGroup.setObjects(*((_B,_K),(_B,_L),(_B,_F)))
if mibBuilder.loadTexts:juniProfileIfGroup.setStatus(_M)
juniProfileIfGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,25,4,2,3))
juniProfileIfGroup2.setObjects(*((_B,_K),(_B,_L),(_B,_F),(_B,_b),(_B,_c),(_B,_J)))
if mibBuilder.loadTexts:juniProfileIfGroup2.setStatus(_A)
juniProfileCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,25,4,1,1))
juniProfileCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:juniProfileCompliance.setStatus(_M)
juniProfileCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,25,4,1,2))
juniProfileCompliance2.setObjects(*((_B,_G),(_B,_d)))
if mibBuilder.loadTexts:juniProfileCompliance2.setStatus(_M)
juniProfileCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,25,4,1,3))
juniProfileCompliance3.setObjects(*((_B,_G),(_B,_e)))
if mibBuilder.loadTexts:juniProfileCompliance3.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'JuniProfileIfEncaps':JuniProfileIfEncaps,'JuniProfileRangeId':JuniProfileRangeId,'juniProfileMIB':juniProfileMIB,'juniProfileObjects':juniProfileObjects,'juniProfileName':juniProfileName,'juniProfileNameTable':juniProfileNameTable,'juniProfileNameEntry':juniProfileNameEntry,_I:juniProfileNameName,_Y:juniProfileNameRowStatus,_Z:juniProfileNameId,'juniProfileIdTable':juniProfileIdTable,'juniProfileIdEntry':juniProfileIdEntry,_N:juniProfileIdId,_a:juniProfileIdName,'juniProfileAssign':juniProfileAssign,'juniProfAssignIf':juniProfAssignIf,'juniProfAssignIfTable':juniProfAssignIfTable,'juniProfAssignIfEntry':juniProfAssignIfEntry,_O:juniProfAssignIfIndex,_P:juniProfAssignIfEncaps,_K:juniProfAssignIfRowStatus,_L:juniProfAssignIfProfileId,'juniProfToIfMapTable':juniProfToIfMapTable,'juniProfToIfMapEntry':juniProfToIfMapEntry,_Q:juniProfToIfMapProfileId,_R:juniProfToIfMapIndex,_F:juniProfToIfMapEncaps,'juniProfAssignIfRange':juniProfAssignIfRange,'juniProfAssignIfRangeTable':juniProfAssignIfRangeTable,'juniProfAssignIfRangeEntry':juniProfAssignIfRangeEntry,_S:juniProfAssignIfRangeIndex,_T:juniProfAssignIfRangeEncaps,_U:juniProfAssignIfRangeRangeId,_b:juniProfAssignIfRangeRowStatus,_c:juniProfAssignIfRangeProfileId,'juniProfToIfRangeMapTable':juniProfToIfRangeMapTable,'juniProfToIfRangeMapEntry':juniProfToIfRangeMapEntry,_V:juniProfToIfRangeMapProfileId,_W:juniProfToIfRangeMapIndex,_J:juniProfToIfRangeMapEncaps,_X:juniProfToIfRangeMapRangeId,'juniProfileMIBConformance':juniProfileMIBConformance,'juniProfileMIBCompliances':juniProfileMIBCompliances,'juniProfileCompliance':juniProfileCompliance,'juniProfileCompliance2':juniProfileCompliance2,'juniProfileCompliance3':juniProfileCompliance3,'juniProfileMIBGroups':juniProfileMIBGroups,_G:juniProfileGroup,_d:juniProfileIfGroup,_e:juniProfileIfGroup2})